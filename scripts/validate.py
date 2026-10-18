"""Offline format, contract, isolation and generated-reference checks; no live agents."""

import argparse
import json
import re
import tempfile
from pathlib import Path

from export_skills import inventory
from sync_shared import sync

ROOT = Path(__file__).resolve().parents[1]
SLUGS = {
    "search-review",
    "ctr-opportunities",
    "content-planning",
    "indexing-check",
    "change-evaluation",
    "competitor-research",
    "backlink-gap",
}
FILES = {
    "SKILL.md",
    "README.md",
    "LICENSE",
    "agents/openai.yaml",
    *{
        f"references/{name}.md"
        for name in (
            "execution-policy",
            "data-quality",
            "tool-map",
            "report-template",
            "sample-report",
        )
    },
}
SECRET = re.compile(
    r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|gh[pousr]_[A-Za-z0-9]{30,}|AKIA[A-Z0-9]{16}"
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def validate_skill(skill, tools):
    files = inventory(skill)
    require(
        set(files) == FILES,
        f"Unexpected or missing skill files: {skill}: {set(files) ^ FILES}",
    )
    text = (skill / "SKILL.md").read_text()
    header = re.fullmatch(
        r"---\nname: ([a-z0-9]+(?:-[a-z0-9]+)*)\ndescription: ([^\n]+)\nlicense: MIT\ncompatibility: ([^\n]+)\n---\n([\s\S]+)",
        text,
    )
    require(
        header and header[1] == skill.name and len(header[1]) <= 64,
        f"Invalid frontmatter: {skill}",
    )
    require(
        0 < len(header[2]) <= 1024 and len(header[3]) <= 500,
        f"Invalid metadata length: {skill}",
    )
    allowed = (
        set(tools)
        | {p for value in tools.values() for p in value["parameters"]}
        | {"next_offset", "version"}
    )
    for name in files:
        path = skill / name
        content = path.read_text()
        require(not SECRET.search(content), f"Credential pattern in {path}")
        require("../../" not in content, f"External skill dependency: {path}")
        require(
            "allowed-tools:" not in content, f"Unexpected tool preauthorization: {path}"
        )
        for tool in re.findall(r"`([a-z][a-z0-9]*_[a-z0-9_]+)`", content):
            require(tool in allowed, f"Unknown tool or parameter {tool}: {path}")
        for url in re.findall(r"https://hypergsc\.com/mcp[^\s\"<>`)]*", content):
            require(
                url == "https://hypergsc.com/mcp",
                f"Unexpected MCP endpoint: {path}",
            )
        for link in re.findall(r"\[[^\]]*\]\(([^)]+)\)", content):
            if re.match(r"(?:https?://|mailto:|#)", link):
                continue
            target = (path.parent / link.split("#")[0]).resolve()
            require(
                target.is_relative_to(skill.resolve()) and target.is_file(),
                f"Missing or escaping reference: {path}: {link}",
            )
        for ref in re.findall(r"`(references/[^`]+)`", content):
            require((skill / ref).is_file(), f"Missing reference: {ref}")
    ui = (skill / "agents/openai.yaml").read_text()
    require(
        f"${skill.name}" in ui and 'value: "hypergsc"' in ui,
        f"Invalid OpenAI metadata: {skill}",
    )
    require(
        'url: "https://hypergsc.com/mcp"' in ui,
        f"Unexpected OpenAI dependency: {skill}",
    )
    return files


def validate(root=ROOT):
    catalog = json.loads((root / "catalog.json").read_text())
    tools = json.loads((root / "contracts/tools.json").read_text())["tools"]
    require(
        {s["slug"] for s in catalog["skills"]} == SLUGS and len(catalog["skills"]) == 7,
        "Expected seven unique workflows",
    )
    require(
        {p.name for p in (root / "skills").iterdir()} == SLUGS,
        "Unexpected skill directory",
    )
    require(
        re.fullmatch(r"\d+\.\d+\.\d+", catalog["version"]), "Invalid catalog version"
    )
    sync(root, check=True)
    for entry in catalog["skills"]:
        require(
            set(entry["tools"]) <= set(tools), f"Unknown catalog tool: {entry['slug']}"
        )
        require(
            entry["validation"] == "live-client-validation-pending",
            "Do not infer compatibility from static validation",
        )
        skill = root / "skills" / entry["slug"]
        validate_skill(skill, tools)
        # Copy just this directory; references must resolve with no sibling skills.
        import shutil

        with tempfile.TemporaryDirectory() as directory:
            isolated = Path(directory) / skill.name
            shutil.copytree(skill, isolated)
            validate_skill(isolated, tools)
    cases = json.loads((root / "evals/cases.json").read_text())
    require(
        len(cases) >= 14 and len({c["id"] for c in cases}) == len(cases),
        "Missing evaluation cases",
    )
    for case in cases:
        require(
            case["prompt"] and case["fixture"] and case["assertions"],
            f"Incomplete evaluation: {case['id']}",
        )
    return catalog


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    result = validate()
    print(
        f"Validated catalog {result['version']}: seven isolated skill packages. Live behavior remains unverified."
    )
