import os
if (not os.path.exists("this_folder")):
    os.mkdir("this_folder")

# for i in range(100):
#     os.mkdir(f"this_folder/Day{i}")

# for i in range(100):
#     os.rename(f"this_folder/Tutorial{i}",f"this_folder/Tutorial {i}")

# for i in range(100):
#     os.remove(f"this_folder/Tutorial {i}")

print(os.getcwd())