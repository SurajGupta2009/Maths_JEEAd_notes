#!/usr/bin/env python3
"""Render all content/*.md sheets to JEE/ and Olympiad/ PNGs."""
import os, sys
from pathlib import Path

CH = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(CH.parent / "_engine"))
os.chdir(CH)
from build import render  # noqa: E402

if __name__ == "__main__":
    render(CH.name)
