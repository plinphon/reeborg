
def turn_right( ):
    turn_left()
    turn_left()
    turn_left()

def window():
    while True:
        if not wall_on_right():
            move()
            if not wall_on_right():
                turn_right()
                turn_right()
                move()
                turn_left()
                move()
            else:
                turn_right()
                turn_right()
                move()
                turn_left()
                build_wall()
                turn_left()
                move()
        elif wall_in_front():
            turn_left()

        else:
            move()
            if at_goal():
                done()
            
  
def find_center():
    walk=0
    while True:
        
        if wall_in_front():
            turn_left()
            turn_left()
            return walk
        else:
            move()
            walk+=1

move()
move()
turn_left()
move()
       
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
