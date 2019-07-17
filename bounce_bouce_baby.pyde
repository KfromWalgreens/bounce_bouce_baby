import random
ball_y = 100
y_speed = 10
ball_x = 200
x_speed = 8

ball2_y = 200
y2_speed = 11
ball2_x = 200
x2_speed = 6

speeds = [y_speed, x_speed, y2_speed, x2_speed]

def setup():
    size(500,500)
    background(255,255,255)
    
def draw():
    global ball_y
    global y_speed
    global ball_x
    global x_speed
    global ball2_y
    global y2_speed
    global ball2_x
    global x2_speed
    background(255,255,255)
    fill(ball_y, random.choice(speeds), ball_x)
    ellipse(ball_x, ball_y, 100, 100)
    ellipse(ball2_x, ball2_y, 100, 100)
    line(0,400,500,400)
    
    if ball_y > 350:
        #print("bounce bounce baby")
        y_speed = -random.choice(speeds)
        #-y_speed 
    if ball_y < 50:
        #print("bounce bounce baby")
        y_speed =  -y_speed 
    if ball_x > 450:
        x_speed = -x_speed
    if ball_x < 50:
        #print("bounce bounce baby")
        x_speed =  -x_speed 
        
    if ball2_y > 350:
        #print("bounce bounce baby")
        y2_speed = -y2_speed 
    if ball2_y < 50:
        #print("bounce bounce baby")
        y2_speed =  -y2_speed 
    if ball2_x > 450:
        x2_speed = -x2_speed
    if ball2_x < 50:
        #print("bounce bounce baby")
        x2_speed =  -x2_speed 
        
    ball_y += y_speed
    ball_x += x_speed
    
    ball2_y += y2_speed
    ball2_x += x2_speed
    


    
