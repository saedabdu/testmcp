#!/usr/bin/env python3

import os
import argparse
from pathlib import Path

def list_files(directory='.', recursive=False):
    """
    List all files in the specified directory.
    
    Args:
        directory (str): The directory to list files from
        recursive (bool): Whether to list files recursively
    """
    try:
        # Convert to absolute path
        directory = os.path.abspath(directory)
        
        # Check if directory exists
        if not os.path.exists(directory):
            print(f"Error: Directory '{directory}' does not exist")
            return
        
        # Print header
        print(f"\nListing files in: {directory}\n")
        
        if recursive:
            # Recursive listing using Path
            for path in Path(directory).rglob('*'):
                if path.is_file():
                    print(f"- {path.relative_to(directory)}")
        else:
            # Non-recursive listing
            for item in os.listdir(directory):
                item_path = os.path.join(directory, item)
                if os.path.isfile(item_path):
                    print(f"- {item}")
                    
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='List files in a directory')
    parser.add_argument('-d', '--directory', 
                       default='.',
                       help='Directory to list files from (default: current directory)')
    parser.add_argument('-r', '--recursive',
                       action='store_true',
                       help='List files recursively')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Call list_files function
    list_files(args.directory, args.recursive)

if __name__ == '__main__':
    main()