import os

pathIn = input("paste the path to the folder: ")
path = ""

for x in pathIn:
    if x == "\\":
        path += "/"
    else:
        path += x
        
lastFileSize = 0
for file in os.listdir(path):
    if os.path.getsize(f"{path}/{file}") == lastFileSize:
        os.remove(f"{path}/{file}")
        print(f"deleted {path}/{file}")
    else:
        lastFileSize = os.path.getsize(f"{path}/{file}")

print("")
print("done")
input()