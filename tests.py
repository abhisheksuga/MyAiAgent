# from functions.get_files_info import get_files_info
# from functions.get_file_content import get_file_content 
# from functions.write_file import write_file
from functions.run_python_file import run_python_file as execute_code



def main():
    working_dir = "calculator"
    print(execute_code(working_dir,"main.py" , ["3 + 5"] ))




main()
