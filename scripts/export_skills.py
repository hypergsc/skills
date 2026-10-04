"""Copy a reviewed, complete skill payload and record deterministic provenance."""

import argparse
import hashlib
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def inventory(root):
    if root.is_symlink():
        raise ValueError(f"Refusing symlink: {root}")
    files = {}
    for path in sorted(root.rglob("*")):
        if path.is_symlink():
            raise ValueError(f"Refusing symlink: {path}")
        if path.is_file():
            files[path.relative_to(root).as_posix()] = hashlib.sha256(
                path.read_bytes()
            ).hexdigest()
    return files


def export(destination, root=ROOT, source_commit=None):
    from validate import validate

    validate(root)
    if source_commit is not None and (
        len(source_commit) != 40
        or any(c not in "0123456789abcdef" for c in source_commit)
    ):
        raise ValueError("Expected full canonical catalog commit")
    if destination.exists():
        raise ValueError(f"Refusing to overwrite skill payload: {destination}")
    shutil.copytree(root / "skills", destination)
    catalog = json.loads((root / "catalog.json").read_text())
    provenance = {
        "repository": "https://github.com/hypergsc/skills",
        "version": catalog["version"],
        "source_commit": source_commit,
        "commit_status": "recorded" if source_commit else "unpublished local payload",
        "files": inventory(destination),
    }
    (destination.parent / "skills-source.json").write_text(
        json.dumps(provenance, indent=2) + "\n"
    )
    return provenance


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination", type=Path)
    parser.add_argument(
        "--source-commit", help="Reviewed commit of the public canonical repository"
    )
    args = parser.parse_args()
    if args.source_commit and (
        len(args.source_commit) != 40
        or any(c not in "0123456789abcdef" for c in args.source_commit)
    ):
        parser.error("source commit must be a full lowercase Git SHA")
    export(args.destination, source_commit=args.source_commit)
