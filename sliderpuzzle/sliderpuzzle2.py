import sys; args = sys.argv[1:]
#Christopher Arraya Student, pd.6
import time; import random;
start = time.time()

# length = len(startPos)

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

def neighbors(pos, v, h):
    children=[]
    usPos = pos.find('_')
    tlc = 0
    trc = 0
    blc = 0
    brc = 0
    le = 0
    re = 0
    te = 0
    be = 0
    c = 0
    if usPos==0:
        tlc=1
    elif usPos==h-1:
        trc=1
    elif usPos==h*(v-1):
        blc=1
    elif usPos==(h*v)-1:
        brc=1
    for i in range(1, v-1):
        if usPos==(h*i):
            le=1
        elif usPos==(h*i)+(h-1):
            re=1
    if usPos>=1 and usPos<=h-2:
        te=1
    elif usPos>=1+((v-1)*h) and usPos<=(v*h)-2:
            be=1
    elif tlc==0 and trc==0 and blc==0 and brc==0 and le==0 and re==0 and te==0 and be==0:
        c=1
    
    if tlc:
        strlst1 = list(pos)
        strlst1[usPos], strlst1[1] = strlst1[1], strlst1[usPos];
        children.append("".join(strlst1))
        strlst2 = list(pos)
        strlst2[usPos], strlst2[h] = strlst2[h], strlst2[usPos];
        children.append("".join(strlst2))
    elif trc:
        strlst1 = list(pos)
        strlst1[usPos], strlst1[usPos-1] = strlst1[usPos-1], strlst1[usPos];
        children.append("".join(strlst1))
        strlst2 = list(pos)
        strlst2[usPos], strlst2[usPos+h] = strlst2[usPos+h], strlst2[usPos];
        children.append("".join(strlst2))
    elif blc:
        strlst1 = list(pos)
        strlst1[usPos], strlst1[usPos+1] = strlst1[usPos+1], strlst1[usPos];
        children.append("".join(strlst1))
        strlst2 = list(pos)
        strlst2[usPos], strlst2[usPos-h] = strlst2[usPos-h], strlst2[usPos];
        children.append("".join(strlst2))
    elif brc:
        strlst1 = list(pos)
        strlst1[usPos], strlst1[usPos-1] = strlst1[usPos-1], strlst1[usPos];
        children.append("".join(strlst1))
        strlst2 = list(pos)
        strlst2[usPos], strlst2[usPos-h] = strlst2[usPos-h], strlst2[usPos];
        children.append("".join(strlst2))
    elif le:
        strlst1 = list(pos)
        strlst1[usPos], strlst1[usPos-h] = strlst1[usPos-h], strlst1[usPos];
        children.append("".join(strlst1))
        strlst2 = list(pos)
        strlst2[usPos], strlst2[usPos+1] = strlst2[usPos+1], strlst2[usPos];
        children.append("".join(strlst2))
        strlst3 = list(pos)
        strlst3[usPos], strlst3[usPos+h] = strlst3[usPos+h], strlst3[usPos];
        children.append("".join(strlst3))
    elif re:
        strlst1 = list(pos)
        strlst1[usPos], strlst1[usPos-h] = strlst1[usPos-h], strlst1[usPos];
        children.append("".join(strlst1))
        strlst2 = list(pos)
        strlst2[usPos], strlst2[usPos-1] = strlst2[usPos-1], strlst2[usPos];
        children.append("".join(strlst2))
        strlst3 = list(pos)
        strlst3[usPos], strlst3[usPos+h] = strlst3[usPos+h], strlst3[usPos];
        children.append("".join(strlst3))
    elif te:
        strlst1 = list(pos)
        strlst1[usPos], strlst1[usPos+1] = strlst1[usPos+1], strlst1[usPos];
        children.append("".join(strlst1))
        strlst2 = list(pos)
        strlst2[usPos], strlst2[usPos-1] = strlst2[usPos-1], strlst2[usPos];
        children.append("".join(strlst2))
        strlst3 = list(pos)
        strlst3[usPos], strlst3[usPos+h] = strlst3[usPos+h], strlst3[usPos];
        children.append("".join(strlst3))
    elif be:
        strlst1 = list(pos)
        strlst1[usPos], strlst1[usPos+1] = strlst1[usPos+1], strlst1[usPos];
        children.append("".join(strlst1))
        strlst2 = list(pos)
        strlst2[usPos], strlst2[usPos-1] = strlst2[usPos-1], strlst2[usPos];
        children.append("".join(strlst2))
        strlst3 = list(pos)
        strlst3[usPos], strlst3[usPos-h] = strlst3[usPos-h], strlst3[usPos];
        children.append("".join(strlst3))
    elif c:
        strlst1 = list(pos)
        strlst1[usPos], strlst1[usPos+1] = strlst1[usPos+1], strlst1[usPos];
        children.append("".join(strlst1))
        strlst2 = list(pos)
        strlst2[usPos], strlst2[usPos-1] = strlst2[usPos-1], strlst2[usPos];
        children.append("".join(strlst2))
        strlst3 = list(pos)
        strlst3[usPos], strlst3[usPos+h] = strlst3[usPos+h], strlst3[usPos];
        children.append("".join(strlst3))
        strlst4 = list(pos)
        strlst4[usPos], strlst4[usPos-h] = strlst4[usPos-h], strlst4[usPos];
        children.append("".join(strlst4))
    return children

def manDist(start, goal, v, h):
    s=0
    e=0
    manCount=0
    # goal=goalState[:goalState.index('_')] + goalState[goalState.index('_')+1:]
    # start=startPos[:startPos.index('_')] + startPos[startPos.index('_')+1:]
    for i in goal:
        if i=='_':
            pass
        else:
            s=start.index(i)
            e=goal.index(i)
            manCount += (abs((s//v)-(e//v)) + abs((s%h)-(e%h)))
    return manCount
    
    
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
    if not isSolvable(startPos, goalState, v, h): return []

    dctSeen = {startPos: ''}
    parseMe = [(manDist(startPos,goalState,v,h), startPos)]

    while parseMe:
        md, pzl = parseMe.pop(0)
        for nbr in neighbors(pzl,v,h):
            if nbr in dctSeen: continue

            dctSeen[nbr]=pzl
            mdn=manDist(nbr,goalState,v,h)
            parseMe+=[(mdn,nbr)]
            if nbr==goalState: return pathFromRootToGoal(dctSeen, goalState)

        parseMe.sort()
    return []
                
def astar(startPos, goalState, v, h):
    if startPos==goalState: return {startPos:0}
    if not isSolvable(startPos, goalState, v, h): return []

    openSet=[(manDist(startPos,goalState,v,h) , startPos, 0)]
    closedSet={} 
    ptr=0
    
    while ptr<len(openSet):
        md, pzl, lvl = openSet[ptr]
        ptr+=1
        
        if pzl in closedSet: continue   
        closedSet[pzl] = lvl
        
        for nbr in neighbors(pzl,v,h):
            if nbr==goalState:
                closedSet[nbr]=closedSet[pzl]+1
                return closedSet

            if nbr in closedSet: continue

            mdn=manDist(nbr,goalState,v,h)
            est=closedSet[pzl]+1+mdn
            openSet.append((est,nbr,closedSet[pzl]+1))
        
        if md == openSet[ptr][0]:
            pass
        else:
            openSet = openSet[ptr:]
            openSet.sort()
            ptr=0
    
        
        
# def find_shortest_path(startPos, goalState, v, h):
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

def displayPath(path, v, h):
    print(path)
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

if args[0]:
    #pl = open(args[0],'r').read().splitlines()
    pl = [args[0]]
    #goalState = pl[0]
    goalState = 'ABCDEFGHIJKLMNO_'
    # newPL = pl[:40]
    otherTime = time.time()
    count=0
    for pzl in pl:
        startTime = time.time()
        dic = astar(pzl,goalState,4,4)
        endTime = time.time()
        if dic:
            print(str(count) + ': ' + pzl + ' solved in ' + str(dic[goalState]) + ' steps in ' + str(endTime-startTime) + ' seconds')
        else:
            print(str(count) + ': ' + pzl + ' solved in ' + 0 + ' steps in ' + str(endTime-startTime) + ' seconds')
        count+=1
# if args[0]=='eckel.txt':
#     pl = open(args[0],'r').read().splitlines()
#     print(pl)
#     goalState = pl[0]
#     newPL = pl[1:]
#     for pzl in newPL:
#         startTime = time.time()
#         dic = astar(pzl,goalState,4,4)
#         endTime = time.time()
#         print(pzl + 'solved in ' + str(len(dic)) + ' steps in ' + str(endTime-startTime))
# if args[0]=='puzzles.txt':
#     wl = open(args[0],'r').read().splitlines()
#     statsCtr = [0]*4
#     puzzleCount = 0
#     solvedPuzzleCount = 0
#     goalState='ABCDEFGHIJKLMNO_'
#     for p in wl:
#         puzzleCount+=1
#         startPos = p
#         newTime = time.time()
#         dimensions = findDimensions(len(startPos))
#         v=dimensions[0]
#         h=dimensions[1]
        
#         processTime = time.time()
#         if not isSolvable(startPos, goalState, v, h):
#             path = []
#             endProcess = time.time()
#         else:
#             path = find_shortest_path(startPos, goalState, v, h)
#             endProcess = time.time()
#             statsCtr[2]+=(len(path)-1)
#             solvedPuzzleCount+=1
#     end = time.time()
#     statsCtr[0]=puzzleCount
#     statsCtr[1]=solvedPuzzleCount
#     statsCtr[2]/=solvedPuzzleCount
#     statsCtr[3]=(end-start)
#     print(statsCtr[0])
#     print(statsCtr[1])
#     print(statsCtr[2])
#     print(statsCtr[3])

# elif len(args)==1:
#     startPos=str(args[0])
#     str1=''
#     for i in range(1,len(startPos)):
#         str1+=str(i)
#     goalState=str1+'_'

#     dimensions = findDimensions(len(startPos))
#     v=dimensions[0]
#     h=dimensions[1]

#     if isSolvable(startPos, goalState, v, h):
#         path = find_shortest_path(startPos, goalState, v, h)
#     else:
#         path = []
#     displayPath(path, v, h)
#     end = time.time()
#     if end-start>=1.0:
#         print(f'Time: {round(end - start,2)}s')
#     else:   
#         print(f'Time: {round(end - start,3)}s')

# else:
#     startPos=str(args[0])
#     goalState=str(args[1])
    
#     dimensions = findDimensions(len(startPos))
#     v=dimensions[0]
#     h=dimensions[1]

#     if isSolvable(startPos, goalState, v, h):
#         path = astar(startPos, goalState, v, h)
#     else:
#         path = []
#     displayPath(path, v, h)
#     end = time.time()
#     if end-start>=1.0:
#         print(f'Time: {round(end - start,2)}s')
#     else:   
#         print(f'Time: {round(end - start,3)}s')

