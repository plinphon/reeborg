
def turn_right( ):
    turn_left()
    turn_left()
    turn_left()

def wall():
    while True:
        if object_here():
                take()
                done()
        elif not wall_on_right():
            turn_right()
            move()
        elif wall_in_front():
            turn_left()
        else:
            move()
                
        
            
  
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

turn_left()
turn_left()
put()
move()
wall()
       
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
