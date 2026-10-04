# Compatibility evidence

**No clean live-client compatibility is claimed for catalog 0.1.0.** Offline package
isolation is automated. Private production OAuth and backend cases recorded by the
existing plugins do not validate native installed workflows in a client.

| Client | Version / date | Clean install | Skill detection | OAuth | First analytic query | Errors | Update |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Claude Code | Not recorded | Pending | Pending | Pending for this catalog | Pending | Pending | Pending |
| Codex | Not recorded | Pending | Pending | Pending for this catalog | Pending | Pending | Pending |
| ChatGPT plugin | Not recorded | Directory review pending | Native runtime pending | Prior plugin evidence only | Pending for this catalog | Pending | Pending |
| Cursor | Not recorded | Pending | Pending | Pending | Pending | Pending | Pending |

Every skill has live-client-validation-pending status in catalog.json, including
indexing, change evaluation and provider workflows. Main priorities are
content-planning, ctr-opportunities and search-review in Claude Code and Codex.

For each real run, record client/model version, date, exact catalog commit/version,
endpoint, prompt, property authorization, anonymized calls, coverage, result and
failures. Run representative cases more than once; include plugin plus standalone
coexistence. Obtain explicit authorization for a controlled property and any cost.
Do not store credentials or private property data here. All critical cases must pass
and all three main workflows must yield checked analytics in both initial clients
before advertising compatibility. Keep unsupported paths visibly pending.

Fixture assertions and static file checks cannot show that a model picks the right
tool, interprets real results correctly or that browser OAuth succeeds.

## Offline installer evidence — 2026-10-04

Skills CLI 1.7.0 discovered all seven local workflows. ctr-opportunities was
installed with --copy into separate temporary project directories for Claude Code
and Codex; each installed payload was compared byte-for-byte with its source.
This tests CLI selection and file installation, not native detection, OAuth or
agent behavior.

## Public repository discovery — 2026-10-04

`npx skills@1.7.0 add hypergsc/skills --list` successfully cloned the public
repository and discovered all seven workflows. This checks remote discovery;
clean installation, native detection, OAuth and analytic behavior remain pending.

The bundled legacy skill quick-validator rejects the specification-supported
compatibility field. All seven frontmatter and OpenAI metadata files were parsed
with PyYAML 6.0.3 and checked against the catalog constraints; the catalog's offline
validator accepts that field. The [public Agent Skills specification](https://agentskills.io/specification)
remains the format reference. No project dependencies were added for this YAML check.
