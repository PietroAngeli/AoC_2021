f = open('input.txt')
lines = f.readlines()
f.close()
digitlist=[]
outputlist=[]
for line in lines:
    parsed = line.strip().split(' | ')
    digitlist.append(parsed[0].split(' '))
    outputlist.append(parsed[1].split(' '))
for i in range(len(digitlist)):
    for j in range(len(digitlist[i])):
        digitlist[i][j] = ''.join(sorted(digitlist[i][j]))
for i in range(len(outputlist)):
    for j in range(len(outputlist[i])):
        outputlist[i][j] = ''.join(sorted(outputlist[i][j]))
count = 0
for output in outputlist:
    for num in output:
        if len(num) in [2,3,4,7]:
            count+=1
print('Part 1:', count)

ord_digs = []
for digits in digitlist:
    ord_digs.append(['','','','','','','','','',''])
    print('Working on new line...')
    while '' in ord_digs[-1]:
        print('New round!')
        for digit in digits:
            print('Found:', ord_digs[-1])
            print('Evaluating ', digit)
            if digit in ord_digs: break
            #Find 1 
            if len(digit) == 2 and not ord_digs[-1][1]:
                ord_digs[-1][1] = digit
                print('1 found!')
            #Find 7
            elif len(digit) == 3 and not ord_digs[-1][7]:
                ord_digs[-1][7] = digit
                print('7 found!')
            #Find 4
            elif len(digit) == 4 and not ord_digs[-1][4]:
                ord_digs[-1][4] = digit
                print('4 found!')
            #Find 8
            elif len(digit) == 7 and not ord_digs[-1][8]:
                ord_digs[-1][8] = digit
                print('8 found!')
            #Find 3, having already found 1 is required
            elif ord_digs[-1][1] and not ord_digs[-1][3]:
                if len(digit) == 5 and ord_digs[-1][1][0] in digit and ord_digs[-1][1][1] in digit:
                    ord_digs[-1][3] = digit
                    print('3 found!')
            #To find 2 and 5 having found 1, 3 and 4 is required
            elif (not ord_digs[-1][2]) or (not ord_digs[-1][5]):
                if ord_digs[-1][1] and ord_digs[-1][4] and ord_digs[-1][3]:
                    # Enters if 2 or 5
                    if len(digit) == 5 and digit != ord_digs[-1][3]:
                        # removing one of the segments used in 1 from 4 gives the three central segments of 5
                        check = digit
                        for char in ord_digs[-1][4]:
                            check = check.replace(char, '')
                        if len(check) == 2:
                            ord_digs[-1][5] = digit
                            print('5 found!')
                        elif len(check) == 3:
                            ord_digs[-1][2] = digit
                            print('2 found!')
            # To find 9, 3 is required
            elif ord_digs[-1][3] and not ord_digs[-1][9] and len(digit) == 6:
                check = digit
                for char in ord_digs[-1][3]:
                    check = check.replace(char, '')
                if len(check) == 1:
                    ord_digs[-1][9] = digit
                    print('9 found!')

            # To find 0 and 6 having found 1, 8 and 9 is required:
            elif (not ord_digs[-1][0] or not ord_digs[-1][6]) and len(digit) == 6:
                if ord_digs[-1][1] and ord_digs[-1][8] and ord_digs[-1][9]:
                    if len(digit.replace(ord_digs[-1][1][0],'').replace(ord_digs[-1][1][1],'')) == 4 and digit != ord_digs[-1][9]:
                        ord_digs[-1][0] = digit
                        print('0 found!')
                    else:
                        ord_digs[-1][6] = digit
                        print('6 found!')

count = 0
for i in range(len(outputlist)):
    readout = ''
    for out in outputlist[i]:
        readout+=str(ord_digs[i].index(out))
    print('Line', i, ', readout:', readout)
    count += int(readout)
print('Part 2:', count)