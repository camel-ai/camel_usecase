#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import argparse
import glob
from pathlib import Path
from collections import defaultdict


def find_file_types(source_dirs):
    """
    Find all file types in the source directories.
    
    Args:
        source_dirs (list): List of source directories to search for files
        
    Returns:
        set: Set of file extensions found in the source directories
    """
    file_types = set()
    
    for source_dir in source_dirs:
        # Find all files in the source directory and its subdirectories
        for root, _, files in os.walk(source_dir):
            for file in files:
                # Get the file extension
                _, ext = os.path.splitext(file)
                if ext:  # Only add non-empty extensions
                    file_types.add(ext.lower())
    
    return file_types


def merge_files(source_dirs, output_dir, file_types=None):
    """
    Merge files of the same type from multiple source directories into a single file.
    
    Args:
        source_dirs (list): List of source directories to search for files
        output_dir (str): Directory to save merged files
        file_types (list): List of file extensions to merge (e.g., ['.py', '.txt'])
                           If None, all file types found in source_dirs will be merged
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # If file_types is not provided, find all file types in the source directories
    if file_types is None:
        file_types = find_file_types(source_dirs)
        print(f"Automatically detected file types: {', '.join(sorted(file_types))}")
    
    # Process each file type
    for file_type in file_types:
        print(f"Processing {file_type} files...")
        output_file = os.path.join(output_dir, f"merged{file_type}")
        
        with open(output_file, 'w', encoding='utf-8') as outfile:
            # Process each source directory
            for source_dir in source_dirs:
                # Find all files of the current type in the source directory and its subdirectories
                pattern = os.path.join(source_dir, f"**/*{file_type}")
                files = glob.glob(pattern, recursive=True)
                
                # Skip if no files found
                if not files:
                    print(f"No {file_type} files found in {source_dir}")
                    continue
                
                # Write a header for this source directory
                outfile.write(f"\n{'='*80}\n")
                outfile.write(f"# Files from: {source_dir}\n")
                outfile.write(f"{'='*80}\n\n")
                
                # Process each file in the current source directory
                for file_path in sorted(files):
                    file_name = os.path.basename(file_path)
                    relative_path = os.path.relpath(file_path, source_dir)
                    
                    # Write a header for this file
                    outfile.write(f"\n{'-'*80}\n")
                    outfile.write(f"# File: {relative_path}\n")
                    outfile.write(f"{'-'*80}\n\n")
                    
                    # Read and write the content of the file
                    try:
                        with open(file_path, 'r', encoding='utf-8') as infile:
                            content = infile.read()
                            outfile.write(content)
                            outfile.write("\n\n")
                    except Exception as e:
                        outfile.write(f"# Error reading file {relative_path}: {str(e)}\n\n")
        
        print(f"Created merged file: {output_file}")


def main():
    parser = argparse.ArgumentParser(description='Merge files of the same type from multiple directories')
    parser.add_argument('--source-dirs', nargs='+', required=True, help='Source directories to search for files')
    parser.add_argument('--output-dir', required=True, help='Directory to save merged files')
    parser.add_argument('--file-types', nargs='+', default=None, 
                        help='File extensions to merge (default: automatically detect all file types)')
    
    args = parser.parse_args()
    
    # Ensure file types start with a dot if provided
    file_types = None
    if args.file_types:
        file_types = [ft if ft.startswith('.') else f'.{ft}' for ft in args.file_types]
    
    merge_files(args.source_dirs, args.output_dir, file_types)
    print("Merge completed successfully!")


if __name__ == "__main__":
    main()
