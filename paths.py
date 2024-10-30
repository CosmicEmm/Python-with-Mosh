from pathlib import Path
path = Path("ecommerce")
# check if a path exists or not
print(path.exists())
# we can also make a new directory
path = Path("webdev")
# path.mkdir()
# we can also remove a directory
path_2 = Path("web_dev")
# path_2.rmdir()

#we can also access all the files and directories in a given path and iterate over them
path3 = Path()
for item in path3.glob("*"): # "*" refers to all files and directories in a path
    print(item)
print("\n")
path4 = Path()
for file in path4.glob("*.*"): # "*.*" refers to only the files in a path
    print(file)
print("\n")
path5 = Path()
for py_files in path5.glob("*.py"): # "*.py" refers to the Python files in a path
    print(py_files)
