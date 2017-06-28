# Queen's Attack II
import sys

class chess(object):
    BLANK = 'Blank'
    OBSTACLE = 'Obstacle'
    QUEEN = 'Queen'
    QUEEN_MOVE = 'Yes'
    board = []
    qm_count = 0

    def setup_board(self,size):
        print("Setup Board")
        #board = [ ( (i,j) for i in range(size) ) for j in range(size) ]
        for i in range(size):
            row = []
            for j in range(size):
                row.append(self.BLANK)
            self.board.append(row)
        print(self.board)
                
    def add_obstacle(self,x,y):
        print("Added Obstacle")
        self.board[x][y] = self.OBSTACLE

    def add_queen(self,x,y):
        print("Added Queen")
        self.board[x-1][y-1] = self.QUEEN    

    def set_queen_moves(self,r,c):
        r1 = r-1
        c1 = c-1
        n = len(self.board)
        print("Setup Queen Moves")
        print("r1=",r1," c1=",c1," n=",n)
        
        # Fix the values in the current row
        for i in range(n):
            if i != c1:
                self.board[r1][i] = self.QUEEN_MOVE
                
        # Fix the values in the current column
        for j in range(n):
            if j != r1:
                self.board[j][c1] = self.QUEEN_MOVE
                
        # Fix the diagnal values
        if c > 0 and r > 0:
            for i in range(0,c1):
                self.board[r1-i][c1-i] = self.QUEEN_MOVE
                
        if r < n and c < n:
            for i in range(c1+1,n):
                self.board[r1+i][c1+i] = self.QUEEN_MOVE

        #self.add_queen(r1,c1)

    def count_queen_moves(self):            
        # Count the True to get the possible moves
        print("Count Queen Moves")
        n = len(self.board)
        for i in range(n):
            for j in range(n):
                if self.board[i][j] == self.QUEEN_MOVE:
                    self.qm_count += 1
        #return count

    def print_board(self):
        print("Print Board")
        n = len(self.board)
        for i in range(n):
            print(self.board[i])

c = chess()
n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
                    
rQueen,cQueen = input().strip().split(' ')
rQueen,cQueen = [int(rQueen),int(cQueen)]

c.setup_board(n)
print("board = ",c.board)
board = c.set_queen_moves(rQueen,cQueen)
board = c.add_queen(rQueen,cQueen)

for a0 in range(k):
    rObstacle,cObstacle = input().strip().split(' ')
    rObstacle,cObstacle = [int(rObstacle),int(cObstacle)]
    # your code goes here
    c.add_obstacle(rObstacle,cObstacle)

c.count_queen_moves()
print("Queen moves=",c.qm_count)
c.print_board()
