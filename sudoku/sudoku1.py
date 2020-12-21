import sys; args = sys.argv[1:]
#Christopher Arraya Student, pd.6
import time; import random; import math;
start = time.time()

def setGlobals(pzl):
    global size, sbW, sbH, rowC, colC, sbCon, constraintSet
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

def isInvalid(pzl):
    for i in constraintSet:
        for j in i:
            for z in i:
                if pzl[j] == pzl[z] != '.' and j!=z:
                    return True

def bruteForce(pzl):
    if isInvalid(pzl): return ""
    if pzl.find('.') == -1: return pzl
    choices = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    for possibleChoice in choices:
        subPzl = pzl
        subPzl = subPzl[:subPzl.find('.')] + possibleChoice + subPzl[subPzl.find('.')+1:]
        bF = bruteForce(subPzl)
        if bF: return bF
    return ""

def checkSum(pzl):
    return sum(ord(c) for c in pzl) - (48*(size*size))

if __name__ == '__main__':
    if len(args)==1 and args[0][-4:]=='.txt':        
        pl = open(args[0],'r').read().splitlines()
        count = 1
        newPL = pl[:20]
        print('Puzzle count: ' + str(len(pl)))
        for pzl in newPL:
            startTime = time.time()
            size = sbW = sbH = 0
            rowC = []
            colC = []
            sbCon = []
            constraintSet = []
            setGlobals(pzl)
            solution = bruteForce(pzl)
            endTime = time.time()
            print(str(count) + ': ' + pzl)
            spaces = ' ' * len(str(count))
            print(spaces + '  ' + solution + ' ' + str(checkSum(solution)) + ' ' + str(endTime-startTime) + 's')
            count+=1
            
    else:
        pzl = str(args[0])
        size = sbW = sbH = 0
        rowC = []
        colC = []
        sbCon = []
        constraintSet = []
        setGlobals(pzl)
        print(bruteForce(pzl))