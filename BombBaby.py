#final version

def loopyloo(z):
    loop = 0
    while max(z)%min(z)!=0:
        big,small = max(z),min(z)
        loop = loop+(big//small)
        big = big%small
        if z[0]>z[1]:
            z=(big,small)
        else:
            z=(small,big)
        
    while z!=(1,1):
        big,small = max(z),min(z)
        if(sum(z)<=0) or big==small:
            return 'impossible'
        
        if small==1:
            loop = loop+big-1
            return str(loop)

        if z[0]>z[1]:
            z=(z[0]-z[1],z[1])
        else:
            z=(z[0],z[1]-z[0])
        loop = loop+1
    return str(loop)

def solution(x,y):
    x=int(x)
    y=int(y)
    target = (x,y)

    #use shortcuts if possible
    if x==y:
        return 'impossible'
    if sum([x,y])>3:
        if x%y==0 or y%x==0:
            return 'impossible'

    return loopyloo(target)


