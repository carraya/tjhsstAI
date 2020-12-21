import sys; args = sys.argv[1:]
#Christopher Arraya Student, pd.6
import time; import random;
start = time.time()
global gNBRPOS
### DIMENSIONS ###

def findDimensions(length):
    f=1
    l=length
    i=0
    while f < l:
        i += 1
        if length % i == 0:
            f = i
            l =length//f
    return [l, f]

### SOLVABILITY

def isSolvable(startPos, goalState, v, h):
    noUS = startPos[:startPos.index('_')] + startPos[startPos.index('_') + 1:]
    noUSGoal = goalState[:goalState.index('_')] + goalState[goalState.index('_') + 1:]
    inversionCountStart = 0
    inversionCountGoal = 0
    lsStart=[c for c in noUS]
    lsGoal=[c for c in noUSGoal]
    
    for i in range(len(lsStart)):
        for j in range(i+1, len(lsStart)):
            if(lsStart[i]>lsStart[j]):
                inversionCountStart+=1
    
    for i in range(len(lsGoal)):
        for j in range(i+1, len(lsGoal)):
            if(lsGoal[i]>lsGoal[j]):
                inversionCountGoal+=1
    if h%2==1:
        if inversionCountStart%2 == inversionCountGoal%2:
            return True
        return False
    elif h%2==0:
        if (inversionCountStart + (startPos.index('_')//h))%2 == (inversionCountGoal + (goalState.index('_')//h))%2:
            return True
        return False

### NEIGHBORS ###

def swap(pzl,p1,p2):
    pzlLst = [*pzl]
    pzlLst[p1], pzlLst[p2] = pzlLst[p2], pzlLst[p1]
    return ''.join(pzlLst)

def neighbors(pos,v,h):
    uPos = pos.find('_')
    if uPos<h: swapPos = {uPos+h,uPos+(uPos!=h-1),uPos-1}-{-1,uPos}
    elif uPos>=len(pos)-h: swapPos = {uPos-h,uPos+1,uPos-(uPos!=len(pos)-h)}-{len(pos),uPos}
    elif uPos%h==0: swapPos = {uPos+1,uPos+h,uPos-h}
    elif (uPos+1)%h==0: swapPos = {uPos-1,uPos+h,uPos-h}
    else: swapPos = {uPos+1,uPos-1,uPos+h,uPos-h}
    return [swap(pos,uPos,sp) for sp in swapPos]

# def neighbors(pos,v,h):
#     priorPos = uPos = pos.find('_')
#     p, res = [*pos], []

#     for nextPos in gNBRPOS[uPos]:
#         p[priorPos], p[uPos], p[nextPos], priorPos = p[uPos], p[nextPos], p[priorPos], nextPos
#         res.append(''.join(p))
#     return res

### BFS ###
    
# def pathFromRootToGoal(dctSeen, goalState):
#     path=[] 
#     parseMe = [goalState]
#     ptr=0
#     while parseMe:
#         item = parseMe.pop(0)
#         if item == '': return path[::-1]
#         parseMe.append(dctSeen[item])
#         path.append(item)
#     return []

# def find_shortest_path(startPos, goalState, v, h):
#     if startPos==goalState: return [startPos]
#     if not isSolvable(startPos,goalState,v,h): return []
#     dctSeen = {startPos: ''}
#     parseMe = [startPos]
#     ptr=0
#     while ptr<len(parseMe):#while parseMe:
#         prnt=parseMe[ptr]#prnt = parseMe.pop(0)
#         ptr+=1
#         if prnt==goalState: return pathFromRootToGoal(dctSeen, goalState)
#         for n in neighbors(prnt, v, h):
#             if n not in dctSeen:   
#                 parseMe.append(n) 
#                 dctSeen[n] = prnt
#     return []
def pathFromRootToGoal(dctSeen, goalState):
    path=[] 
    parseMe = [goalState]
    ptr=0
    while parseMe:
        item = parseMe.pop(0)
        if item == '': return path[::-1]
        parseMe.append(dctSeen[item])
        path.append(item)
    return []

def find_shortest_path(startPos, goalState, v, h):
    if startPos==goalState: return [startPos]
    if not isSolvable(startPos,goalState,v,h): return []

    dctSeen = {startPos: ''}
    parseMe = [(startPos, startPos.find('_'), -1)]
    ptr=0
    
    while ptr<len(parseMe):
        prnt, uPos, gpuPos = parseMe[ptr]
        ptr+=1

        p, pPos = [*prnt], uPos

        for nPos in NBRPOS[uPos]:
            if nPos == gpuPos: continue
            p[pPos], p[uPos], p[nPos], pPos = p[uPos], p[nPos], p[pPos], nPos
            nbr = ''.join(p)

            if nbr in dctSeen: continue

            parseMe.append((nbr, nPos, uPos))
            dctSeen[nbr] = prnt

            if nbr == goalState: return pathFromRootToGoal(dctSeen, goalState)

    return []

# def degreeList():
#     dctSeen = {startPos: ''}
#     dctLevel = {startPos: 0}
#     parseMe = [startPos]
#     while parseMe:
#         prnt = parseMe.pop(0)
#         for n in neighbors(prnt, v, h):
#             if n not in dctSeen:
#                 parseMe.append(n) 
#                 dctSeen[n] = prnt
#                 dctLevel[n] = dctLevel[prnt]+1
#     return dctLevel

# newDct = degreeList()

# def degreeList2(g):
#     ls = [0]
#     for k in g:
#         degree = g[k]
#         if len(ls)-1<degree:
#             ls+=[0]*(degree-(len(ls))+1)
#         ls[degree]+=1
#     return ls

# print(' '.join(map(str, degreeList2(newDct))))

# if isSolvable():
#     path = find_shortest_path()
# else:
#     path = []

def displayPath(path, v, h):
    if path==[]:
        for j in range(v):
            for i in range(1):
                print(startPos[(len(startPos)//v)*j:(len(startPos)//v)*(j+1)], end='     ')
            print('')

    if path != []:
        for u in range(0,len(path),6):
            for j in range(v):
                for i in path[u:u+6]:
                    if (u%6!=0):
                        print(i[(len(i)//v)*j:(len(i)//v)*(j+1)], end='     ')
                    elif (u%6==0):
                        # print('')
                        print(i[(len(i)//v)*j:(len(i)//v)*(j+1)], end='     ')
                print('')
            print('')

    print('Steps: ' + str(len(path)-1))

    
    
if len(args)==0:
    goalState = '12345678_'
    statsCtr = [0]*5
    ls=['1','2','3','4','5','6','7','8','_']
    solvedPuzzleCount = 0
    for i in range(500):
        shuffledList = list(random.sample(ls[:], len(ls)))
        startPos = ''.join(shuffledList)
        newTime = time.time()
        dimensions = findDimensions(len(startPos))
        v=dimensions[0]
        h=dimensions[1]
        
        processTime = time.time()
        if not isSolvable(startPos, goalState, v, h):
            path = []
            endProcess = time.time()
            statsCtr[1]+=(endProcess-processTime)
            statsCtr[2]+=1
        else:
            path = find_shortest_path(startPos, goalState, v, h)
            endProcess = time.time()
            statsCtr[4]+=(endProcess-processTime)
            statsCtr[3]+=(len(path)-1)
            solvedPuzzleCount+=1
    end = time.time()
    statsCtr[0]=(end-start)
    statsCtr[1]/=statsCtr[2]
    statsCtr[3]/=solvedPuzzleCount
    statsCtr[4]/=solvedPuzzleCount
    print(statsCtr[0])
    print(statsCtr[1])
    print(statsCtr[2])
    print(statsCtr[3])
    print(statsCtr[4])

elif len(args)==1:
    startPos=str(args[0])
    str1=''
    for i in range(1,len(startPos)):
        str1+=str(i)
    goalState=str1+'_'
    # gNBRPOS = [({u+h,u-h,u-(u%h>0),u+((u+1)%h>0)} & {*range(len(startPos))})-{u} for u in range(len(startPos))]
    dimensions = findDimensions(len(startPos))
    v=dimensions[0]
    h=dimensions[1]

    if isSolvable(startPos, goalState, v, h):
        path = find_shortest_path(startPos, goalState, v, h)
    else:
        path = []
    displayPath(path, v, h)
    end = time.time()

else:
    startPos=str(args[0])
    goalState=str(args[1])
    
    dimensions = findDimensions(len(startPos))
    v=dimensions[0]
    h=dimensions[1]

    if isSolvable(startPos, goalState, v, h):
        path = find_shortest_path(startPos, goalState, v, h)
    else:
        path = []
    displayPath(path, v, h)
    end = time.time()


if end-start>=1.0:
    print(f"Time: {round(end - start,2)}s")
else:   
    print(f"Time: {round(end - start,3)}s")
# 134.67081356048584 (total)
# 0.00013116890924018727 (impossible puzzle avg time)
# 228 (num of impos puz)
# 22.106617647058822 (avg path length)
# 0.49496672521619234 (avg time to solve)
# TIMES