# implementation of card game - Memory
import simplegui
import random

#Setings of card
HEIDHT = 100
WIDTH = 50
COLORBORDER = "Red"
COLOR = "Green"
COLORNUM = "Green"

#Setings of game
numlist = []
exposed = []
choices = [-1, -1]
moves = 0
status = 0


# helper function to initialize globals
def new_game():
    global numlist, exposed, moves, status, choices
    
    numlist = range(0, 8)
    numlist.extend( range(0,8) )
    
    random.shuffle(numlist)
    
    exposed = [0] * 16
    moves = 0
    status = 0
    choices = [-1, -1]
    
    label.set_text( "Moves : " + str(moves) )

     
# define event handlers
def mouseclick(pos):
    global choices,status,moves
    
    index=int(pos[0]/WIDTH)
    
    if status == 0:
        if exposed[index] == 0:
            if numlist[choices[0]] != numlist[choices[1]]:
                exposed[choices[0]] = 0
                exposed[choices[1]] = 0
            exposed[index] = 1
            status = 1
            choices[0] = index
    elif status == 1:
        if exposed[index]==0:
            status = 0
            exposed[index] = 1
            choices[1] = index
            moves+=1
            
            label.set_text("Moves : "+str(moves))
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for index in range(0, len(numlist)):
        if exposed[index] == 0:
            canvas.draw_polygon( [ (WIDTH * index, 0), (WIDTH * (index + 1), 0), (WIDTH * (index+1),100), (WIDTH * index,100) ], 3, COLORBORDER, COLOR)
        else :
            canvas.draw_text( str(numlist[index] ),[WIDTH * index + 5, HEIDHT-25], 60,COLORNUM )

# create frame and add a button and labels1
frame = simplegui.create_frame("Memory game", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
# Always remember to review the grading rubric