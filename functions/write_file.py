import os


def write_file (working_directory,file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory,file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'ERROR :"{file_path}" not in the working directory'
    
    parent_dir = os.path.dirname(abs_file_path)
    if not os.path.dirname(parent_dir) :
        try:
            os.makedirs(parent_dir)
        except Exception as e :
            return f"Could not create parent dirs :{parent_dir} = {e}"

    try :    
        with open(abs_file_path,"w") as f :
            f.write(content)
            return f' Successfully written to "{abs_file_path}"({len(content)} characters written)'
        
    except Exception as e :
        return f"failed to write to file : {abs_file_path} , {e}"
    


