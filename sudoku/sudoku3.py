import sys; args = sys.argv[1:]
#Christopher Arraya Student, pd.6
import time; import random; import math;

def setGlobals(pzl):
    global size, sbW, sbH, rowC, colC, sbCon, constraintSet, constraintLookup, choices
    choices = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
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

def makeDic(pzl):
    indices = []
    for i in range(len(pzl)):
        if pzl[i]=='.':
            indices.append(i)
    
    dic = {}
    for i in indices:
        myChoices = {*choices}
        myChoices -= {pzl[j] for j in constraintLookup[i] if pzl[j] in myChoices}
        dic[i] = myChoices
    return dic

def bestMove(dic):
    lowest = 1e9
    solution = 0
    for k in dic:
        if len(dic[k]) < lowest:
            lowest = len(dic[k])
            solution = k
        if lowest <= 1:
            continue
        
    return solution




def possiblePlaces(pzl, passedDownDic):
    dic = {}
    smallestOld = 1e9
    smallestNew = 1e9
    storeOld = 0
    storeNew = 0
    for i in passedDownDic:
        if len(passedDownDic[i]) < smallestOld:
            smallestOld = len(passedDownDic[i])
            storeOld = i
    for c in choices:
        for constraints in constraintSet:
            for i in constraints:
                if i in passedDownDic:
                    if pzl[i] == '.' and c in passedDownDic[i]:
                        if c in dic:
                            dic[c].add(i)
                        else:
                            dic[c] = {i}
        if c in dic:
            if len(dic[c]) < 2:
                continue
        elif c not in dic:
            continue 
    
    for i in dic:
        if len(dic[i]) < smallestNew:
            smallestNew = len(dic[i])
            storeNew = i
    if smallestNew < smallestOld:
        return (1, storeNew, dic[storeNew])
    else:
        return (0, storeOld, passedDownDic[storeOld])

def bruteForce(pzl, ind, dic):
    if pzl.find('.') == -1: return pzl
    # loopThrough = possiblePlaces(pzl, dic)
    nextDot = bestMove(dic)
    # symbolDic = possiblePlaces(pzl, dic)
    # lowestPlace = bestMove(symbolDic)

    # if loopThrough[0] == 0:
    for possibleChoice in dic[nextDot]:
        subPzl = pzl
        subPzl = subPzl[:nextDot] + possibleChoice + subPzl[nextDot+1:]
        # cpy = {k:{*dic[k]} for k in dic if k!=nextDot}
        track = {k: {} for k in dic if k!=nextDot}
        for i in constraintLookup[nextDot]: #go through constraints of index that I just replaced 
            if i==nextDot:
                track[i] += dic[nextDot]
                dic.pop(i)
                pass
            if i in dic: #check if each constraint is in copy
                if possibleChoice in dic[i]: #if it is, then check if the symbol we are at in the choices is in the choices for something that can't have that choice
                    track[i] += {possibleChoice}
                    dic[i] -= {possibleChoice} #if those two conditions are met
        print(track)
        bF = bruteForce(subPzl, nextDot, dic)
        for i in track:
            if i not in dic:
                dic[i] = track[i]
            else:
                dic[i] += track[i]
        if bF: return bF
    return ""

    # elif loopThrough[0] == 1:
    #     lowestPlace = loopThrough[1]
    #     newChoices = loopThrough[2]
    #     for possibleIndex in newChoices:
    #         subPzl = pzl
    #         subPzl = subPzl[:possibleIndex] + lowestPlace + subPzl[possibleIndex+1:]
    #         cpy = {k:{*dic[k]} for k in dic if k!=possibleIndex}
    #         for i in constraintLookup[possibleIndex]: #go through constraints of index that I just replaced 
    #             if i in dic: #check if each constraint is in copy
    #                 if lowestPlace in dic[i]: #if it is, then check if the symbol we are at in the choices is in the choices for something that can't have that choice
    #                     cpy[i] -= {lowestPlace} #if those two conditions are met
    #         bF = bruteForce(subPzl, possibleIndex, cpy)
    #         if bF: return bF
    #     return ""

    # elif loopThrough[0] == 3:
    #     return ""

            
        

def checkSum(pzl):
    return sum(ord(c) for c in pzl) - (48*(size*size))

if __name__ == '__main__':
    if len(args)==1 and args[0][-4:]=='.txt':        
        pl = open(args[0],'r').read().splitlines()
        count = 1
        anotherTime = time.time()
        print('Puzzle count: ' + str(len(pl)))
        for pzl in pl:
            startTime = time.time()
            size = sbW = sbH = 0
            rowC = []
            colC = []
            sbCon = []
            constraintSet = []
            choices = {}
            constraintLookup = dict()
            setGlobals(pzl)
            dic = makeDic(pzl)
            solution = bruteForce(pzl, 0, dic)
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