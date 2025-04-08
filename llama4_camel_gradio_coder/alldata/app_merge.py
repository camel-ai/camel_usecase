#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import glob
import shutil
import tempfile
import gradio as gr
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
    
    result_files = []
    result_messages = []
    
    # Process each file type
    for file_type in file_types:
        result_messages.append(f"Processing {file_type} files...")
        output_file = os.path.join(output_dir, f"merged{file_type}")
        
        with open(output_file, 'w', encoding='utf-8') as outfile:
            # Process each source directory
            for source_dir in source_dirs:
                # Find all files of the current type in the source directory and its subdirectories
                pattern = os.path.join(source_dir, f"**/*{file_type}")
                files = glob.glob(pattern, recursive=True)
                
                # Skip if no files found
                if not files:
                    result_messages.append(f"No {file_type} files found in {source_dir}")
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
        
        result_messages.append(f"Created merged file: {output_file}")
        result_files.append(output_file)
    
    return result_files, "\n".join(result_messages)


def process_uploaded_files(uploaded_files, output_dir, file_types=None, auto_detect=True):
    """
    Process uploaded files and directories for merging.
    
    Args:
        uploaded_files (list): List of uploaded file paths
        output_dir (str): Directory to save merged files
        file_types (str): Comma-separated list of file extensions to merge
        auto_detect (bool): Whether to automatically detect file types
        
    Returns:
        tuple: (list of output files, log message)
    """
    # Create a temporary directory to store uploaded files
    with tempfile.TemporaryDirectory() as temp_dir:
        source_dirs = []
        
        # Process each uploaded file
        for file_path in uploaded_files:
            if not file_path:
                continue
                
            # Get the file name
            file_name = os.path.basename(file_path)
            
            # Check if it's a directory (zip file)
            if file_name.endswith('.zip'):
                # Extract the zip file
                import zipfile
                extract_dir = os.path.join(temp_dir, os.path.splitext(file_name)[0])
                os.makedirs(extract_dir, exist_ok=True)
                
                with zipfile.ZipFile(file_path, 'r') as zip_ref:
                    zip_ref.extractall(extract_dir)
                
                source_dirs.append(extract_dir)
            else:
                # It's a single file, create a directory for it
                file_dir = os.path.join(temp_dir, os.path.splitext(file_name)[0])
                os.makedirs(file_dir, exist_ok=True)
                
                # Copy the file to the directory
                shutil.copy2(file_path, file_dir)
                source_dirs.append(file_dir)
        
        # Validate source directories
        if not source_dirs:
            return [], "Error: No valid files or directories were uploaded."
        
        # Process file types
        file_type_list = None
        if not auto_detect and file_types:
            file_type_list = [ft.strip() for ft in file_types.split(',') if ft.strip()]
            # Ensure file types start with a dot
            file_type_list = [ft if ft.startswith('.') else f'.{ft}' for ft in file_type_list]
        
        # Perform the merge
        try:
            return merge_files(source_dirs, output_dir, file_type_list)
        except Exception as e:
            return [], f"Error during merge operation: {str(e)}"


# Create the Gradio interface
def create_interface():
    with gr.Blocks(title="File Merger Tool", theme=gr.themes.Soft()) as app:
        gr.Markdown("# 📁 File Merger Tool")
        gr.Markdown("Merge files of the same type from multiple folders or files into a single file.")
        
        with gr.Row():
            with gr.Column(scale=2):
                uploaded_files = gr.File(
                    label="Upload Files or Folders (ZIP)",
                    file_count="multiple",
                    file_types=["file", ".zip"],
                    type="filepath"
                )
                
                output_dir = gr.Textbox(
                    label="Output Directory",
                    placeholder="Enter output directory path",
                    info="Where to save the merged files"
                )
                
                with gr.Row():
                    auto_detect = gr.Checkbox(
                        label="Auto-detect file types",
                        value=True,
                        info="Automatically detect all file types in uploaded files"
                    )
                    
                    file_types = gr.Textbox(
                        label="File Types (if not auto-detecting)",
                        placeholder="Enter comma-separated list of file extensions",
                        info="Example: .py, .txt, .md",
                        visible=False
                    )
                
                merge_btn = gr.Button("Merge Files", variant="primary")
            
            with gr.Column(scale=1):
                gr.Markdown("### Instructions")
                gr.Markdown("""
                1. Upload files or folders (as ZIP files)
                2. Specify the output directory
                3. Choose whether to auto-detect file types
                4. If not auto-detecting, specify the file types to merge
                5. Click 'Merge Files' to start the process
                """)
                
                gr.Markdown("### Notes")
                gr.Markdown("""
                - For folders, please zip them first before uploading
                - The app will automatically detect file types if not specified
                - Each file type will be merged into a separate file
                """)
        
        with gr.Row():
            output_files = gr.File(
                label="Merged Files",
                file_count="multiple",
                visible=False
            )
        
        log_output = gr.Textbox(
            label="Log",
            lines=10,
            max_lines=20,
            interactive=False
        )
        
        # Show/hide file types input based on auto-detect checkbox
        def toggle_file_types(checked):
            return gr.update(visible=not checked)
        
        auto_detect.change(
            fn=toggle_file_types,
            inputs=[auto_detect],
            outputs=[file_types]
        )
        
        # Process the merge operation
        def run_merge(uploaded_files, output_dir, file_types, auto_detect):
            if not output_dir:
                return None, "Error: Output directory is required.", gr.update(visible=False)
                
            files, log = process_uploaded_files(uploaded_files, output_dir, file_types, auto_detect)
            
            if files:
                return files, log, gr.update(visible=True)
            else:
                return None, log, gr.update(visible=False)
        
        merge_btn.click(
            fn=run_merge,
            inputs=[uploaded_files, output_dir, file_types, auto_detect],
            outputs=[output_files, log_output, output_files]
        )
    
    return app


if __name__ == "__main__":
    app = create_interface()
    app.launch(share=True)
