import simplegui

interval = 100
totalStops = 0
succesStops = 0
time = 0

def result(totalStops, succesStops):
    return str(totalStops) + '/' + str(succesStops)

#format time
def format(time):
    a = str(time / 600)#min
    b = str((time % 600) / 100)#ks
    c = str((time % 100) / 10)#s
    d = str((time % 10))#ms
    return a + ':' + b + c + '.' + d

#start timer
def Start():
    timer.start()
    
#stop timer    
def Stop():
    timer.stop()
    
    global totalStops,succesStops
    totalStops += 1
    
    if time%10 == 0:
        succesStops += 1
       
#reset timer    
def Reset():
    timer.stop()
    
    global time, totalStops, succesStops
    time = 0
    totalStops = 0
    succesStops = 0
    
#drawing    
def draw_handler(canvas):
    canvas.draw_text(format(time), (130, 130), 50, "White")
    canvas.draw_text(result(succesStops,totalStops), (300,50), 30, "Red")
    

def timer_handler():
    global time
    time += 1
    
#create frame    
frame = simplegui.create_frame("Game stopwathc", 400, 250,)
frame.set_canvas_background("Green")

#add buttons
button1 = frame.add_button("Start", Start, 100)
button2 = frame.add_button("Stop", Stop, 100)
button3 = frame.add_button("Restart", Reset,100)

#draw in frame
frame.set_draw_handler(draw_handler)
timer = simplegui.create_timer(interval, timer_handler)


#start frame
frame.start()