import sys; args = sys.argv[1:]
for i in range(len(args)):
    args[i] = args[i].lower()

#Christopher Arraya Student, pd.6

def makeLookupTable(board, token):
    lookupTable = dict()
    for i in range(64):
        if board[i] == token:
            lookupTable[i] = [[],[],[],[],[],[],[],[]]
            t1 = i+8
            while t1 <= 63:
                lookupTable[i][0].append(t1)
                t1+=8
            t2 = i-8
            while t2 >= 0:
                lookupTable[i][1].append(t2)
                t2-=8
            t3 = i+1
            while t3%8 != 0:
                lookupTable[i][2].append(t3)
                t3+=1
            t4 = i-1
            while (t4-7)%8 != 0:
                lookupTable[i][3].append(t4)
                t4-=1
            t5 = i-9
            while (t5-7)%8 != 0 and t5 >= 0:
                lookupTable[i][4].append(t5)
                t5-=9
            t6 = i+7
            while (t6-7)%8 != 0 and t6 <= 63:
                lookupTable[i][5].append(t6)
                t6 += 7
            t7 = i-7
            while t7%8 != 0 and t7 >= 0:
                lookupTable[i][6].append(t7)
                t7-=7
            t8 = i+9
            while t8%8 != 0 and t8 <= 63:
                lookupTable[i][7].append(t8)
                t8+=9
    return lookupTable

def neighbors(board, token, opposite, table):
    solution = []
    for k in table:
        for i in table[k]:
            ls = []
            for j in i:
                ls.append(board[j])
                if board[j] == token:
                    break
                elif board[j] == '.':
                    if len(ls)-1 == ls.count(opposite) and ls[0] == opposite and j not in solution:
                        solution.append(j)
                    break
    return solution
# def display(board):

if __name__ == "__main__":
    global board, token, opposite
    if args:
        if len(args) == 2:
            board = args[0]
            token = args[1]
            if token == 'x':
                opposite = 'o'
            else:
                opposite = 'x'
            table = makeLookupTable(board, token)
            nbrs = neighbors(board, token, opposite, table)
            temp = board
            for n in nbrs:
                temp = temp[:n] + '*' + temp[n+1:]
            for x in range(0, 63, 8):
                print(board[x:x+8])
            if len(nbrs) == 0:
                print('No moves possible.')
            print(nbrs)
        else:
            blanks = 0
            if len(args[0]) == 64:
                board = args[0]
                blanks = board.count('.')
                if blanks%2 == 0:
                    token = 'x'
                    opposite = 'o'
                else:
                    token = 'o'
                    opposite = 'x'
                
            else:
                board = '.'*27 + 'ox......xo' + '.'*27
                token = args[0]
                if token == 'x':
                    opposite = 'o'
                else:
                    opposite = 'x' 
            table = makeLookupTable(board, token)
            nbrs = neighbors(board, token, opposite, table)
            temp = board
            for n in nbrs:
                temp = temp[:n] + '*' + temp[n+1:]
            for x in range(0, 63, 8):
                print(board[x:x+8])
            if len(nbrs) == 0:
                print('No moves possible.')
            print(nbrs)
    else:
        board = '.'*27 + 'ox......xo' + '.'*27
        token = 'x'
        opposite = 'o'
        table = makeLookupTable(board, token)
        nbrs = neighbors(board, token, opposite, table)
        temp = board
        for n in nbrs:
            temp = temp[:n] + '*' + temp[n+1:]
        for x in range(0, 63, 8):
            print(board[x:x+8])
        if len(nbrs) == 0:
            print('No moves possible.')
        print(nbrs)
    
    
    

#check if there are any enemy pieces between your current token and any space forming a row, column, or diaganol
#if there is then those are possible moves
#if there isn't then there are no possible moves