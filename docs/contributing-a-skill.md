# Author a workflow

Keep SKILL.md brief with name matching directory and a concise trigger description.
Use simple English and link supporting references. Each directory includes its own
MIT license, README, OpenAI interface metadata, policy, data quality, tool map, report
template and synthetic sample. Follow https://agentskills.io/specification.

The offline validator deliberately accepts our simple scalar frontmatter convention;
that restriction is local, not the entire Agent Skills YAML standard. Do not add
wildcard allowed-tools. Metadata cannot preauthorize the service's full catalog.

Edit shared-source first, then run scripts/sync_shared.py. Update tool maps against
contracts/tools.json and actual exposed schemas. Test a single copied directory
without siblings. Add relevant prompts, synthetic inputs and output/side-effect
assertions in evals/cases.json. Report static, transcript and native-agent results
separately. Preserve names and scope; optional provider or save branches need their
own explicit intent and quota/write checks.
