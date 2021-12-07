f = open('input.txt')
lines = f.readlines()
f.close()
positions = [int(i) for i in lines[0].strip().split(',')]
minpos = min(positions)
maxpos=max(positions)
fuel = 0
for val in range(minpos,maxpos+1):    
    newfuel = 0
    for pos in positions:
        newfuel+=(abs(val-pos)*(abs(val-pos)+1)//2)
    if (newfuel < fuel) or (fuel == 0):
        fuel = newfuel
print(fuel)