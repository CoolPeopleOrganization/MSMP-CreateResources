import re
import sys
from pathlib import Path


def increment_version(pack_path: Path) -> None:
    if not pack_path.is_file():
        print(f"ERROR: File not found: {pack_path}")
        sys.exit(1)

    content = pack_path.read_text(encoding="utf-8")

    pattern = r'^version\s*=\s*"(\d+)\.(\d+)\.(\d+)"\s*$'

    match = re.search(pattern, content, re.MULTILINE)

    if not match:
        print("ERROR: Could not find a valid version field (e.g. version = \"1.1.0\").")
        sys.exit(1)

    major, minor, patch = map(int, match.groups())
    new_version = f"{major}.{minor}.{patch + 1}"
    updated_content = content[:match.start(1)] + new_version + content[match.end(3):]

    pack_path.write_text(updated_content, encoding="utf-8")

    print(f"version incremented: {major}.{minor}.{patch} -> {new_version}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)

    increment_version(Path(sys.argv[1]))