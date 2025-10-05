import os
from google.genai import types

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
    

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Overwrites an existing file or writes a new file if it doesnt exits(and creates required parent dirs safely),constrained to the working directory ",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to write",
            ),
            "Content": types.Schema(
                type=types.Type.STRING,
                description="The contents to write to the file as a string",
            ),
        },
    ),
)
