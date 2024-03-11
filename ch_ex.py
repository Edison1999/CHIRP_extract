import datetime
from pathlib import Path
import os
import subprocess
import shutil
import argparse

def extract_files(file_path):
    path_7z= r'"C:\Program Files\7-Zip\7z.exe"'
    command =  '{1} x {0} -so | {1} x -aoa -si -ttar -o{2}'.format(file_path, path_7z, os.path.dirname(file_path))
    subprocess.run(command, shell=True, check=True)

def move_files_to_curr_dir(root_dir, sub_dir):
    upper_dir = os.path.join(root_dir, sub_dir)
    src_files = os.listdir(upper_dir)
    for file_name in src_files:
        full_file_name = os.path.join(upper_dir, file_name)
        if os.path.isfile(full_file_name) and full_file_name.endswith('.fits'):
            shutil.copy(full_file_name, root_dir)
    shutil.rmtree(upper_dir)

def search_tgz_files(dir_path):
    for root, _, files in os.walk(dir_path):
        for file in files:
            if file.endswith('.tgz'):
                ex_files = os.path.join(root, file)
                try:
                    extract_files(ex_files)
                    move_files_to_curr_dir(root, Path(file).stem)
                except Exception:
                    print("Unable to extract files for {0}".format(ex_files))

# Function to list directories
def list_dirs(dir_path, year = None):
    for item in os.listdir(dir_path):
        item_path = os.path.join(dir_path, item)
        if os.path.isdir(item_path):
            if year and year[len(year)-2: len(year)] == item[0:2]:
                search_tgz_files(item_path)
            elif year == None:
                search_tgz_files(item_path)
                        
def valid_year(year):
    try:
        year = int(year)
        current_year = datetime.datetime.now().year
        if year < 1970 or year > current_year:
            raise argparse.ArgumentTypeError("Invalid year")
        return year
    except ValueError:
        raise argparse.ArgumentTypeError("Invalid year")

def valid_path(path):
    try:
        if not os.path.exists(path):
            raise argparse.ArgumentTypeError("Invalid path")
        return path
    except ValueError:
        raise argparse.ArgumentTypeError("Invalid path")

def main():
    parser = argparse.ArgumentParser(description="Extract archive files from a given directory.")
    parser.add_argument("path", type=valid_path, help="Path to the directory")
    parser.add_argument("-a", "--all", action="store_true", help="Extract all files.")
    parser.add_argument("-y", "--year", type=valid_year ,help="Extract files by year. Need to be an int.")
    args = parser.parse_args()

    if args.all:
        list_dirs(args.path)
    elif args.year:

        list_dirs(args.path, str(args.year))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()