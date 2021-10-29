file = open('notyet.txt','r')
f = file.readlines()

newList = []
for line in f:
    newList.append(line.replace(' and ', '\n'))

print(newList)

file.close