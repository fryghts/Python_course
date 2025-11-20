import os
s = input()
files = []
for file in os.listdir():
    if os.path.isfile(file) and s in file:
        files.append(file)
#files = [file for file in os.listdir() if os.path.isfile(file) and (s in file)]
print(files)
