import os
from pathlib import Path
import sys
try:
    project_path = Path(sys._MEIPASS)
except Exception:
    project_path = (Path(__file__).parents[1])

print(project_path.joinpath("example_batch.txt"))