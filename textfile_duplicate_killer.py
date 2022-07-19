filename = input("filename of the source? ")
file = open(f"{filename}", "r").readlines()
list = []
for line in file:
    if line not in list:
        list.append(line)
output = open("output.txt", "w")
for x in list:
    output.write(x)
output.close()
input("")
