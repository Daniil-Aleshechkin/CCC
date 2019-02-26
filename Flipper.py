grid = [[1,2],[3,4]]

instructions = input()

for i in instructions:
    if i == "V":
        flipGrid = []
        for line in grid:
            line.reverse()
            flipGrid.append(line)
        grid = flipGrid
    else:
        grid.reverse()

for line in grid:
    for x in line:
        print(x, end = " ")
    print()