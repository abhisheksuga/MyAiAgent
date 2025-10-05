import os
import subprocess
from google.genai import types
def run_python_file(working_directory, file_path,args =[]):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory,file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f"ERROR: '{file_path}' is not a directory"
    if not file_path.endswith('.py'):
        return f'ERROR : {file_path} is not a Python file '
    
    try :
         input_args = ['python3',file_path]
         input_args.extend(args)

         output = subprocess.run(input_args,
                             cwd = abs_working_dir,
                             timeout = 30,
                             capture_output =True,
                             )
         output_string = f"""
STDOUT : {output.stdout}
STDERR : {output.stderr}
         """

         if output.stdout == ""  and output.stderr == "" :
            output_string = "No output Produced \n"

         if output.returncode != 0 :
            output_string += f"Process exited with code{output.returncode}"

         return output_string
    
    except Exception as e :
          return f'ERROR : executing Python file : {e}'
    



schema_run_python_file = types.FunctionDeclaration(
name="run_python_file",
description="Runs a file with the python3 interpreter.Takes additional CLI args as an array",
parameters=types.Schema(
    type=types.Type.OBJECT,
    properties={
        "file_path": types.Schema(
            type=types.Type.STRING,
            description="The file to run, relative to the working directory. ",
        ),
        "args" :types.Schema(
            type=types.Type.ARRAY,
            description="An optional array of strings to be used as the CLI args for a python file  ",
        ),
    },
),
)