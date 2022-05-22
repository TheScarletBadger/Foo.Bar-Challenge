#If anyone reads these, you should know that I would not in all honesty have 
#managed to do this without cracking and reading another's solution
#https://medium.com/@chris.bell_/google-foobar-as-a-non-developer-level-5-a3acbf3d962b
#While the code is my own (with exception of the integer partitions function)
#the method implemented is very much as per the blog above so I do not really 
#deserve credit here.

import math
import numpy

#Function not my own
#https://jeromekelleher.net/generating-integer-partitions.html
def accel_asc(n):
    a = [0 for i in range(n + 1)]
    k = 1
    y = n - 1
    while k != 0:
        x = a[k - 1] + 1
        k -= 1
        while 2 * x <= y:
            a[k] = x
            y -= x
            k += 1
        l = k + 1
        while x <= y:
            a[k] = x
            a[l] = y
            yield a[:k + 2]
            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        yield a[:k + 1]

#Conjugacy class size calculation with wildly liberal use of long integers
def ccs(p):
    u = list(numpy.unique(p))
    denom = long(1)
    for i in u:
        e = p.count(i)
        denom = denom*long(((i**e)*long(math.factorial(e))))
    return long(math.factorial(sum(p))/denom) 


#From a-googlin around it seems I knew I needed to use Burnsides Lemma in order to find
#the number of non-equivalent ways to 'color' a WxH matrix of s colors (states)
    
def solution(w,h,s):
    
    #Magnitude of G is the product of possible row and column permutations 
    G=math.factorial(w)*math.factorial(h)
    
    #Integer partitions the of number of rows (hp) and columns (wp)
    hp = list(accel_asc(h))
    wp = list(accel_asc(w))
    
    output = long(0)
    #Sum greatest common divisors in all cominations of elements in wp and hp
    for wi in wp:
        cw = long(ccs(wi))
        for hi in hp:
            hw = long(ccs(hi))
            e=long(0)
            for wii in wi:
                for hii in hi:
                    e=e+long(numpy.gcd(wii,hii))
            #product of conjugacy class sizes of row and column partitions
            conjprod = long(cw*hw)
            output = output + long((conjprod * (s**e)))
    #took me a disturbingly long time to notice answer was to be returned as a
    #string rather than an integer
    return str(long(output // G))

print(solution(2,2,2))
