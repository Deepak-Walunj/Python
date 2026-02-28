# import os

# def rename(dir,file,old_path,type):
#     try:
#         new_path=os.path.join(dir,f"{len(os.listdir(dir))+1}{type}")
#         os.rename(old_path,new_path)
#     except FileNotFoundError:
#         print(f"File {file} dosent exist")
#     except PermissionError:
#         print(f"Access denied to rename the file {file}")
#     except OSError as e:
#         print(f"Error renaming file {file}:{e}")


# def create_dir(dir):
#     try:
#         if not os.path.exists(dir):
#             os.makedirs(dir)
#     except OSError as e:
#         print(f"Error:{e}")

# def changefilename(dir):
#     try:
#         pdf_dir=os.path.join(dir,"PDF")
#         png_dir=os.path.join(dir,"PNG")
#         docx_dir=os.path.join(dir,"DOCX")
#         jpeg_dir=os.path.join(dir,"JPEG")
#         jpg_dir=os.path.join(dir,"JPG")
#         xlsx_dir=os.path.join(dir,"XLSX")
        
#         create_dir(pdf_dir)
#         create_dir(png_dir)
#         create_dir(jpeg_dir)
#         create_dir(jpg_dir)
#         create_dir(xlsx_dir)
#         create_dir(docx_dir)

#     except FileNotFoundError:
#         print(f"The directory {dir} doesnt exists")
#         return
#     except PermissionError:
#         print(f"Access denied for directory {dir}")
#         return
#     files=os.listdir(dir)

#     for file in files:
#         old_path=os.path.join(dir,file)
#         if file.endswith(".png"):
#             rename(png_dir,file,old_path,".png")
#         elif file.endswith(".jpg"):
#             rename(jpg_dir,file,old_path,".jpg")            
#         elif file.endswith(".xlsx"):
#             rename(xlsx_dir,file,old_path,".xlsx")            
#         elif file.endswith(".docx"):
#             rename(docx_dir,file,old_path,".docx")        
#         elif file.endswith(".png"):
#             rename(jpeg_dir,file,old_path,".jpeg")
#         elif file.endswith(".pdf"):
#             rename(pdf_dir,file,old_path,".pdf")            
    
# d="C:/Users/Deepak/OneDrive/Desktop/Python/PROJECTS/Project_6"
# changefilename(d)

import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_directory(path):
    """
    Create a directory if it doesn't exist.
    
    :param path: Directory path to create
    """
    try:
        os.makedirs(path, exist_ok=True)
        logging.info(f"Directory created: {path}")
    except OSError as e:
        logging.error(f"Error creating directory {path}: {e}")

def rename_and_move_file(old_path, new_dir, extension):
    """
    Rename and move a file to a new directory with a sequential name.
    
    :param old_path: Original file path
    :param new_dir: Target directory for the file
    :param extension: File extension for the new file
    """
    try:
        # Count existing files in the directory and generate new file name
        new_file_name = f"{len(os.listdir(new_dir)) + 1}{extension}"
        new_path = os.path.join(new_dir, new_file_name)
        os.rename(old_path, new_path)
        logging.info(f"Moved and renamed file {old_path} to {new_path}")
    except FileNotFoundError:
        logging.error(f"File {old_path} doesn't exist")
    except PermissionError:
        logging.error(f"Access denied to rename the file {old_path}")
    except OSError as e:
        logging.error(f"Error renaming file {old_path}: {e}")

def organize_files(base_dir):
    """
    Organize files in the base directory into subdirectories by file type
    and rename them sequentially.
    
    :param base_dir: The base directory containing the files to organize
    """
    # Define target directories for each file type
    target_dirs = {
        ".pdf": os.path.join(base_dir, "PDF"),
        ".png": os.path.join(base_dir, "PNG"),
        ".jpeg": os.path.join(base_dir, "JPEG"),
        ".jpg": os.path.join(base_dir, "JPG"),
        ".xlsx": os.path.join(base_dir, "XLSX"),
        ".docx": os.path.join(base_dir, "DOCX"),
        ".xls": os.path.join(base_dir, "XLS"),
    }

    # Create target directories if they don't exist
    for dir_path in target_dirs.values():
        create_directory(dir_path)

    # Iterate through files in the base directory
    for file_name in os.listdir(base_dir):
        old_path = os.path.join(base_dir, file_name)
        # Skip directories
        if os.path.isdir(old_path):
            continue
        # Get file extension
        _, ext = os.path.splitext(file_name)
        # Move and rename the file if the extension is recognized
        if ext in target_dirs:
            rename_and_move_file(old_path, target_dirs[ext], ext)

if __name__ == "__main__":
    base_directory = "C:/Users/Deepak/OneDrive/Desktop/Python/PROJECTS/Project_6"
    organize_files(base_directory)
