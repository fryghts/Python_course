import os
all_files = []
for cur, dirs, files in os.walk(r'C:\Users\Администратор\Desktop\Python_course'):
    all_files += [os.path.join(cur,file) for file in files if file.endswith('.py')]

print(all_files)

