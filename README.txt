Archive Extractor

The Archive Extractor is a Python script designed to extract archive files from a given directory. It supports extracting files from .tgz archives and moving them to the current directory. Additionally, it can extract files based on the year they were created.

Requirements

Python 3.x
7-Zip installed and added to the system path
Usage

To use the Archive Extractor, follow these steps:

Clone or download the repository to your local machine.
Ensure Python 3.x is installed on your system.
Install the required Python packages using pip:

pip install -r requirements.txt

Install 7-Zip and add it to the system path if it's not already installed.
Run the script using Python:

python ch_ex.py [-h] [-a] [-y YEAR] path
Command-line Arguments

path: Path to the directory containing archive files.
-a, --all: Extract all files from archive files in the specified directory.
-y YEAR, --year YEAR: Extract files from archive files created in the specified year.
Example Usage

Extract all files from archive files in the current directory:

python ch_ex.py /path/to/directory -a
Extract files from archive files created in the year 2023:

python ch_ex.py /path/to/directory -y 2023
Notes

If 7-Zip is installed in a different location than the default ("C:\Program Files\7-Zip\7z.exe"), please update the path_7z variable in the script accordingly.