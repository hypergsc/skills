"""Check normalized synthetic/client traces; this does not execute a model."""

import argparse
import json
from pathlib import Path

WRITE_TOOLS = {
    "save_keywords",
    "update_project_context",
    "clear_project_context",
    "record_seo_change",
    "delete_seo_change",
    "delete_saved_keywords",
}
PROVIDER_TOOLS = {
    "keyword_research",
    "competitor_keyword_gap",
    "competitor_domain_overview",
    "competitor_top_pages",
    "backlink_gap",
    "referring_domains",
}
SALES_TOOLS = {
    "create_checkout",
    "upgrade_plan",
    "preview_upgrade",
    "get_billing_link",
    "list_plans",
}
DISCOVERY = {"get_capabilities", "list_properties"}
BUDGETS = {"content-planning": 5, "ctr-opportunities": 4, "search-review": 6}


def check(trace):
    failures = []
    exhausted = False
    analytic = 0
    ambiguous_provider_calls = set()
    for call in trace["calls"]:
        tool = call["tool"]
        arguments = call.get("arguments", {})
        if tool in SALES_TOOLS:
            failures.append("Subscription sales call")
        if tool in WRITE_TOOLS and not trace.get("save_requested", False):
            failures.append("Unrequested write")
        if tool in PROVIDER_TOOLS and not trace.get("provider_requested", False):
            failures.append("Unrequested provider")
        signature = (tool, json.dumps(arguments, sort_keys=True))
        if signature in ambiguous_provider_calls and not trace.get(
            "retry_requested", False
        ):
            failures.append("Ambiguous billable provider call retried automatically")
        if (
            tool in PROVIDER_TOOLS
            and call.get("error")
            and call.get("dispatched") is not False
        ):
            ambiguous_provider_calls.add(signature)
        if exhausted and tool not in DISCOVERY:
            failures.append("Analysis continued after quota exhaustion")
        if "site_url" in arguments and arguments["site_url"] != trace.get("site_url"):
            failures.append("Property scope changed")
        if (
            trace.get("connection_id")
            and "connection_id" in arguments
            and arguments["connection_id"] != trace["connection_id"]
        ):
            failures.append("Connection scope changed")
        if not trace.get("property_resolved", True) and tool not in DISCOVERY:
            failures.append("Analysis before property resolution")
        if trace.get("unrelated", False):
            failures.append("HyperGSC called for unrelated task")
        if tool not in DISCOVERY:
            analytic += 1
        exhausted = exhausted or call.get("error") in {
            "QUOTA_EXHAUSTED",
            "ALLOWANCE_EXHAUSTED",
            "QUOTA_EXCEEDED",
        }
    if analytic > BUDGETS.get(trace["skill"], float("inf")) and not trace.get(
        "expanded_scope_requested", False
    ):
        failures.append("Initial analytical budget exceeded")
    return failures


def self_test():
    valid = {
        "skill": "ctr-opportunities",
        "site_url": "sc-domain:example.com",
        "calls": [
            {
                "tool": "get_advanced_search_analytics",
                "arguments": {"site_url": "sc-domain:example.com"},
            }
        ],
    }
    assert not check(valid)
    for call, expected in [
        ({"tool": "save_keywords"}, "Unrequested write"),
        ({"tool": "keyword_research"}, "Unrequested provider"),
        ({"tool": "create_checkout"}, "Subscription sales call"),
        (
            {
                "tool": "get_advanced_search_analytics",
                "arguments": {"site_url": "sc-domain:example.org"},
            },
            "Property scope changed",
        ),
    ]:
        assert expected in check({**valid, "calls": [call]})
    assert "Analysis continued after quota exhaustion" in check(
        {
            **valid,
            "calls": [
                {"tool": "get_advanced_search_analytics", "error": "QUOTA_EXCEEDED"},
                valid["calls"][0],
            ],
        }
    )
    assert "Initial analytical budget exceeded" in check(
        {**valid, "calls": valid["calls"] * 5}
    )
    assert check({**valid, "property_resolved": False})
    assert check({**valid, "unrelated": True})
    assert "Ambiguous billable provider call retried automatically" in check(
        {
            **valid,
            "provider_requested": True,
            "calls": [
                {"tool": "keyword_research", "error": "PROVIDER_TIMEOUT"},
                {"tool": "keyword_research"},
            ],
        }
    )
    print(
        "Synthetic transcript checker self-tests passed; native agent behavior unverified."
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("transcript", nargs="?", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
    elif args.transcript:
        failures = check(json.loads(args.transcript.read_text()))
        if failures:
            raise SystemExit("\n".join(failures))
        print(
            "Trace side-effect checks passed. Analytical/human assertions remain required."
        )
    else:
        parser.error("Provide a transcript or --self-test")
