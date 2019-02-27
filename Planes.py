import random

g = int(input())
p = int(input())
n = int(input())
nPlanes = 1
canDock = True
dockedS = [n]
m = 1
l = 1

for x in range(p-1):
    n = int(input())
    if canDock == True:
        if m < n:
            m = n
        
        a = 0
        b = l-1
        randPos = random.randint(a,b)
            
        if dockedS[randPos] == randPos:
            break
        elif dockedS[randPos] > randPos:
            a = randPos
        else:
            b = randPos
        while a != b:
            randPos = random.randint(a,b)
            
            if dockedS[randPos] == randPos:
                break
            elif dockedS[randPos] > randPos:
                a = randPos
            else:
                b = randPos
        
        dockedS.insert(randPos,n)
        l += 1
        
        planes = 0
        for d in dockedS:
            if planes >= d:
                canDock = False
                break
            else:
                planes += 1
        if canDock == True:
            nPlanes += 1

print(nPlanes)