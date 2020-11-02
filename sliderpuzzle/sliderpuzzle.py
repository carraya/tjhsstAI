import sys; args = sys.argv[1:]
#Christopher Arraya Student, pd.6
import time; import random;
start = time.time()

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

def bfs(startPos, goalState, v, h):
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

def manDistOrig(pzl, goal, v, h):
    s=0
    e=0
    manCount=0
    for i in pzl:
        if i=='_':
            pass
        else:
            s=pzl.index(i)
            e=goal.index(i)
            manCount += (abs((s//v)-(e//v)) + abs((s%h)-(e%h)))
    return manCount

def manDist(pzl, prev, goal, v, h, nPos):
    s=0
    e=0
    d=0
    i = prev[nPos] #save the position of the moved piece in the parent
    s=pzl.index(i) #find where the moved piece is now
    e=goal.index(i) #find where the moved piece should be
    manCountPzl=(abs((s//v)-(e//v)) + abs((s%h)-(e%h))) #calculate manhattan distance for that one piece in the neighbor
    d=nPos #position of the moved piece in parent
    manCountPrev=(abs((d//v)-(e//v)) + abs((d%h)-(e%h))) #calculate manhattan distance for that one piece in the parent
    return manCountPzl-manCountPrev #find the difference

def astar(startPos, goalState, v, h):
    if startPos==goalState: return {startPos:0} #check if its already solved
    if not isSolvable(startPos, goalState, v, h): return [] #check if solvable
    origMD = manDistOrig(startPos,goalState,v,h) #the only time i calculate full manhattan distance
    openSet={origMD:[(origMD, startPos, 0, startPos.find('_'), -1, '')]} #create openSet with md as key and tuple of md, current pzl, level, underscore position, and position of moved piece in grandparent
    closedSet={} #store pzl:level in here
    ptr1=origMD #pointer for the keys in openSet
    ptr2=0 #pointer for which tuple in the key of the openSet
    
    while openSet:
        if len(openSet[ptr1]) > ptr2:#check if there are still tuples left at this key, if there is keep going
            pass
        else: #find the next f-value in openSet
            ptr1+=1
            ptr2=0
            while(ptr1 not in openSet):
                ptr1+=1
        md, pzl, lvl, uPos, gpuPos, myMove = openSet[ptr1][ptr2] 
        ptr2+=1 #use next tuple next iteration
        pzlLst, pPos = [*pzl], uPos #create a list of the characters of pzl and make the prior position the current underscore position
        
        if pzl in closedSet: continue   #if the pzl is already in closed set, then keep going, otherwise add to closed set with level
        closedSet[pzl] = lvl
        
        for nPos in NBRPOS[uPos]: #calculate the swaps possible from the current position of the underscore
            if nPos == gpuPos: continue #if we already have been at that neighbor, then don't even bother
            pzlLst[pPos], pzlLst[uPos], pzlLst[nPos], pPos = pzlLst[uPos], pzlLst[nPos], pzlLst[pPos], nPos #swap the pieces that the lookup table provided
            nbr = ''.join(pzlLst) #make it back into a string
            move = myMove
            if nPos-4==uPos: move+='D'
            elif nPos+4==uPos: move+='U'
            elif nPos-1==uPos: move+='R'
            elif nPos+1==uPos: move+='L'
            if nbr==goalState: #check if the nbr is the solution, if it is add it to closed set and now we are done
                closedSet[nbr]=closedSet[pzl]+1
                return closedSet

            if nbr in closedSet: continue #check if the neighbor is already in closedset, if it is then just skip the iteration
            
            mdn=manDist(nbr,pzl,goalState,v,h, nPos)+md #calculate manhattandistance for the one piece that moved and add it to md to see if it went down or up
            est=closedSet[pzl]+1+mdn #level plus mdn
            if est in openSet: #if est is already in openSet then just append the new tuple of the neighbor
                openSet[est].append((mdn,nbr,closedSet[pzl]+1, nPos, uPos, move))
            else: #else make a new key of est and add the tuple of the neighbor
                openSet[est] = [(mdn,nbr,closedSet[pzl]+1, nPos, uPos, move)]

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
                        print(i[(len(i)//v)*j:(len(i)//v)*(j+1)], end='     ')
                print('')
            print('')

    print('Steps: ' + str(len(path)-1))

if len(args)==0:
    global NBRPOS
    goalState = '12345678_'
    statsCtr = [0]*5
    ls=['1','2','3','4','5','6','7','8','_']
    solvedPuzzleCount = 0
    for i in range(500):
        shuffledList = list(random.sample(ls[:], len(ls)))
        startPos = ''.join(shuffledList)
        newTime = time.time()
        dimensions = findDimensions(len(startPos))
        w=dimensions[0]
        h=dimensions[1]
        NBRPOS = [({i+w,i-w,i-(i%w>0),i+((i+1)%w>0)} & {*range(len(startPos))}) - {i} for i in range(len(startPos))]
        
        processTime = time.time()
        if not isSolvable(startPos, goalState, w, h):
            path = []
            endProcess = time.time()
            statsCtr[1]+=(endProcess-processTime)
            statsCtr[2]+=1
        else:
            path = bfs(startPos, goalState, w, h)
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
    
elif args[0][-4:] == '.txt' and args[1] == 'astar':
    pl = open(args[0],'r').read().splitlines()
    goal = pl[0]
    h = findDimensions(len(goal))[0]
    w = findDimensions(len(goal))[1]
    count = 0
    for pzl in pl:
        startTime = time.time()
        NBRPOS = [({i+w,i-w,i-(i%w>0),i+((i+1)%w>0)} & {*range(len(pzl))}) - {i} for i in range(len(pzl))]
        dic = astar(pzl,goal,4,4)
        endTime = time.time()
        print(str(count) + ': ' + pzl + ' solved in ' + str(dic[goal]) + ' steps in ' + str(endTime-startTime) + ' seconds')
        count+=1

elif args[0][-4:] == '.txt' and args[1] == 'bfs':
    pl = open(args[0],'r').read().splitlines()
    goal = pl[0]
    h = findDimensions(len(goal))[0]
    w = findDimensions(len(goal))[1]
    count = 0
    for pzl in pl:
        startTime = time.time()
        NBRPOS = [({i+w,i-w,i-(i%w>0),i+((i+1)%w>0)} & {*range(len(pzl))}) - {i} for i in range(len(pzl))]
        dic = bfs(pzl,goal,4,4)
        endTime = time.time()
        print(str(count) + ': ' + pzl + ' solved in ' + str(len(dic)-1) + ' steps in ' + str(endTime-startTime) + ' seconds')
        count+=1

elif len(args)==1:
    startPos=str(args[0])
    str1=''
    for i in range(1,len(startPos)):
        str1+=str(i)
    goalState=str1+'_'
    dimensions = findDimensions(len(startPos))
    w=dimensions[0]
    h=dimensions[1]
    NBRPOS = [({i+w,i-w,i-(i%w>0),i+((i+1)%w>0)} & {*range(len(startPos))}) - {i} for i in range(len(startPos))]
    if isSolvable(startPos, goalState, w, h):
        path = bfs(startPos, goalState, w, h)
    else:
        path = []
    displayPath(path, w, h)
    end = time.time()

else:
    startPos=str(args[0])
    goalState=str(args[1])
    
    dimensions = findDimensions(len(startPos))
    w=dimensions[0]
    h=dimensions[1]
    NBRPOS = [({i+w,i-w,i-(i%w>0),i+((i+1)%w>0)} & {*range(len(startPos))}) - {i} for i in range(len(startPos))]
    if isSolvable(startPos, goalState, w, h):
        path = bfs(startPos, goalState, w, h)
    else:
        path = []
    displayPath(path, w, h)
    end = time.time()


if end-start>=1.0:
    print(f"Time: {round(end - start,2)}s")
else:   
    print(f"Time: {round(end - start,3)}s")