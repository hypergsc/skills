"""Materialize shared policy into each independently installable skill."""

import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def sync(root=ROOT, check=False):
    for skill in sorted((root / "skills").iterdir()):
        if not skill.is_dir():
            continue
        for source in sorted((root / "shared-source").glob("*.md")):
            target = skill / "references" / source.name
            if check:
                if not target.is_file() or target.read_bytes() != source.read_bytes():
                    raise ValueError(f"Stale shared reference: {target}")
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(source.read_bytes())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    sync(check=parser.parse_args().check)
