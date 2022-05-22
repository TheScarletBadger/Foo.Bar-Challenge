import itertools as it
loopalert=0

#Here I use a slightly wonky implementation of Djikstras algorithm to convert a row of the
#original transition cost matrix into a new one which indicates the shortest route
#between rows (even if its a multi-hop)
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
            #Something I didn't account for was the possibility that the original graph contains
            #a negative cost loop allowing infinite time refils. This is my crude method of detecting
            #one and if one is detected simply reporting that we can rescue all bunnies.
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

#function uses the one above and iterates over rows to create an updated transition cost matrix
def updatemat(mat):
    newmat = []
    for row in range(len(mat)):
        newmat.append(djikrow(row,mat))
        if loopalert ==1:
            return
    return newmat

#calculate all permutations of all subsets of rows containing rabbits. These are the
#various groups we can attempt a rescue and the orders we can try visiting them in
def getopts(mat):
    options = []
    for sub in range(1,len(mat)-1):
        ss = it.combinations(list(range(1,len(mat)-1)), sub)
        for s in ss:
            p = list(it.permutations(s))
            for p2 in p:
                options.append(list(p2))
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






                
