f = open('input.txt')
lines = f.readlines()
f.close()

score1 = 0
score2 = []

matches1 = {
    ')':['(',3],
    ']':['[',57],
    '}':['{',1197],
    '>':['<',25137]
}

matches2 = {
    '(':1,
    '[':2,
    '{':3,
    '<':4
}

for line in lines:
    opened = ''
    stop = False
    for char in line:
        if char in '([{<':
            opened+=char
        elif char in ')]}>':
            if opened[-1] == matches1[char][0]:
                opened = opened[:-1]
            else:
                score1+=matches1[char][1]
                stop = True
    if not stop:
        score2.append(0)
        for char in opened[::-1]:
            score2[-1] = 5*score2[-1]+matches2[char]
score2.sort()
score2 = score2[int((len(score2)-1)/2)]
print('Part 1:', score1)
print('Part 2:', score2)