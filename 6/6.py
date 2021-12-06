f = open('input.txt')
lines = f.readlines()
f.close()
start = [int(i) for i in lines[0].strip().split(',')]
print(start)
population=[start]

time=256
day = 0
while day < time:
    newfish = 0
    population.append([])
    for fish in population[-2]:
        if fish == 0:
            population[-1].append(6)
            newfish += 1
        if fish > 0:
            population[-1].append(fish-1)
    for i in range(newfish):
        population[-1].append(8)
    print('Day', day, ': ', len(population[-1]))
    day+=1
print('Part 1:', len(population[-1]))