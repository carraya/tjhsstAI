import sys; args = sys.argv[1:]
#Christopher Arraya Student, pd.6
import time; import random; import math;
start = time.time()

#solution 1: get rid of all pegs except one, where that one peg ends in the hole that was empty in the beginning
#solution 2: get rid of all pegs except one, where that one peg ends in a hole of than the hole that was empty in the beginning
#periods for empty spaces, 1's for filled, length 15
#a neighbor of a peg puzzle is 
possibleSwaps = [
  (0, 1, 3),
  (0, 2, 5, ),
  (1, 3, 6),
  (1, 4, 8),
  (2, 4, 7),
  (2, 5, 9),
  (3, 1, 0),
  (3, 4, 5),
  (3, 6, 10),
  (3, 7, 12),
  (4, 7, 11),
  (4, 8, 13),
  (5, 2, 0),
  (5, 4, 3),
  (5, 8, 12),
  (5, 9, 14),
  (6, 3, 1),
  (6, 7, 8),
  (7, 4, 2),
  (7, 8, 9),
  (8, 4, 1),
  (8, 7, 6),
  (9, 5, 2),
  (9, 8, 7),
  (10, 6, 3),
  (10, 11, 12),
  (11, 7, 4),
  (11, 12, 13),
  (12, 7, 3),
  (12, 8, 5),
  (12, 11, 10),
  (12, 13, 14),
  (13, 8, 4),
  (13, 12, 11),
  (14, 9, 5),
  (14, 13, 12)
]

def nbrs(pzl):
    nbrs = []
    for c in range(len(pzl)):
        if pzl[c]=='1':
            for s in possibleSwaps:
                if s[0] == c and pzl[s[1]] == '1' and pzl[s[2]] == '.':
                    nbr = pzl
                    nbr = nbr[:s[0]] + '.' + nbr[s[0] + 1:]
                    nbr = nbr[:s[1]] + '.' + nbr[s[1] + 1:]
                    nbr = nbr[:s[2]] + '1' + nbr[s[2] + 1:]
                    nbrs.append(nbr)
    return nbrs
        

def solve(pzl, goal):
    parseMe = [pzl]
    dctSeen = {pzl:''}

    while parseMe:
        prnt = parseMe.pop(0)
        for nbr in nbrs(prnt):
            if nbr not in dctSeen:
                if nbr == goal:
                    return nbr
                parseMe.append(nbr)
                dctSeen[nbr] = prnt
    return ''

def display(p):
    ind = 0
    leng = 1
    tab = 4
    while ind < len(p):
        x = ind
        out=' '*tab
        while x<ind+leng:
            out+=p[x]+' '
            x+=1
        print(out)
        ind+=leng
        leng+=1
        tab+=-1

if __name__ == "__main__":
    puzzle = str(args[0])
    solution = solve(puzzle, '1..............')
    secondSolution = solve(puzzle, '1..............')
    display(solution)