#Could not find the bug output

memo = []
def combineRouts(a,b,routs):
    global memo
    memo.append(a)
    
    combinedR = []
    for rout in routs:
        if rout[0]==a and rout[1]==b:
            combinedR.append(rout)
        elif rout[1] in memo:
            continue
        elif rout[0]==a:
            newCombined = combineRouts(rout[1],b,routs)
            
            for combined in newCombined:
                combinedR.append([a,b,rout[2]+combined[2],rout[3]+combined[3]])
    
    return combinedR

i = input().split()
n = int(i[1])
m = int(i[2])
hull = int(i[0])

routs = []
for x in range(m):
    y = input().split()
    
    rout = [int(x) for x in y]
    
    routs.append(rout)
    
    rout = [rout[1],rout[0],rout[2],rout[3]]
    
    routs.append(rout)

islands = input().split()
a = int(islands[0])
b = int(islands[1])
combined = combineRouts(a,b,routs)

minT = -1
possible = False
for rout in combined:
    if rout[3] < hull:
        if possible == False:
            possible = True
            minT = rout[2]
        elif rout[2]<minT:
            minT = rout[2]

print(minT)
