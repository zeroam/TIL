from pathlib import Path

cur_path = Path(".")
txt_files = cur_path.glob("*.txt")
for txt_file in txt_files:
    txt_file.unlink()
