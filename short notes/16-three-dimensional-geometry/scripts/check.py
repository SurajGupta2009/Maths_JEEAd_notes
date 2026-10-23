#!/usr/bin/env python3
"""Run the reproducible delivery checks for this chapter."""
import os, sys
from pathlib import Path

CH = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(CH.parent / "_engine"))
os.chdir(CH)
import checks  # noqa: E402

if __name__ == "__main__":
    checks.main()
