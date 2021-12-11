f = open('input.txt')
lines = f.readlines()
f.close()

gridwidth = len(lines[0].strip())
gridheight = len(lines)

class Octo:
    def __init__(self, energy):
        self.energy = energy
        self.charged = False
    def flash(self):
        if self.charged == True:
            self.energy = 0
            self.charged = False
            return(1)
        else:
            return(0)

def checkright(i,j,grid):
    grid[i+1,j].energy += 1
    #print('Octo in ', [i+1,j], 'has now energy', grid[i+1,j].energy)
    return(grid)

def checkleft(i,j,grid):
    grid[i-1,j].energy += 1
    #print('Octo in ', [i-1,j], 'has now energy', grid[i-1,j].energy)
    return(grid)

def checkup(i,j,grid):
    grid[i,j-1].energy += 1
    #print('Octo in ', [i,j-1], 'has now energy', grid[i,j-1].energy)
    return(grid)

def checkdown(i,j,grid):
    grid[i,j+1].energy +=1
    #print('Octo in ', [i,j+1], 'has now energy', grid[i,j+1].energy)
    return(grid)

def checkcorners(i,j,grid):
    if i>0 and j>0:
        grid[i-1,j-1].energy +=1
    if i>0 and j<gridheight-1:
        grid[i-1,j+1].energy+=1
    if i<gridwidth-1 and j<gridheight-1:
        grid[i+1,j+1].energy+=1
    if i<gridwidth-1 and j>0:
        grid[i+1,j-1].energy+=1
    return(grid)

def propagateflash(point, grid):
    i = point[0]
    j = point[1]
    grid = checkcorners(i,j,grid)
    if j > 0:
        grid = checkup(i, j, grid)
    if i > 0:
        grid = checkleft(i, j, grid)   
    if i < gridwidth-1:
        grid = checkright(i, j, grid)   
    if j < gridheight-1:
        grid = checkdown(i, j, grid)  
    
    return(grid)

octogrid = {}
y = 0
for line in lines:
    octorow = line.strip()
    x = 0
    for octoval in octorow:
        octogrid[x,y] = Octo(int(octoval))
        x += 1
    y += 1

steps = 100
flashes = 0
for step in range(steps):
    '''
    for j in range(gridheight):
        for i in range(gridwidth):
            print(octogrid[i,j].energy, end='')
        print('')
    print('')
    '''
    # Increase all octos energy by 1
    for point in octogrid:
        octogrid[point].energy += 1
    
    # check who flashes, propagate
    check = True
    while check:
        for point in octogrid:
            check = False
            if octogrid[point].energy > 9 and octogrid[point].charged == False:
                octogrid[point].charged = True
                #print('Charged:', point)
                octogrid = propagateflash(point, octogrid)
        for point in octogrid:
            if octogrid[point].energy > 9 and octogrid[point].charged == False:
                check = True
    
    for point in octogrid:
        flashes+=octogrid[point].flash()   

print('Part 1:', flashes)
