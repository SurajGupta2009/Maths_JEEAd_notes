#!/usr/bin/env python3
"""Export ZIPs, bookmarked A4 PDFs and index.html from rendered sheets."""
import os, sys
from pathlib import Path

CH = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(CH.parent / "_engine"))
os.chdir(CH)
from build import export  # noqa: E402

if __name__ == "__main__":
    export(CH.name)
