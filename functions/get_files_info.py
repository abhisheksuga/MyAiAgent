import os


def get_files_info(working_directory, directory="."):
    abs_working_dir = os.path.abspath(working_directory)
    abs_directory = os.path.abspath(os.path.join(working_directory,directory))
    
    if not abs_directory.startswith(abs_working_dir):
        return f"ERROR: '{directory}' is not a directory"
      
    final_response = ''
    contents = os.listdir(abs_directory)
    for content in contents :
        content_path = os.path.join(abs_directory,content)
        is_dir =os.path.isdir(content_path)
        is_size = os.path.getsize(content_path)
        final_response += f'- {content} : file size ={is_size} bytes , is_dir = {is_dir} \n'

    return final_response