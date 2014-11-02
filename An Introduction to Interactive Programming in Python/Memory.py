# implementation of card game - Memory

import simplegui
import random

# helper function to initialize globals
def new_game():
    global list_cards, exposed, state, open_cards, count
    
    open_cards = []
    ind_list = []
    count = 0
    state = 0
    list_cards = range(1, 9)
    list_cards.extend(range(1, 9))
    random.shuffle(list_cards) 
    
    exposed = []
    for i in range(16):
        exposed.append(False)
    
     
# define event handlers
def mouseclick(pos):
    global list_cards, exposed, state, count, ind_one, ind_two
    
    ind = pos[0] // 50
    if exposed[ind] != True:
        exposed[ind] = True
        if state == 0:
            state = 1
            ind_one = ind
        elif state == 1:
            ind_two = ind
            state = 2
        else:
            if list_cards[ind_one] != list_cards[ind_two]:
                exposed[ind_one] = False
                exposed[ind_two] = False
            ind_one = ind
            count += 1
            state = 1

                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global list_cards, exposed, count
    label.set_text("Turns =" + str(count))
    x1 = 0
    for k in range(len(exposed)):
        if exposed[k]:
            p_text = [x1 + 5, 85]
            canvas.draw_text(str(list_cards[k]), p_text, 80, "White")
            x1 += 50
        else:
            canvas.draw_polygon([[x1, 0], [x1, 100], [x1 + 50, 100], [x1 + 50, 0]], 2, "Black", "Green") 
            x1 += 50

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric