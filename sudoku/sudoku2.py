import sys; args = sys.argv[1:]
#Christopher Arraya Student, pd.6
import time; import random; import math;

#IMPROVEMENT 1: bail out if possible choices is 1 or 0 
#IMPROVEMENT 2: 
#
#
#
#
#
#



def setGlobals(pzl):
    global size, sbW, sbH, rowC, colC, sbCon, constraintSet, constraintLookup
    size = int(math.sqrt(len(pzl)))
    f=1
    l=size
    i=0
    while f < l:
        i += 1
        if size % i == 0:
            f = i
            l = size//f

    sbW = l
    sbH = f
    rowC = []
    colC = []
    sbC = []
    sbR = int(size/sbH)
    sbC = int(size/sbW)

    for r in range(size):
        thisLst = [n for n in range(r*size, (r*size)+size)]
        rowC.append(thisLst)
    for c in range(size):
        thisLst = [n for n in range(c, len(pzl), size)]
        colC.append(thisLst)

    otherLst = []
    for s in range(size):
        # thisLst = [[[i for i in range(n, n+sbW)] for n in range(s*z, s*(z+sbW))] for z in range(sbH)]
        thisLst = [[i for i in range(n*sbW, (n*sbW)+sbW)] for n in range(sbH*s, (sbH*s)+sbH)]
        otherLst.append(thisLst)

    newLst = []
    for x in range(len(otherLst[0][0])):
        for xListInList in otherLst:
            newLst.append(xListInList[x])

    for i in range(0, size*sbC, sbH):
        sbCon.append(newLst[i] + newLst[i+1] + newLst[i+2])
    constraintSet = rowC
    for l in colC:
        constraintSet.append(l)
    for i in sbCon:
        constraintSet.append(i)

    constraintLookup = dict()
    for i in range(len(pzl)):
        for j in constraintSet:
            if i in j:
                if i not in constraintLookup:
                    constraintLookup[i] = [k for k in j if k!=i]
                else:
                    for b in j:
                        if b!=i and b not in constraintLookup[i]:
                            constraintLookup[i].append(b)
    
def isInvalid(pzl, ind):
    for i in constraintLookup[ind]:
        if pzl[i] == pzl[ind] != '.':
            return True
    return False

def bestMove(pzl):
    indices = []
    for i in range(len(pzl)):
        if pzl[i]=='.':
            indices.append(i)
    choices = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
    lowest = 1e9
    for i in indices:
        myChoices = {*choices}
        myChoices -= {pzl[j] for j in constraintLookup[i] if pzl[j] in myChoices}
        if len(myChoices) < lowest:
            solution = (i, myChoices)
            lowest = len(myChoices)
        if lowest<=1:
            continue
    return solution

def bruteForce(pzl, ind, dic):
    if isInvalid(pzl, ind): return ""
    if pzl.find('.') == -1: return pzl
    best = bestMove(pzl)
    nextDot = best[0]
    options = best[1]
    for possibleChoice in options:
        subPzl = pzl
        subPzl = subPzl[:nextDot] + possibleChoice + subPzl[nextDot+1:]
        bF = bruteForce(subPzl, nextDot, dic)
        if bF: return bF
    return ""

def checkSum(pzl):
    return sum(ord(c) for c in pzl) - (48*(size*size))

if __name__ == '__main__':
    if len(args)==1 and args[0][-4:]=='.txt':        
        pl = open(args[0],'r').read().splitlines()
        count = 1
        newPL = pl[:60]
        anotherTime = time.time()
        print('Puzzle count: ' + str(len(pl)))
        for pzl in newPL:
            startTime = time.time()
            size = sbW = sbH = 0
            rowC = []
            colC = []
            sbCon = []
            constraintSet = []
            constraintLookup = dict()
            setGlobals(pzl)
            solution = bruteForce(pzl, 0)
            endTime = time.time()
            print(str(count) + ': ' + pzl)
            spaces = ' ' * len(str(count))
            print(spaces + '  ' + solution + ' ' + str(checkSum(solution)) + ' ' + str(endTime-startTime) + 's')
            count+=1
        anotherEnd = time.time()
        print(anotherEnd-anotherTime)
    else:
        pzl = str(args[0])
        size = sbW = sbH = 0
        rowC = []
        colC = []
        sbCon = []
        constraintSet = []
        constraintLookup = dict()
        setGlobals(pzl)
        print(constraintLookup)
        # print(bruteForce(pzl))