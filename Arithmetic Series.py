#From the 2019 competition
#I've made a simple solution that will only work if every 'X' could be solved on each row i.e. rows with only one 'X'

def printGrid(grid):
    for y in grid:
        for x in y:
            print(x, end = " ")
        print()
def rotate(grid):
    newGrid = []
    for x in range(2,-1,-1):
        newLine = []
        for y in range(3):
            newLine.append(grid[y][x])
        newGrid.append(newLine)
    
    return newGrid

def rotateBack(grid):
    newGrid = []
    for x in range(3):
        newLine = []
        for y in range(2,-1,-1):
            newLine.append(grid[y][x])
        newGrid.append(newLine)
    return newGrid

def solveSeries(series,posX):
    if posX == 0:
        d = series[2]-series[1]
        newSeries = [series[1]-d,series[1],series[2]]
    elif posX == 1:
        d = int((series[2]-series[0])/2)
        newSeries = [series[0],series[0]+d,series[2]]
    else:
        d = series[1]-series[0]
        newSeries = [series[0],series[1],series[1]+d]
    return newSeries

grid = []

for y in range(3):
    line = input().split()
    newLine = []
    
    for x in line:
        if x != "X":
            newLine.append(int(x))
        else:
            newLine.append(x)
    
    grid.append(newLine)

printGrid(grid)
yPos = 0
for y in grid:
    nXs = 0
    pos = 0
    for x in y:
        if x == "X":
            xPos = pos
            nXs += 1
        pos += 1
    
    if nXs == 1:
        line = solveSeries(y,xPos)
    else:
        line = y
    
    grid[yPos] = line
    
    yPos += 1

rotateGrid = rotate(grid)

yPos = 0
for y in rotateGrid:
    nXs = 0
    pos = 0
    for x in y:
        if x == "X":
            xPos = pos
            nXs += 1
        pos += 1
    
    if nXs == 1:
        line = solveSeries(y,xPos)
    else:
        line = y
    
    rotateGrid[yPos] = line
    yPos += 1

printGrid(rotateBack(rotateGrid))
print(rotateBack(rotateGrid))
