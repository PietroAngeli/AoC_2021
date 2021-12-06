f = open('input.txt')
lines = f.readlines()
f.close()
start = [int(i) for i in lines[0].strip().split(',')]
print(start)
#population=[start]
population=[[0,0,0,0,0,0,0,0,0]]
for fish in start:
    population[0][fish]+=1
print('Start population:', population[-1])
time=256
day = 0
while day < time:
    population.append([0,0,0,0,0,0,0,0,0])
    for i in range(6):
        population[-1][i] = population[-2][i+1]  
    population[-1][6] = population[-2][0]+population[-2][7]
    population[-1][7] = population[-2][8]
    population[-1][8] = population[-2][0]
    day+=1
    #print('Day ', day, ': ', population[-1])
tot = 0
for val in population[-1]:
    tot+=val

print('Final population: ',tot)