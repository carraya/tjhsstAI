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

def display(board, token, move, opposite):
    calc = neighbors(board,token,opposite)
    nbrs = calc[0]
    helper = calc[1]
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
            print(token + ' moves to ' + str(move))
            newBoard = makeMove(board, token, move, helper)
            newNbrs = neighbors(newBoard,opposite,token)[0]
            newTemp = newBoard
            for n in newNbrs:
                newTemp = newTemp[:n] + '*' + newTemp[n+1:]
            for x in range(0, 63, 8):
                print(newTemp[x:x+8])
            print(newBoard + ' ' + str(newBoard.count('x')) + '/' + str(newBoard.count('o'))) #print score
            print('Possible moves for ' + opposite + ': ' + str(newNbrs))


if __name__ == "__main__":
    global board, token, opposite, move
    if args:
        if len(args) == 3: #all arguments
            board = args[0]
            token = args[1]
            move = args[2]
            if token == 'x':
                opposite = 'o'
            else:
                opposite = 'x'
            if move[0].isalpha():
                move = ((int(move[1])-1)*8) + (ord(move[0]) - 97)
            display(board, token, int(move), opposite)
        elif len(args) == 2: #if two arguments
            if len(args[0]) == 64 and (args[1] == 'x' or args[1] == 'o'): #if its board and token
                board = args[0]
                token = args[1]
                move = 'NO'
                if token == 'x':
                    opposite = 'o'
                else:
                    opposite = 'x'
                display(board, token, move, opposite)
            elif len(args[0]) == 64 and (args[1][0].isalpha() or args[1].isdigit): #if its board and move
                board = args[0]
                move = args[1]
                blanks = board.count('.')
                if blanks%2 == 0:
                    token = 'x'
                    opposite = 'o'
                else:
                    token = 'o'
                    opposite = 'x'
                if move[0].isalpha():
                    move = ((int(move[1])-1)*8) + (ord(move[0]) - 97)
                display(board, token, int(move), opposite)
            else: #if its token and move
                board = '.'*27 + 'ox......xo' + '.'*27
                token = args[0]
                move = args[1]
                if token == 'x':
                    opposite = 'o'
                else:
                    opposite = 'x'
                if move[0].isalpha():
                    move = ((int(move[1])-1)*8) + (ord(move[0]) - 97)
                display(board, token, int(move), opposite)
        else: #if one argument
            if len(args[0]) == 64: #if its board
                board = args[0]
                blanks = board.count('.')
                if blanks%2 == 0:
                    token = 'x'
                    opposite = 'o'
                else:
                    token = 'o'
                    opposite = 'x'
                move = 'NO'
                display(board, token, move, opposite)
            elif args[0] == 'x' or args[0] == 'o': #if its token
                board = '.'*27 + 'ox......xo' + '.'*27
                token = args[0]
                move = 'NO'
                display(board, token, move, opposite)
            else: #if its move
                board = '.'*27 + 'ox......xo' + '.'*27
                blanks = board.count('.')
                if blanks%2 == 0:
                    token = 'x'
                    opposite = 'o'
                else:
                    token = 'o'
                    opposite = 'x'
                move = args[0]
                if move[0].isalpha():
                    move = ((int(move[1])-1)*8) + (ord(move[0]) - 97)
                display(board, token, int(move), opposite)
    else: #if no arguments
        board = '.'*27 + 'ox......xo' + '.'*27
        token = 'x'
        opposite = 'o'
        move = 'NO'
        display(board, token, move, opposite)