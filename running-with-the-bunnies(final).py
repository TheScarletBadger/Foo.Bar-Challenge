import itertools as it
loopalert=0
def djikrow(start,mat):    
    global loopalert
    q = []
    d = {}
    for i in range(0,len(mat)): 
        d[i]=float('inf')
    d[start] = 0
    q.append(start)
    #for i in range(1):
    while len(q)>0:
        #set current position to row with lowest distance
        qdis = [d[n] for n in q]
        cpos = q[qdis.index(min(qdis))]
        cost = mat[cpos]
        #pop current position off queue
        q.pop(q.index(cpos))
        #calculate distance from start to neighbours
        cdis = d[cpos]
        nidx = [n for n in range(len(mat)) if n != cpos]
        for n in nidx:
            ndis = cdis+cost[n]
            #best guess is that if we reach a value of -1000 theres
            #a loop in graph allowing infinite time refils
            if ndis <-1000:
                loopalert = 1
                return
            if ndis<d[n]:
                #add neigbour to q
                q.append(n)
                #update distance to neighbor
                d[n]=ndis
    out = [d[x] for x in range(len(d))]
    return out

def updatemat(mat):
    newmat = []
    for row in range(len(mat)):
        newmat.append(djikrow(row,mat))
        if loopalert ==1:
            return
    return newmat

def getopts(mat):
    #calculate all permutations of all subsets of rows containing rabbits
    options = []
    for sub in range(1,len(mat)-1):
        ss = it.combinations(list(range(1,len(mat)-1)), sub)
        for s in ss:
            p = list(it.permutations(s))
            for p2 in p:
                options.append(list(p2))
                #options.insert(0,list(p2))
    return options

def solution(mat,t):
    mat2 = updatemat(mat)
    if loopalert == 1:
        return [i for i in range(0,len(mat)-2)]
    options = getopts(mat2)
    resc = []
    for o in options:
        tr=t
        o2 = [0] + o + [len(mat2)-1]
        for i in range(0,len(o2)-1):
            st = o2[i]
            ed = o2[i+1]
            tc = mat2[st][ed]
            tr = tr-tc
        #print(tr)
        if tr>=0:
            if len(o)>len(resc):
                resc=sorted([x-1 for x in o])
    return resc


mat = [[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, -10, 0]]

time = 3

print(solution(mat,3))






                