import json
from pathlib import Path

__all__ = [
    "load_manifest"
]


def load_manifest():
    root_dir = Path(__file__).parent.parent
    with open(f"{root_dir}/manifest.json") as f:
        manifest = json.load(f)
    return manifest
