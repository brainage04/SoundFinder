import os
import re
import shutil

# object indexing file path
dirname = os.path.dirname(__file__)
json = os.path.join(dirname, '1.8.json')
d = open(json).read()

print("Enter the name or path of sounds you would like to locate:")
input_string = input()

# copies all files based on regex string to "desired_objects" along with a list of all files and hash information in "matches.txt"
regex_string = input_string + "\/(.*?)\.ogg\": {\"hash\": \"((.{2}).*?)\""

# create destination folder if it does not exist
def check_folder(folder: str):
    if not os.path.exists(folder):
        os.makedirs(folder)

input_folder = os.path.join(dirname, f"results/{input_string}")
check_folder(input_folder)

# main logic
# find all matches
matches = re.findall(regex_string, d)

matches_temp = []

for match in matches:
    # create array for current file to store later for reference
    match_temp = [match[0], match[2], match[1]]
    matches_temp.append(match_temp)

    # init source/destination folders, check destination folder and copy file from objects folder to destination folder
    source = os.path.join(dirname, f"objects/{match_temp[1]}/{match_temp[2]}")

    destination = os.path.join(input_folder, match_temp[0])
    check_folder(destination)

    shutil.copy(source, destination)

# open file, store arrays for referencing and close file
matches_file = open(os.path.join(input_folder, "matches.txt"), "w")

for match in matches_temp:
    matches_file.write(f"{match}\n")

matches_file.close()