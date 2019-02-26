class Board():
    #Convert list of str into objects
    def __init__(self,board,yLen,xLen):
        self.yLen = yLen
        self.xLen = xLen
        nBoard = [["" for i in range(xLen) ] for j in range(yLen)]
        for y in range(yLen):
            for x in range(xLen):
                if board[y][x] == "W":
                    nBoard[y][x] = Wall()
                elif board[y][x] == "C":
                    activeted = self.activateCam(y,x,board,nBoard,yLen,xLen)
                    board = activeted[0]
                    nBoard = activeted[1]
                    nBoard[y][x] = Wall()
                elif board[y][x] in ["L","R","U","D"]:
                    nBoard[y][x] = Conveyer(y,x,board[y][x])
                elif board[y][x] == ".":
                    nBoard[y][x] = Empty(y,x)
                elif board[y][x] == "X":
                    nBoard[y][x] = Empty(y,x)
                    nBoard[y][x].catch = True
                elif board[y][x] == "S":
                    nBoard[y][x] = Robot((y,x))
                    self.sPos = (y,x)
        self.board = nBoard
    
    #Applies the rules for cameras
    @staticmethod
    def activateCam(y,x,board,nBoard,yLen,xLen):
        posY = 1
        posX = 1
        while y+posY<yLen:
            if board[y+posY][x] == ".":
                board[y+posY][x] = "X"
                nBoard[y+posY][x] = Empty(y+posY,x)
                nBoard[y+posY][x].catch = True
            elif board[y+posY][x] == "W":
                break
            posY += 1
        posY = -1
        while y+posY>=0:
            if board[y+posY][x] == ".":
                board[y+posY][x] = "X"
                nBoard[y+posY][x] = Empty(y+posY,x)
                nBoard[y+posY][x].catch = True
            elif board[y+posY][x] == "W":
                break
            posY -= 1
        while x+posX<xLen:
            if board[y][x+posX] == ".":
                board[y][x+posX] = "X"
                nBoard[y][x+posX] = Empty(y,posX+x)
                nBoard[y][x+posX].catch = True
            elif board[y][x+posX] == "W":
                break
            posX += 1
        posX = -1
        while x+posX>=0:
            if board[y+posY][x] == ".":
                board[y][x+posX] = "X"
                nBoard[y][x+posX] = Empty(y,posX+x)
                nBoard[y][x+posX].catch = True
            elif board[y][x+posX] == "W":
                break
            posX -= 1
        return (board,nBoard)
    
    #Runs for every tile that it can land on
    def activateRobot(self,pos):
        if len(pos) == 0:
            return
        onType = self.board[pos[0][0]][pos[0][1]]
        moves = pos[0][2]
        del pos[0]
        paths = pos
        
        if onType.type == "E":
            onType.minV = moves
            onType.v = True
            if onType.catch == True:
                onType.minV = -1
                return
        types = self.checkNear(onType.pos[0],onType.pos[1])
        
        for t in range(len(types)):
            if types[t] != "":
                if types[t].type not in ["W",""] and types[t].pos not in paths:
                    if types[t].type == "E":
                        if types[t].v == False:
                            paths.append((types[t].pos[0],types[t].pos[1],moves+1))
                    elif types[t].type == "C" and self.canMove(self.board[types[t].pos[0]][types[t].pos[1]],types[t].pos[0],types[t].pos[1]):
                        paths.append((types[t].pos[0],types[t].pos[1],moves+1))
        
        if pos in paths:
            paths.remove(pos)

        self.activateRobot(paths)
        return True
    
    #Returns boolean based on if it can move
    def canMove(self,t,y,x):
        if y >= 0 and y < self.yLen and x >= 0 and x < self.xLen:
            if t.type == "C":
                return True
            elif t.type == "E":
                if t.v == False:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    
    #Returns all the adjacent tiles
    def checkNear(self,y,x):
        types = ["","","",""]
        if y+1<self.xLen:
            types[0] = self.board[y+1][x]
        else:
            types[0] = ""
        if y-1>=0:
            types[1] = self.board[y-1][x]
        else:
            types[1] = ""
        if x-1>=0:
            types[2] = self.board[y][x-1]
        else:
            types[2] = ""
        if x+1<self.xLen:
            types[3] = self.board[y][x+1]    
        else:
            types[3] = ""
            
        return types
    
    def output(self):
        for y in self.board:
            for x in y:
                if x.type == "E":
                    print(x.minV)
    
class Empty():
    def __init__(self,y,x):
        self.type = "E"
        self.v = False #If it's visited
        self.catch = False #It the robot would get caught
        self.pos = (y,x) #
        self.minV = -1 #Minimun amount of moves to get to the tile
    def __str__(self):
        return self.type
        
class Conveyer():
    def __init__(self,y,x,d):
        self.type = "C"
        
        #Determines the position that it sends the robot to
        if d == "U":
            self.pos = (y-1,x)
        if d == "D":
            self.pos = (y+1,x)
        if d == "L":
            self.pos = (y,x-1)
        if d == "R":
            self.pos = (y,x+1)        
    def __str__(self):
        return self.type

class Wall():
    def __init__(self):
        self.type = "W"
    def __str__(self):
        return self.type

class Robot():
    def __init__(self,pos):
        self.pos = pos
        self.type = "S"
    def __str__(self):
        return self.type
        
dim = input().split()
i = []
for y in range(int(dim[0])):
    row = input()
    i.append([x for x in row])

board = Board(i,len(i),len(i[0]))

if board.activateRobot([(board.sPos[0],board.sPos[1],0)])==True:
    board.output()