import os
import shutil

ROOT = os.path.dirname(__file__)
SRC = os.path.join(ROOT, 'solar_power_output.csv')
DEST_DIR = os.path.join(ROOT, 'dataset')
DEST = os.path.join(DEST_DIR, 'solar_power_output.csv')

if not os.path.exists(SRC):
    print(f"Source file not found: {SRC}")
    raise SystemExit(1)

os.makedirs(DEST_DIR, exist_ok=True)

if os.path.exists(DEST):
    print(f"Destination already exists: {DEST}")
else:
    shutil.copy2(SRC, DEST)
    print(f"Copied {SRC} -> {DEST}")
