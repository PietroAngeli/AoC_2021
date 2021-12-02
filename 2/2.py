f = open('input.txt')
lines = f.readlines()
f.close()
fwd = 0
depth = 0
# Part 1
for line in lines:
    command = line.split(" ")
    command[-1] = int(command[-1])
    if command[0] == "forward":
        fwd+=command[1]
    elif command[0] == "up":
        depth-=command[1]
    elif command[0] == "down":
        depth+=command[1]
    else:
        print("not recognised")
print("Part 1:", fwd*depth)

#Part 2
aim = 0
fwd = 0
depth = 0
for line in lines:
    command = line.split(" ")
    command[-1] = int(command[-1])
    if command[0] == "forward":
        fwd+=command[1]
        depth+=aim*command[1]
    elif command[0] == "up":
        aim-=command[1]
    elif command[0] == "down":
        aim+=command[1]
    else:
        print("not recognised")
print("Part 2:", fwd*depth)