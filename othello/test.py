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

def makeMove(board, token, move, helper):
    newBoard = board
    if move not in helper:
        return board
    for i in helper[move]:
        newBoard = newBoard[:i] + token + newBoard[i+1:]
    return newBoard

def display(board, token, movess, opposite):
    calc = neighbors(board,token,opposite)
    nbrs = calc[0]
    helper = calc[1]
    for m in range(len(movess)):
        move = movess[m]
        if move == 'NO':
            if len(nbrs) == 0:
                tempvar = token
                token = opposite
                opposite = token
                calc = neighbors(board,token,opposite)
                nbrs = calc[0]
                helper = calc[1]
            if len(nbrs) == 0:
                for x in range(0, 63, 8):
                    print(board[x:x+8])
                print(board + ' ' + str(board.count('x')) + '/' + str(board.count('o')))
                for x in range(0, 63, 8):
                    print(board[x:x+8])
                print(board + ' ' + str(board.count('x')) + '/' + str(board.count('o')))
            else:
                temp = board
                for n in nbrs:
                    temp = temp[:n] + '*' + temp[n+1:]
                for x in range(0, 63, 8):
                    print(temp[x:x+8])
                print(board + ' ' + str(board.count('x')) + '/' + str(board.count('o')))
                print('Possible moves for ' + token + ': ' + str(nbrs))
        else:
            if len(nbrs) == 0:
                tempvar = token
                token = opposite
                opposite = tempvar
                calc = neighbors(board,token,opposite)
                nbrs = calc[0]
                helper = calc[1]
            if len(nbrs) == 0:
                for x in range(0, 63, 8):
                    print(board[x:x+8])
                print(board + ' ' + str(board.count('x')) + '/' + str(board.count('o')))
                for x in range(0, 63, 8):
                    print(board[x:x+8])
                print(board + ' ' + str(board.count('x')) + '/' + str(board.count('o')))
            else:
                if m==0:
                    temp = board
                    for n in nbrs:
                        temp = temp[:n] + '*' + temp[n+1:]
                    for x in range(0, 63, 8):
                        print(temp[x:x+8])
                    print(board + ' ' + str(board.count('x')) + '/' + str(board.count('o')))
                    print('Possible moves for ' + token + ': ' + str(nbrs))
                    
                    board = makeMove(board, token, move, helper)
                    newT = token
                    token = opposite
                    opposite = newT
                    k = neighbors(board,token,opposite)
                    nbrs = k[0]
                    helper = k[1]
                    print(opposite + ' moves to ' + str(move))
                    temp = board
                    for n in nbrs:
                        temp = temp[:n] + '*' + temp[n+1:]
                    for x in range(0, 63, 8):
                        print(temp[x:x+8])
                    print(board + ' ' + str(board.count('x')) + '/' + str(board.count('o')))
                    print('Possible moves for ' + token + ': ' + str(nbrs))
                else:
                    if len(nbrs) == 0:
                        print('here')
                        tempvar = token
                        token = opposite
                        opposite = tempvar
                        calc = neighbors(board,token,opposite)
                        nbrs = calc[0]
                        helper = calc[1]
                    board = makeMove(board, token, move, helper)
                    newT = token
                    token = opposite
                    opposite = newT
                    k = neighbors(board,token,opposite)
                    nbrs = k[0]
                    helper = k[1]
                    
                    print(opposite + ' moves to ' + str(move))
                    temp = board
                    for n in nbrs:
                        temp = temp[:n] + '*' + temp[n+1:]
                    for x in range(0, 63, 8):
                        print(temp[x:x+8])
                    print(board + ' ' + str(board.count('x')) + '/' + str(board.count('o')))
                    if len(nbrs) == 0:
                        print('No possible moves.')
                    else:
                        print('Possible moves for ' + token + ': ' + str(nbrs))




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