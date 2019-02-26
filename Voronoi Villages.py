def midPoint(a,b):
    return((b-a)/2+a)

nVillages = int(input())
villLocations = []

for x in range(nVillages):
    villLocations.append(float(input()))

villLocations.sort()

pos = 0
neighBound = []
for l in villLocations:
    if pos != len(villLocations)-1:
        neighBound.append(midPoint(l,villLocations[pos+1]))
    pos += 1

pos = 0
for n in neighBound:
    if pos == 0:
        smallest = neighBound[pos+1]-n
    if pos != len(neighBound)-1:
        midPoint = neighBound[pos+1]-n
        if midPoint < smallest:
            smallest = midPoint
    pos += 1
print(smallest)