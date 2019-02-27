#Complete but slow solution
nQ = int(input())

n = int(input())

dmojS = input().split()
dmojS = [int(x) for x in dmojS]
pegS = input().split()
pegS = [int(x) for x in pegS]

dmojS.sort()
pegS.sort()

if nQ == 2:
    pegS.reverse()

s = 0
for x in range(n):
    s += max(dmojS[x],pegS[x])

print(s)