# SEO skills for your real Search Console data

Find pages to improve, investigate search changes and review Google Search Console
with your AI. These Agent Skills describe the procedure; HyperGSC supplies the MCP
tools. Claude Code and Codex plugins package both for their clients.

| Workflow | Result | Example question |
| --- | --- | --- |
| [content-planning](skills/content-planning/README.md) | Pages worth improving | Which five existing pages should I improve next? |
| [ctr-opportunities](skills/ctr-opportunities/README.md) | Search snippet experiments | Which pages get impressions but few clicks? |
| [search-review](skills/search-review/README.md) | Weekly review and next actions | Review my latest complete week. |

Also available: [indexing-check](skills/indexing-check/README.md),
[change-evaluation](skills/change-evaluation/README.md),
[competitor-research](skills/competitor-research/README.md), and
[backlink-gap](skills/backlink-gap/README.md). Provider workflows are optional;
none run automatically as part of the examples.

## Preview without an account

**Synthetic example — not your site data.**

| Metric | Previous week | Latest week | Change |
| --- | --- | --- | --- |
| Clicks | 200 | 240 | +40 (+20%) |
| Impressions | 10,000 | 12,000 | +2,000 (+20%) |
| CTR | 2.0% | 2.0% | 0.0 percentage points |

Property: sc-domain:example.com. Pacific dates: 2026-09-14–20 vs 2026-09-21–27.
Unfiltered WEB; synthetic totals. This does not establish a cause for the change.
[See the complete sample and actions](skills/search-review/references/sample-report.md).

## Installation and connection

Install from [hypergsc/skills](https://github.com/hypergsc/skills). Clean live-client
validation is pending; installation does not establish native detection, OAuth or
analytic behavior. Choose a workflow and your client:

```sh
npx skills add hypergsc/skills --list
npx skills add hypergsc/skills
npx skills add hypergsc/skills --skill ctr-opportunities -a claude-code
npx skills add hypergsc/skills --skill ctr-opportunities -a codex
```

For local packaging evaluation, run `npx skills add /absolute/path/to/this/repository --list`
and select one skill interactively. Do not use automated repeated installs as a
ranking signal. CLI privacy settings and telemetry belong to the CLI, not these skills.

Installing a skill and connecting data are separate steps:

1. Install one workflow for your chosen client and project. Global install is optional.
2. Sign in at [HyperGSC](https://hypergsc.com/?utm_source=github&utm_medium=skills&utm_campaign=skills-catalog),
   connect Google and enable your property. Reuse an existing HyperGSC MCP connection
   or configure the client using [the connection guide](https://hypergsc.com/agent-setup/prompt.md).
3. Complete browser OAuth for the client, then ask the example question.

Free, open-source SEO workflows. Live analysis requires a connected HyperGSC account
and an enabled Search Console property. Available tools and usage depend on your
account. You can preview a sample report without connecting an account. Hosted
service, third-party providers and model usage are separate from the free download.
Do not paste secrets in chat.

[Installation](docs/installation.md) · [Compatibility and pending live tests](docs/compatibility.md)
· [Migration](docs/migration.md) · [Release process](docs/release-process.md)

## Contribute

[Contributing](CONTRIBUTING.md) explains standalone packaging and synthetic fixtures.
Run `python3 scripts/sync_shared.py --check` and `python3 scripts/validate.py`.
These checks validate files and isolation; they do not prove model behavior.
The [MIT license](LICENSE) covers this repository's own workflow files and tooling,
not HyperGSC's hosted backend or dependencies. Report private issues through
[the security policy](SECURITY.md).
