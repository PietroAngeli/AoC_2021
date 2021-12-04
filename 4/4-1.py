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
        sheets.append([])
    else:
        row = [int(i) for i in line.split(' ') if i]
        sheets[-1].append([])
        for num in row:
            sheets[-1][-1].append([num, 0])

finalpick = 0
winsheet = []
for pick in picklist:
    for sheet in sheets:
        for x in range(len(sheet[0])):
            colscore=0
            for y in range(len(sheet)):
                if sheet[y][x][0] == pick:
                    sheet[y][x] = [sheet[y][x][0],1]
                if sheet[y][x][1] == 1:
                    colscore += 1
            if colscore == len(sheet):
                winsheet = sheet
                finalpick = pick
                break
        for raw in sheet:
            rawscore = 0
            for num in raw:
                rawscore += num[1]
            if rawscore == len(raw):
                winsheet = sheet
                finalpick = pick
                break
    if finalpick != 0:
        break

score=0
for x in range(len(winsheet[0])):
    for y in range(len(winsheet)):
        if winsheet[y][x][1] == 0:
            score += winsheet[y][x][0]
score *= finalpick
print('Final pick:', finalpick,'\nWinning sheet:', winsheet, '\nScore:', score)