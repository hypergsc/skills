# Release process

1. Review the catalog version, changes, source provenance and compatibility evidence.
2. Run `python3 scripts/sync_shared.py --check`, `python3 scripts/validate.py` and
   `python3 scripts/check_transcript.py --self-test`. These need only Python 3.9+.
3. In the application repository run `pnpm skills:sync`, `pnpm plugins:check` and
   `pnpm plugins:build --output /a/new/directory`. The new directory receives skills,
   both plugin repositories and ZIPs; export never overwrites an existing repository.
4. Publish a reviewed catalog commit before passing its full SHA through
   `--skills-source-commit` when exporting plugin payloads. Hash inventory pins draft
   files but is not a substitute for the public release commit.
5. Review payload-only distribution PRs, preserve manifests/endpoints, and run clean
   client install, OAuth, query, error and duplicate-install cases. Attach their
   anonymized evidence. Do not call file checks behavioral evaluation.
6. Only after live gates pass, tag a reviewed semantic version and run the read-only
   release workflow to build a downloadable catalog artifact. Publishing a release
   and directory submission remain deliberate platform operations.

Release CI never contacts properties or providers. External pull requests receive
no production credentials. Rollback is a deliberate export of the prior reviewed
commit and matching manifest version; no runtime main download is involved.
The draft is not ready for a compatibility announcement until all live gates pass.
