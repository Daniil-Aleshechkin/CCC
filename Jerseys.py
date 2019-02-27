#
sizes = ["L","M","S"]

nJ = int(input())
nA = int(input())

jerseys = {}
for x in range(nJ):
    size = input()
    
    jerseys[str(x+1)] = size

aths = {}
for x in range(nA):
    ath = input().split()
    
    if ath[1] in aths:
        l = aths[ath[1]]
        l.append(ath[0])
        aths[ath[1]] = l
    else:
        aths[ath[1]] = [ath[0]]

requests = 0
for ath in aths:
    l = aths[ath]
    
    for size in l:
        if sizes.index(size) >= sizes.index(jerseys[ath]):
            requests += 1
            break

print(requests)
