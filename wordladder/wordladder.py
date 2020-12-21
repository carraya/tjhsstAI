import sys; args = sys.argv[1:]
#Christopher Arraya Student, pd.6
wl = set(open(args[0],'r').read().splitlines())
import time;
start = time.time()

### FUNCTIONS ###

def simpleGraphInfo(wl):
    dic={}
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for w in wl:
        dic[w]=[]
        for c in range(6):  
            for l in range(26):
                nw = w[:c] + alpha[l] + w[c+1:]
                if nw in wl and nw!=w:  
                    dic[w].append(nw)
    count=0
    for k in dic:
        count+=len(dic[k])
    ls = [0]
    for k in dic:
        degree = len(dic[k])
        if len(ls)-1<degree:
            ls+=[0]*(degree-(len(ls))+1)
        ls[degree]+=1
    print('Word count: ' + str(len(wl)))
    print('Edge count: ' + str(count//2))    
    print('Degree list: ' + ' '.join(map(str,ls)))
    return dic

graph = simpleGraphInfo(wl)

def degreeList(dic):
    ls = [0]
    for k in dic:
        degree = len(dic[k])
        if len(ls)-1<degree:
            ls+=[0]*(degree-(len(ls))+1)
        ls[degree]+=1
    return ls

def secondDegree(dic):
    count=0
    dl=degreeList(graph)
    for k in dic:
        degree = len(dic[k])
        if degree==len(dl)-2 and count==0:
            return k
    return None
    
def pathFromRootToGoal(dctSeen, start, end):
    path=[] 
    parseMe=[goal]
    while parseMe:
        item = parseMe.pop(0)
        if item == '': return path[::-1]
        parseMe.append(dctSeen[item])
        path.append(item)
    return []
    
def find_shortest_path(start, end):
    dctSeen = {start: ''}
    parseMe = [start]
    while parseMe:
        prnt = parseMe.pop(0)
        if prnt==end: return pathFromRootToGoal(dctSeen, start, end)
        for n in graph[prnt]:
            if n not in dctSeen:   
                parseMe.append(n) 
                dctSeen[n] = prnt
    return []

def mark(recur, k, visited):
    visited[k]=True
    recur.append(k)
    for i in graph[k]:
        if visited[i]==False:
            recur=mark(recur,i,visited)
    return recur

def ccList():
    visited={}
    sizes={}
    kValues={2:0, 3:0, 4:0}
    for k in graph:
        visited[k]=False
    for k in graph:
        if visited[k]==False:
            recur=[]
            component = mark(recur, k, visited)
            sizes[len(component)]='1'
            if len(component)==2:
                kValues[2]+=1
            elif len(component)==3:
                edges=0
                for n in graph[k]:
                    edges+=1
                    for nn in graph[n]:
                        edges+=1
                if edges==6:
                    kValues[3]+=1
            elif len(component)==4:
                edges=0
                for n in graph[k]:
                    edges+=1
                    for nn in graph[n]:
                        edges+=1
                if edges==12:
                    kValues[4]+=1
    print('Connected component size count: ' + str(len(sizes)))
    print('Largest component size: ' + str(max(sizes)))
    print('K2 count: ' + str(kValues[2]))
    print('K3 count: ' + str(kValues[3]))
    print('K4 count: ' + str(kValues[4]))

def farthest(root):
    parseMe=[root]
    path=[]
    while parseMe:
        prnt=parseMe.pop(0)
        for n in graph[prnt]:
            if n not in path:
                parseMe.append(n)
                path.append(n)
    return path[-1]

### CMD-LINE ARGS ###

if len(args)==1: 
    end = time.time()
    print(f"Construction time: {round(end - start,3)}s")
else:
    end = time.time()
    print(f"Construction time: {round(end - start,3)}s")
    root = args[1]; goal = args[2] 
    print('Second degree word: ' + secondDegree(graph))
    ccList()
    print('Neighbors: ' + str(graph[root]))
    print('Farthest: ' + str(farthest(root)))
    print('Path: ' + str(find_shortest_path(root,goal)))