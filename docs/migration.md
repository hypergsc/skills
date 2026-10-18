# Migration inventory and source ownership

Inventory performed 2026-10-04 using public Git trees:

- Claude: bc18098d98b5714593f44db6c07273e6a0257f6e
- ChatGPT/Codex: c17c2a9fb88a30649e22495c0f8d807536e06f36
- Private application baseline: dd90142652fb41438b25495014bd1a2e7e3d12c3

All seven public SKILL.md blobs match each other and the private baseline.
[source-skills.json](source-skills.json) records original Git blobs and SHA-256
hashes. The public trees contain no LICENSE or NOTICE files. The imported texts are
HyperGSC-authored; MIT is applied only to this catalog's own files and tooling.
No dependency or hosted backend is relicensed.

The existing private exporter was found at scripts/plugin-bundles.py. Its canonical
authoring input is now plugins/skills-catalog; plugins/hypergsc/skills is a generated
copy. The exporter emits the public skills repository and both plugin repositories.
This preserves one authoring source while enabling a public standalone catalog.
After publishing, record its exact commit in plugin payload provenance using
--skills-source-commit. Local draft exports use null and explicitly say unpublished;
the application commit must not be mislabeled as the public catalog commit.

Platform differences are manifests, marketplace and HTTP transport configuration.
Skill payloads are byte-identical. Claude and OpenAI use /mcp. Each plugin
carries all files, license copies and skills-source.json with per-file SHA-256 hashes.
No submodules, runtime downloads or branch-following updates.

Review generated payload diffs before distribution. Roll back by regenerating from
the previous reviewed catalog commit and restoring its paired plugin version and
provenance. Keep the old marketplace identity and skill slugs. Do not update an
existing OAuth connection silently. Publishing and distribution PRs are separate
from preparing these local exports.
