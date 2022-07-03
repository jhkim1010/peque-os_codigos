import glob

path = "./*/*.py"
file_list = glob.glob(path)
file_list_py = [file for file in file_list]
# file_list_py = [file for file in file_list if file.endswith(".py")]

for file in file_list_py:
    print(file)
#print ("file_list_py: {}".format(file_list_py))