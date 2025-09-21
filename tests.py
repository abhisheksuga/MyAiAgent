from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content 
from functions.write_file import write_file



def main():
    working_dir = "calculator"

    print(write_file(working_dir ,'/temp/contenting.txt','This is the file'))
    # print (get_file_content(working_dir,'main.py'))
    # print (get_file_content(working_dir,'pkg/calculator.py'))

    # print (get_file_content(working_dir,'/bin/cat'))

    # root_contents = get_files_info(working_dir)
    # print(root_contents)
    # pkg_contents = get_files_info(working_dir ,"pkg")
    # print(pkg_contents)
    # pkg_contents = get_files_info(working_dir ,"/bin")
    # print(pkg_contents)
    # pkg_contents = get_files_info(working_dir ,"../")
    # print(pkg_contents)


main()
