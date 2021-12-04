f = open('input.txt')
lines = f.readlines()
f.close()

picklist = lines[0].strip().split(',')
picklist = [int(x) for x in picklist]
#print(picklist)
lines.pop(0)

sheets=[]
for line in lines:
    line = line.strip()
    if line == '':
        sheets.append([[],0])
    else:
        row = [[int(i),0] for i in line.split(' ') if i]
        sheets[-1][0].append(row)

finalpick = 0
winsheet = []
for pick in picklist:
    for sheet in sheets:
        for x in range(len(sheet[0][0])):
            colscore=0
            for y in range(len(sheet[0])):
                if sheet[0][y][x][0] == pick:
                    sheet[0][y][x] = [sheet[0][y][x][0],1]
                if sheet[0][y][x][1] == 1:
                    colscore += 1
            if sheet[1] == 0:
                if colscore == len(sheet[0]):
                    winsheet.append(sheet[0])
                    sheet[1] = 1
                    finalpick = pick
        if sheet[1] == 0:      
            for row in sheet[0]:
                rowscore = 0
                for num in row:
                    rowscore += num[1]
                if rowscore == len(row):
                    winsheet.append(sheet[0])
                    sheet[1] = 1
                    finalpick = pick
    lastwin = True
    for sheet in sheets:
        if sheet[1] == 0:
            lastwin = False
    if lastwin == True:
        break
    
score=0
for x in range(len(winsheet[-1][0])):
    for y in range(len(winsheet[-1])):
        if winsheet[-1][y][x][1] == 0:
            score += winsheet[-1][y][x][0]
score *= finalpick
print('Final pick:', finalpick,'\nWinning sheet:', winsheet[-1], '\nScore:', score)