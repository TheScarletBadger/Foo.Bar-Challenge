#Final version
from itertools import combinations as combi

def solution(n,k):
    #The cap on number of each key type (kcap) in circulation is given by n-(k-1)
    kcap = n-(k-1)
    
    #lets make a matrix giving all posible ways of sampling kcap from a vector of length n.
    subsets = list(combi(list(range(0,n)),kcap))
    
    #initialize an empty matrix to hold the key distribution
    scheme = [[] for x in range(0,n)]
    
    #in 'subsets' row indices are key type names and elements are rabbit names
    #so we just need to do the old switcharoo
    for r in range(0,len(subsets)):
        subsrow = subsets[r]
        for c in range(0,len(subsrow)):
            rabbit = subsets[r][c]
            keytype = r
            scheme[rabbit].append(keytype)

    return scheme

