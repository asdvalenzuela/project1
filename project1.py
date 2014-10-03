import os
import shutil

for letter in "abcdefghijklmnopqrstuvwxyz":
    os.mkdir(letter)

file_list = os.listdir("/home/user/src/project1/files")
print file_list
for f in file_list:
    for letter in "abcdefghijklmnopqrstuvwxyz":
        if f[0] == letter:
            move_file = "files/"+f
            shutil.move(move_file,letter)


