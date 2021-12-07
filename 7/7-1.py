f = open('input.txt')
lines = f.readlines()
f.close()
positions = [int(i) for i in lines[0].strip().split(',')]
minpos = min(positions)
maxpos=max(positions)
fuel = []
for val in range(minpos,maxpos+1):
    fuel.append(0)
    for pos in positions:
        fuel[-1]+=abs(pos-val)
print(min(fuel))