f = open('input.txt')
lines = f.readlines()
f.close()
inc = 0
for i in range(1, len(lines)):
    if lines[i]>lines[i-1]: inc +=1
print(inc)