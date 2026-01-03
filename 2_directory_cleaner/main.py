# Directory Cleaner
"""
    "Cleans up" a given directory by sorting files 
    into subdirectories by extension, renaming files,
    and deleting empty subdirs
"""
# Usage: main.py [--dry-run] /path/to/directory 

# Imports
from pathlib import Path
import sys

# Global Vars
exts = {"images": ['.jpg', '.png', '.webp'], "archives": ['.zip', '.gz', '.7z'],
        "misc": ['.pdf', '.nes', '.exe', '.txt']}

# Helper Functions
def del_empty_dirs(dir: Path, dry_run=True) -> None:
    #if dir.exists(): print("file exists")
    if dir.is_dir():
        if not any(dir.iterdir()):
            print(f"{dir.name} is empty, deleting.")
            if not dry_run:
                dir.rmdir()

def cleaned_name(file_name: str) -> any:
    """make a file name more readable by making everything lowercase 
       and removing junk like spaces"""
    file = Path(file_name).resolve()
    new_name = file.parent.resolve() / (file.stem.replace(" ", "-").lower() + file.suffix.lower())
    print(f"{file.as_posix()} will become -> {new_name}")
    return new_name

def sort_f(file: Path, dry_run=True) -> Path:
    if file.exists():
        for key in exts.keys():
            if file.suffix in exts.get(key):
                print(f"{file.as_posix()} will be moved to -> {key}")
                if not dry_run:
                    Path(f"{file.parent}/{key}").mkdir(exist_ok=True)
                    print(f"making directory {key} and moving {file.name}")
                    file.rename(f"test_dir/{key}/{file.name}")

# Main Function                
def clean(dir: str, dry_run=True) -> None:
    dirpath = Path(dir)
    if dirpath.is_dir():
        for file in dirpath.iterdir():
            new_filename = cleaned_name(file.as_posix())
            file.rename(new_filename)
            file_updated = Path(new_filename)
            sort_f(file_updated, dry_run=dry_run)
            #del_empty_dirs(file, dry_run=dry_run)
            
    else: print(f"{dirpath.name} is not a directory.")

if __name__ == "__main__":
    clean(Path(sys.argv[1]), dry_run=False)