import fractions
import numpy as np

matrix = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]]

#function to convert to a stochastic matrix
def formatinput(inmat):
    finput = []
    nrow = len(inmat)
    for i in range(0,nrow):
        row = inmat[i]
        if sum(row)==0:
            row[i]=1
        else:
            row = [float(x) / sum(row) for x in row]
        finput.append(row)
    return finput

def flipflop(matrix):
    terminal = []
    transient = []
    terminalkey = []
    transientkey = []
    for i in range(0,len(matrix)):
        if sum(matrix[i])==0:
            terminal.append(matrix[i])
            terminalkey.append(i+1)
        else:
            transient.append(matrix[i])
            transientkey.append(i+1)
    matrix = transient + terminal
    key = transientkey + terminalkey
    colkey = [x for _, x in sorted(zip(key, list(range(0,len(matrix)))))]
    for i in range(0,len(matrix)):
        matrix[i] = [x for _, x in sorted(zip(colkey, matrix[i]))]
    return matrix

def solution(matrix):
    if sum(matrix[0])==0:
        return [1,1]
    tstates = len(matrix)-list(map(sum, matrix)).count(0)
    if list(map(sum, matrix)).count(0) == 1:
        return [1,1]
    matrix=flipflop(matrix)
    P = np.asarray(formatinput(matrix))
    
    Q = P[:tstates,:tstates]
    R = P[:tstates,tstates:]
    I = np.identity(tstates)
    N=np.subtract(I,Q)
    N=np.linalg.inv(N)
    B = np.matmul(N,R)
    B=B[0]
    B=[fractions.Fraction(r).limit_denominator() for r in B]
    L = [fr.denominator for fr in B]
    lcm = 1
    for i in L:
        lcm = lcm*i//fractions.gcd(lcm, i)
    B = [int(fr.numerator * lcm / fr.denominator) for fr in B]
    B.append(lcm)
    
    return B



print(solution(matrix))