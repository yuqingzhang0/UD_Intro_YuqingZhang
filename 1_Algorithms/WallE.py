import math, pygame
from math import pi

# This is the Wall-E class
class WallE:
    def turn(self, angle):
        x = self.direction[0]
        y = self.direction[1]
        self.direction = [int(x*math.cos(angle)-y*math.sin(angle)),
                            int(x*math.sin(angle)+y*math.cos(angle))]
        self.image = self.imageDict[str(self.direction)]


    #Function that turns Wall-E 90 degrees to the right
    def turn_right(self):
        self.turn(0.5*pi)

    #Function that turns Wall-E 90 degrees to the left
    def turn_left(self):
        self.turn(-0.5*pi)

    #Function that returns true if Wall-E stands on a box
    def check_on_box(self):
        if self.board[self.position[0]][self.position[1]] == 2:
            return True
        else:
            return False

    #Function that returns true if Wall-E stands in front of a wall
    def check_wall(self):
        x = self.position[0] + self.direction[0]
        y = self.position[1] + self.direction[1]
        if -1 < x < len(self.board) and -1 < y < len(self.board[0]):
            if self.board[x][y]==1:
                return True
            return False
        else:
            return True

    #Function that picks up a box - it breaks Wall-E if you try to pick up a box
    #that isn't there!
    def pick_up_box(self):
        if self.board[self.position[0]][self.position[1]] == 2:
            self.board[self.position[0]][self.position[1]] = 0
        else:
            self.broken = True

    #Function that drops a box - it breaks Wall-E if you try to drop a box on top
    #of another box!
    def drop_box(self):
        if self.board[self.position[0]][self.position[1]] == 0:
            self.board[self.position[0]][self.position[1]] = 2
        else:
            self.broken = True

    #Function that makes Wall-E takes one step forward. It breaks Wall-E if you
    #try to take 2 steps at once!
    def move(self):
        if not self.action:
            self.position[0] += self.direction[0]
            self.position[1] += self.direction[1]
            if -1 < self.position[0] < len(self.board) and -1 < self.position[1] < len(self.board[0]):
                if self.board[self.position[0]][self.position[1]]==1:
                    self.broken = True
            else:
                self.broken = True
            self.action = True
        else:
            self.broken = True

    # Initialisation function of Wall-E Class
    def __init__(self, position, board, image):
        self.position = position
        self.board = board
        self.direction = [1,0]
        self.image = image
        il = pygame.transform.flip(self.image, True, False)
        ir = pygame.transform.rotate(self.image, 0)
        id = pygame.transform.rotate(self.image, -90)
        iu = pygame.transform.rotate(self.image, 90)
        self.imageDict = {'[1, 0]':ir, '[-1, 0]':il, '[0, 1]':id, '[0, -1]':iu}
        self.action = False
        self.broken = False

        # DO NOT CHANGE ANYTHING ABOVE THIS LINE!!!!!
        #-----------------------------------------------------------------------
        # Declare variables you need here (Please formulate these variables
        # in ALL CAPS to avoid clashes with existing variable!!!)
        # and make sure they are at this indent level

        self.TURNS = 0
        self.WALKING_TO_OBSTACLE = False
        self.BOX_OBTAINED = False
        self.WALL_Y = True
        
    # Declare any help functions here (also use all caps for these!!), it has to include self in the argument.
    # and make sure they are at this indent level
    def DROP_PICK_UP(self):
        if self.check_on_box() == True:
            self.pick_up_box()
        else:
            self.drop_box()
            
    def CHECK_WALL_Y(self):
        self.turn_left()
        self.WALL_Y = self.check_wall()
        if self.WALL_Y == True:
            self.turn_right()
        else:
            self.turn_left()
        return self.WALL_Y

    # These are the 5 functions you have to fill in
    def walk_back_and_forth(self):
        if self.check_wall() == False:         
            self.move()
            
        else:
             if self.TURNS == 0:
                self.turn_right()
                self.turn_right()
                self.TURNS += 1
                self.move()
             
    def walk_a_lap(self):
        if self.check_wall() == False:
            self.move()
        else:
            if self.TURNS < 3:
                self.turn_right()
                self.TURNS += 1
                self.move()
                    
        pass #Remove this and fill with your own code

    def find_the_box(self):
        if not self.BOX_OBTAINED:
            if self.check_on_box() == True:
                    self.pick_up_box()
                    self.BOX_OBTAINED = True
            if self.check_wall() == False:
                self.move()
            else:
                self.TURNS += 1
                if ((self.TURNS)%2) == 1:
                    self.turn_right()
                    self.move()
                    self.action = False
                    self.turn_right()
                else:
                    self.turn_left()
                    self.move()
                    self.action = False
                    self.turn_left()
           


    def swap_all_boxes(self):
        if not self.BOX_OBTAINED:
            if self.check_wall() == False:
                self.DROP_PICK_UP()
                self.move()
            elif self.check_wall() == True:
                self.TURNS += 1
                if self.TURNS == 24:
                    self.BOX_OBTAINED = True
                else:
                    if ((self.TURNS)%2) == 1:
                        self.turn_right()
                        self.DROP_PICK_UP()
                        self.move()
                        self.turn_right()
                    
                    elif ((self.TURNS)%2) == 0:
                        self.turn_left()
                        self.DROP_PICK_UP()
                        self.move()
                        self.turn_left()
            
                    

            
                
            #PICK UP BOXES AND RECORD POSITIONS WITHOUT BOXES
        
        
        pass #Remove this and fill with your own code

    def walk_around_obstacle(self):
        if self.check_wall() == False:
            if self.WALKING_TO_OBSTACLE == False:
                self.move()
            elif self.WALKING_TO_OBSTACLE == True:
                if self.CHECK_WALL_Y() == True:
                    self.move()
                else:
                    self.turn_right()
        else:
            if self.WALKING_TO_OBSTACLE == False:
                self.turn_right()
                self.move()
                self.turn_left()
                self.WALKING_TO_OBSTACLE == True
            if self.WALKING_TO_OBSTACLE == True:
                self.turn_right()
            elif self.CHECK_WALL_Y() == True:
                self.move()
                
        
            
            
            

