# File Listing Utility

A simple Python utility to list files in a directory.

## Features

- List files in a specified directory
- Optional recursive listing
- Clean and formatted output
- Error handling for invalid directories

## Usage

```bash
# List files in current directory
python list_files.py

# List files in a specific directory
python list_files.py -d /path/to/directory

# List files recursively
python list_files.py -r

# List files recursively in a specific directory
python list_files.py -d /path/to/directory -r
```

## Arguments

- `-d, --directory`: Specify the directory to list files from (default: current directory)
- `-r, --recursive`: Enable recursive file listing