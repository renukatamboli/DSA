# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def __init__(self):
        self.visited = {}
        self.dir = [(0,-1),(-1,0),(0,1),(1,0)]
        
    def goBack(self,robot):
        robot.turnRight()
        robot.turnRight()
        robot.move()
        robot.turnRight()
        robot.turnRight()
    
    def backtrack(self,row, col,d, robot):
        self.visited[(row,col)] = True
        robot.clean()
        
        for i in range(4):
            newD = (i+d) % 4
            newRow = row + self.dir[newD][0]
            newCol = col + self.dir[newD][1]
            
            if (newRow,newCol) not in self.visited and robot.move():
                self.backtrack(newRow, newCol, newD,robot)
                self.goBack(robot)
            
            robot.turnRight()
                
            
        
    def cleanRoom(self, robot):
        self.backtrack(0,0,0,robot)
        """
        :type robot: Robot
        :rtype: None
        """
        
