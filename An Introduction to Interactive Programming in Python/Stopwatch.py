# template for "Stopwatch: The Game"
import simplegui

# define global variables
global time
global x
global y 

time = 0
x = 0
y = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    minutes = t // 600
    seconds = (t - minutes * 600) // 10
    millis = t % 10
    if seconds < 10:
        return str(minutes) + ":0" + str(seconds) + "." + str(millis)
    else:
        return str(minutes) + ":" + str(seconds) + "." + str(millis)
        
# define event handlers for buttons; "Start", "Stop", "Reset"
def button_start():
    timer.start()

def button_stop():
    global x
    global y
    global clock_run
    
    if timer.is_running() == True:
        y += 1	
        timer.stop()
    else:
        return
    
    if time % 10 == 0:
        x += 1
        
def button_reset():
    global time
    global x
    global y
    time = 0
    x = 0
    y = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time
    time += 1
    

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(time), (50, 100), 40, 'white')
    canvas.draw_text((str(x) + '/' + str(y)), (150, 20), 20, 'red')
    
# create frame
frame = simplegui.create_frame('Stopwatch', 200, 150)

# register event handlers
b_start = frame.add_button('Start', button_start, 50)
b_stop = frame.add_button('Stop', button_stop, 50)
b_reset = frame.add_button('Reset', button_reset, 50)

timer = simplegui.create_timer(100, timer_handler)

frame.set_draw_handler(draw_handler)
# start frame
frame.start()

# Please remember to review the grading rubric
