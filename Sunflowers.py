def check(table):
    for x in table:
        prev = x[0]
        for y in x:
            if y < prev:
                return False
            else:
                prev = y
    for y in range(len(table)):
        for x in range(len(table)):
            if x != 0:
                if table[x][y] < table[x-1][y]:
                    return False
    return True

n = int(input())
data = []
for x in range(n):
    i = input().split()
    ints = [int(x) for x in i]
    data.append(ints)

count = 0
while check(data) == False and count <= 3:
    rotate = []
    for x in range(n):
        rRange = []
        for y in range(n-1,-1,-1):
            rRange.append(data[y][x])
        rotate.append(rRange)
    data = rotate
    count += 1
if count <= 3:
    for y in data:
        for x in y:
            print(x, end= " ")
        print()
