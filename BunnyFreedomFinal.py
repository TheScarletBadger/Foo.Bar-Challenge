import numpy as np

def makeuniverses(matrix):
    matrix=np.asarray(matrix)
    walls = matrix.nonzero()
    universes = [matrix]
    for i in range(0,len(walls[0])):
        u = np.copy(matrix)
        u[walls[0][i],walls[1][i]] = 0
        universes.append(u)
    return universes

def qkey(mapmat):
    #get dimensions of map
    nrow = len(mapmat)
    ncol = len(mapmat[0])
    #initialize queue (open) list
    q={}
    #initialize key number of bottom right node
    endkey = []
    #end position coordinates
    endpos = (nrow-1,ncol-1)
    #node counter (used to uniquely identify node)
    n = 0
    for r in range(0,nrow):
        for c in range(0,ncol):
            if mapmat[r,c] == 0:
                #manhattan distance to end
                h = (endpos[0]-r)+(endpos[1]-c)
                #node row = 0.position, 1.g, 2.h, 3.parent
                q[n]=([(r,c),r+c,h,[]])
                if (r,c) == endpos:
                    endkey = n        
                n=n+1
    return q,endkey


def astar(mapmat):
    mapmat = np.asarray(mapmat)
    #pile contains initial state of all nodes
    pile,endkey = qkey(mapmat)
    #set source node distance to 1
    pile[0][1] = 1
    #open: initially contins only source node
    op={}
    op[0]=pile[0]
    #closed: initially empty
    cl = {}
    x =1
    #while x==1:
    while len(op)>0:
        #find node in open with lowest f score
        flist = []
        klist = []
        for key in op.keys():
            klist.append(key)
            flist.append(op[key][1]+op[key][2])
        cnodekey = klist[flist.index(min(flist))]
        if cnodekey==endkey:
            x=2
        #list of valid coordinates to check if neighbours exist
        plist = []
        klist = []
        for key in pile.keys():
            klist.append(key)
            plist.append(pile[key][0])
        #make current node and move to closed list
        node=op.pop(cnodekey)
        cl[cnodekey] = node
        cpos = node[0]
        cg = node[1]
        #generate list of neigbours
        ncords = [(cpos[0],cpos[1]+1),(cpos[0],cpos[1]-1),(cpos[0]+1,cpos[1]),(cpos[0]-1,cpos[1])]
        for n in ncords:
            #check if neighbour coordinates are valid
            if n in plist:
                nnodekey = klist[plist.index(n)]
                if nnodekey in op.keys():
                    nnode = op[nnodekey]
                    oldf = nnode[1]+nnode[2]
                    newf = (cg+1) + nnode[2]
                    if newf<oldf:
                        nnode[3]=cnodekey
                        nnode[1]=cg+1
                        op[nnodekey]=nnode
                        
                elif nnodekey in cl.keys():
                    nnode = cl[nnodekey]
                    oldf = nnode[1]+nnode[2]
                    newf = (cg+1) + nnode[2]
                    if newf<oldf:
                        nnode[3]=cnodekey
                        nnode[1]=cg+1
                        cl[nnodekey]=nnode
                        
                else:
                    newnode = pile[nnodekey]
                    newnode[1]=cg+1
                    newnode[3]=cnodekey
                    op[nnodekey]=newnode
                    
    if x==2:              
        return int(cl[endkey][1])
    else:
        return int(1000)


def solution(mapmat):
    universe = makeuniverses(mapmat)
    distlist = []
    for u in universe:
        dist = astar(u)
        distlist.append(dist)
    
    return int(min(distlist))


mapmat = np.zeros((20,20))
mapmat[10]=1
print(solution(mapmat))