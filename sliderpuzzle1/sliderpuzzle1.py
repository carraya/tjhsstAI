import sys; args = sys.argv[1:]
#Christopher Arraya Student, pd.6
startPos=str(args[0])
if len(args)==1:
    str1=''
    for i in range(1,len(startPos)):
        str1+=str(i)
    goalState=str1+'_'
else:
    goalState=str(args[1])
import time;
start = time.time()

length = len(startPos)

def findDimensions():
    f=1
    l=length
    i=0
    while f < l:
        i += 1
        if length % i == 0:
            f = i
            l =length//f
    
    return [l, f]

dimensions = findDimensions()
v=dimensions[0]
h=dimensions[1]

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
    
def pathFromRootToGoal(dctSeen, start):
    path=[] 
    parseMe=[goalState]
    while parseMe:
        item = parseMe.pop(0)
        if item == '': return path[::-1]
        parseMe.append(dctSeen[item])
        path.append(item)
    return []

def find_shortest_path():
    dctSeen = {startPos: ''}
    parseMe = [startPos]
    while parseMe:
        prnt = parseMe.pop(0)
        if prnt==goalState: return pathFromRootToGoal(dctSeen, start)
        for n in neighbors(prnt, v, h):
            if n not in dctSeen:   
                parseMe.append(n) 
                dctSeen[n] = prnt
    return []

path = find_shortest_path()

def displayPath():
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

displayPath()
end = time.time()
if end-start>=1.0:
    print(f"Time: {round(end - start,2)}s")
else:   
    print(f"Time: {round(end - start,3)}s")