# file renamer

# takes a directory and renames each file to fit 
# a specific naming scheme; i.e. adds a prefix 
# to file names

# Imports ---
import pathlib
import shutil

file_prefix = "myfile_"

def rename_file(file_path: pathlib.Path, dry_run=False):
    intended_path = file_path.parent / (file_prefix + file_path.name)
    print(f"{file_path.as_posix()} -> {intended_path}")
    if dry_run:
        return
    else: file_path.rename(intended_path)


def main(dir_path : str, dry_run=False):
    directory = pathlib.Path(dir_path)
    if directory.is_dir():
        for path in directory.iterdir():
            rename_file(path, dry_run=dry_run)

main("./junk_drawer", dry_run=False)