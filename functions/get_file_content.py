import os 
from config import MAX_CHAR_COUNT

def get_file_content(working_directory, file_path="."):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory,file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f"ERROR: '{file_path}' is not a directory"
    if not os.path.isfile(abs_file_path):
        return f"ERROR: '{file_path}' is not a file"

    file_content_string = ""

    try:
        with open(abs_file_path,'r') as f :
            file_content_string = f.read(MAX_CHAR_COUNT)
            if len(file_content_string)>= MAX_CHAR_COUNT:
                file_content_string+= f'[..File " {file_path} truncated at 10000 characters]'
        return file_content_string
    
    except Exception as e :
        return f"Exception reading the file {e}"
