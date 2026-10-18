# Catalog contributor instructions

This repository is the authoring source for seven standalone SEO skills. Preserve
slugs and the existing OAuth endpoint https://hypergsc.com/mcp. Update shared
policies in shared-source, then run scripts/sync_shared.py. Never hand-edit copies
inside skills/*/references/execution-policy.md or data-quality.md.

Each skill must work when copied alone. Keep its required references and MIT notice
inside the directory. No sibling dependencies, symlinks, executable runtime scripts,
embedded credentials, hidden tracking or downloaded instructions. English source;
reports follow the user's language. Do not widen live query or paid-provider scope.

Change reviewed tool semantics in contracts/tools.json only against actual source
and exposed schemas. Preserve live-client-validation-pending until recorded real
client evidence supports a deliberate compatibility update (and update validation).
Static checks, transcript checks and native client evaluation are distinct.

Run python3 scripts/validate.py before exporting. The application repository's
scripts/plugin-bundles.py maintains platform manifests and generated payloads;
changes made in distribution repositories must flow back here before re-export.
