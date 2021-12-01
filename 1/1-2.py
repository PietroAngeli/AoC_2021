f = open('input.txt')
lines = f.readlines()
f.close()
intmap = map(int, lines)
lines = list(intmap)
inc = 0
for i in range(3, len(lines)):
    A=lines[i-3:i]
    B=lines[i-2:i+1]
    if sum(B)>sum(A): inc +=1
print(inc)