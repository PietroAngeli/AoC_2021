f = open('input.txt')
lines = f.readlines()
f.close()
gammavect=[]
linelen = len(lines[0].strip())
for i in range(linelen):
    gammavect.append(0)

for line in lines:
    stripped = line.strip()
    for i in range(len(stripped)):
        gammavect[i] += int(stripped[i])

gamma = 0
epsilon = 0
for val in gammavect:
    bit=round(val/len(lines))
    gamma = (gamma<<1)|bit
    epsilon = (epsilon<<1)|int(not bit)
    

#print(bin(epsilon), bin(gamma))
#print(epsilon, gamma)
print('Result 1: ', gamma*epsilon)

# Part 2
oxgen_list = lines.copy()
oxscrub_list = lines.copy()
for i in range(linelen):
    bitsum = 0
    for line in oxgen_list:
        bitsum += int(line[i])
    if bitsum/len(oxgen_list) >= 0.5:
        oxgen_bit = 1
    else:
        oxgen_bit = 0
    j=0
    while j < len(oxgen_list):
        eval_bit = int(oxgen_list[j][i])
        if eval_bit != oxgen_bit:
            oxgen_list.pop(j)
        else:
            j+=1
    if len(oxgen_list) == 1:
        oxgen=int(oxgen_list[0].strip(),2)
        print('Oxgen:',int(oxgen_list[0].strip(),2))
        break

for i in range(linelen):
    bitsum = 0
    for line in oxscrub_list:
        bitsum += int(line[i])
    if bitsum/len(oxscrub_list) >= 0.5:
        oxscrub_bit = 0
    else:
        oxscrub_bit = 1
    j=0
    while j < len(oxscrub_list):
        eval_bit = int(oxscrub_list[j][i])
        if eval_bit != oxscrub_bit:
            oxscrub_list.pop(j)
        else:
            j+=1
    if len(oxscrub_list) == 1:
        oxscrub=int(oxscrub_list[0].strip(),2)
        print('Oxscrub:',int(oxscrub_list[0].strip(),2))
        break
print('Part 2:', oxscrub*oxgen)