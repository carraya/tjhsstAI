import sys; args = sys.argv[1:]
for i in range(len(args)):
    args[i] = args[i].lower()

#Christopher Arraya Student, pd.6
table = dict()
for i in range(64):
    table[i] = [[],[],[],[],[],[],[],[]]
    t1 = i+8
    while t1 <= 63:
        table[i][0].append(t1)
        t1+=8
    t2 = i-8
    while t2 >= 0:
        table[i][1].append(t2)
        t2-=8
    t3 = i+1
    while t3%8 != 0:
        table[i][2].append(t3)
        t3+=1
    t4 = i-1
    while (t4-7)%8 != 0:
        table[i][3].append(t4)
        t4-=1
    t5 = i-9
    while (t5-7)%8 != 0 and t5 >= 0:
        table[i][4].append(t5)
        t5-=9
    t6 = i+7
    while (t6-7)%8 != 0 and t6 <= 63:
        table[i][5].append(t6)
        t6 += 7
    t7 = i-7
    while t7%8 != 0 and t7 >= 0:
        table[i][6].append(t7)
        t7-=7
    t8 = i+9
    while t8%8 != 0 and t8 <= 63:
        table[i][7].append(t8)
        t8+=9

def neighbors(board, token, opposite):
    tokens = []
    for i in range(len(board)):
        if board[i] == token:
            tokens.append(i)
    solution = []
    moveHelper = dict()
    for k in tokens: #go through each token
        for i in table[k]: #go through each possible place you can put the other token (the lists)
            ls = []
            indices = []
            for j in i: #go through each possible place you can put the other token(now we are in the lists)
                ls.append(board[j]) #append the letter at that position
                indices.append(j) #append the index
                if board[j] == token: #if the letter is the same as the token, skip
                    break
                elif board[j] == '.': #if its a period
                    if len(ls)-1 == ls.count(opposite) and ls[0] == opposite and j not in solution: #if all the letters in ls are the opposite
                        solution.append(j)
                    if len(ls)-1 == ls.count(opposite) and ls[0] == opposite:
                        if j not in moveHelper:
                            moveHelper[j] = indices
                        else:
                            moveHelper[j] += indices
                    break
    return [solution, moveHelper]

def makeMove(board, token, opposite, moves):
    returnThis = []
    for move in moves:
        gen = neighbors(board, token, opposite)
        nbrs = gen[0]
        helper = gen[1]
        if len(nbrs) == 0:
            temp = token
            token = opposite
            opposite = temp
            gen = neighbors(board, token, opposite)
            nbrs = gen[0]
            helper = gen[1]
        tempBoard = board
        if move in helper:
            for i in helper[move]:
                tempBoard = tempBoard[:i] + token + tempBoard[i+1:]
        returnThis.append([move, board, tempBoard, token, nbrs]) #move, current board, next board, current token, current nbrs
        board = tempBoard
        t = token
        token = opposite
        opposite = t
    gen = neighbors(returnThis[-1][2],token,opposite)
    nbrs = gen[0]
    if len(nbrs) == 0:
        temp = token
        token = opposite
        opposite = temp
        gen = neighbors(board, token, opposite)
        nbrs = gen[0]
    returnThis.append([moves[-1], board, board, token, nbrs])
    return returnThis

def display(board, token, moves, opposite):
    calc = makeMove(board,token,opposite,moves)
    temp = board
    for n in calc[0][4]:
        temp = temp[:n] + '*' + temp[n+1:]
    for x in range(0, 63, 8):
        print(temp[x:x+8])
    print(calc[0][1] + ' ' + str(calc[0][1].count('x')) + '/' + str(calc[0][1].count('o')))
    print('Possible moves for ' + calc[0][3] + ': ' + str(calc[0][4]))
    saveToken = calc[0][3]
    saveMove = calc[0][0]
    calc = calc[1:]
    for m in calc:
        temp = m[1]
        print(saveToken + ' moves to ' + str(saveMove))
        for n in m[4]:
            temp = temp[:n] + '*' + temp[n+1:]
        for x in range(0, 63, 8):
            print(temp[x:x+8])
        print(m[1] + ' ' + str(m[1].count('x')) + '/' + str(m[1].count('o')))
        if len(m[4]) == 0:
            print('No possible moves.')
        else:
            print('Possible moves for ' + m[3] + ': ' + str(m[4]))
        saveToken = m[3]
        saveMove = m[0]

        




if __name__ == "__main__":
    global board, token, opposite, move

    if args:

        if len(args) >= 3:

            if len(args[0]) == 64:
                if args[1] == 'x' or args[1] == 'o': #board first token second moves third
                    board = args[0]
                    token = args[1]
                    if token == 'x':
                        opposite = 'o'
                    else:
                        opposite = 'x'
                    move = []
                    for i in args[2:]:
                        if i.isalpha():
                            n = ((int(i[1])-1)*8) + (ord(i[0]) - 97)
                        else:
                            n = int(i)
                        if n >= 0:
                            move.append(n)

                else: #board first moves second
                    board = args[0]
                    blanks = board.count('.')
                    if blanks%2 == 0:
                        token = 'x'
                        opposite = 'o'
                    else:
                        token = 'o'
                        opposite = 'x'
                    move = []
                    for i in args[1:]:
                        if i[0].isalpha():
                            n = ((int(i[1])-1)*8) + (ord(i[0]) - 97)
                        else:
                            n = int(i)
                        if n >= 0:
                            move.append(n)


            elif args[0] == 'x' or args[0] == 'o': #token first moves second
                board = '.'*27 + 'ox......xo' + '.'*27
                token = args[0]
                if token == 'x':
                    opposite = 'o'
                else:
                    opposite = 'x'
                move = []
                for i in args[1:]:
                    if i[0].isalpha():
                        n = ((int(i[1])-1)*8) + (ord(i[0]) - 97)
                    else:
                        n = int(i)
                    if i >= 0:
                        move.append(n)

            else: #only moves
                board = '.'*27 + 'ox......xo' + '.'*27
                token = 'x'
                opposite = 'o'
                move = []
                for i in args:
                    if i[0].isalpha():
                        n = ((int(i[1])-1)*8) + (ord(i[0]) - 97)
                    else:
                        n = int(i)
                    if n >= 0:
                        move.append(n)
        
        elif len(args) == 2: #2 arguments

            if len(args[0]) == 64:
                if args[1] == 'x' or args[1] == 'o': #board first token second
                    board = args[0]
                    token = args[1]
                    if token == 'x':
                        opposite = 'o'
                    else:
                        opposite = 'x'
                    move = 'NO'

                else: #board first move second
                    board = args[0]
                    blanks = board.count('.')
                    if blanks%2 == 0:
                        token = 'x'
                        opposite = 'o'
                    else:
                        token = 'o'
                        opposite = 'x'
                    if args[1][0].isalpha():
                        y = [((int(args[1][1])-1)*8) + (ord(args[1][0]) - 97)]
                    if int(y) >= 0:
                        move = [y]
                    else:
                        move = 'NO'
            
            elif args[0] == 'x' or args[0] == 'o': #token first move second
                board = '.'*27 + 'ox......xo' + '.'*27
                token = args[0]
                if token == 'x':
                    opposite = 'o'
                else:
                    opposite = 'x'
                if args[1][0].isalpha():
                        y = [((int(args[1][1])-1)*8) + (ord(args[1][0]) - 97)]
                else:
                    y = args[1]
                if int(y) >= 0:
                    move = [y]
                else:
                    move = 'NO'

            else: #only moves
                board = '.'*27 + 'ox......xo' + '.'*27
                token = 'x'
                opposite = 'o'
                for i in args:
                    if i[0].isalpha():
                        n = ((int(i[1])-1)*8) + (ord(i[0]) - 97)
                    else:
                        n = int(i)
                    if n >= 0:
                        move.append(n)
    
        elif len(args) == 1:

            if len(args[0]) == 64:
                board = args[0]
                blanks = board.count('.')
                if blanks%2 == 0:
                    token = 'x'
                    opposite = 'o'
                else:
                    token = 'o'
                    opposite = 'x'
                move = 'NO'

            elif args[0] == 'x' or args[0] == 'o':
                board = '.'*27 + 'ox......xo' + '.'*27
                token = args[0]
                if token == 'x':
                    opposite = 'o'
                else:
                    opposite = 'x'
                move = 'NO'

            else:
                board = '.'*27 + 'ox......xo' + '.'*27
                token = 'x'
                opposite = 'o'
                if args[0][0].isalpha():
                    y = [((int(args[0][1])-1)*8) + (ord(args[0][0]) - 97)]
                if int(y) >= 0:
                    move = [y]
                else:
                    move = 'NO'

    else: #if no arguments
        board = '.'*27 + 'ox......xo' + '.'*27
        token = 'x'
        opposite = 'o'
        move = 'NO'
    
    display(board,token,move,opposite)