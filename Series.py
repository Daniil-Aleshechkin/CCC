#From 2019 competition
#Incomplete due to time
nk = input().split()

n = int(nk[0])
k = int(nk[1])

i = [int(x) for x in input().split()]


l = i[:k]
r = i[len(i)-k:]
l.sort()
r.sort()
l.reverse()
r.reverse()

if l[0]==r[0]:
    if l[1]>=r[1]:
        m = l[1]+r[0]
else:
    m = l[0]+r[0]

print(m)