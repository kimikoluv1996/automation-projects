from pathlib import Path

test_dir = Path("/home/joey/Downloads")

exts = {"images": ['.jpg', '.png', '.webp'], "archives": ['.zip', '.gz', '.7z'],
        "misc": ['.pdf', '.nes', '.exe', '.txt']}

def del_empty_dirs(dir: Path, dry_run=True) -> None:
    #if dir.exists(): print("file exists")
    if dir.is_dir():
        if not any(dir.iterdir()):
            print(f"{dir.name} is empty, deleting.")
            if not dry_run:
                dir.rmdir()

def clean_filename(file: Path, dry_run=True) -> None:
    """make a file name more readable by making everything lowercase 
       and removing junk like spaces"""
    new_name = file.stem.replace(" ", "-").lower() + file.suffix
    print(f"{file.name} will become -> {new_name}")
    if not dry_run:
        file.rename(new_name)

def sort_f(file: Path, dry_run=True) -> None:
    if file.is_file():
        for key in exts.keys():
            if file.suffix in exts.get(key):
                print(f"{file.name} is in {key}")
                Path(f"./{key}").mkdir()
                print(f"making directory {key} and moving {file.name}")
                
def clean(dir: str, dry_run=True) -> None:
    dirpath = Path(dir)
    if dirpath.is_dir():
        for file in dirpath.iterdir():
            clean_filename(file, dry_run=dry_run)
            del_empty_dirs(file, dry_run=dry_run)
            sort_f(file, dry_run=dry_run)
    else: print(f"{dirpath.name} is not a directory.")

#clean("/home/joey/Downloads")