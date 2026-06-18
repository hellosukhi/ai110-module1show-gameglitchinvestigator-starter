import sys
from pathlib import Path

# FIX: Added test path setup for local imports;
# ensures pytest can import the project modules reliably from the repository root.
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
