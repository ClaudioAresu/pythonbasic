file = open('change.txt', 'r')
f = file.readlines()

newList = []
for line in f:
    newList.append(line.strip())
print(newList)

file.close