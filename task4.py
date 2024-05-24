import os
import shutil
inp_path = input("Please enter the file path: ")
files_list = os.listdir(inp_path)
for file in files_list:
    filename, file_extension = os.path.splitext(file)
    file_extension = file_extension[1:]
    if os.path.exists(inp_path + '/' + file_extension):
        shutil.move(inp_path + '/' + file, inp_path + '/' + file_extension + '/' + file)
    else:
        os.makedirs(inp_path + '/' + file_extension)
        shutil.move(inp_path + '/' + file, inp_path + '/' + file_extension + '/' + file)
