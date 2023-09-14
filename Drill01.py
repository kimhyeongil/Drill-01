import turtle as t
t.shape("turtle")
t.listen()  
def move_up():
    t.stamp()
    t.setheading(90)
    t.forward(50)
def move_left():
    t.stamp()
    t.setheading(180)
    t.forward(50)
    
def move_down():
    t.stamp()
    t.setheading(-90)
    t.forward(50)
def move_right():
    t.stamp()
    t.setheading(0)
    t.forward(50)

t.onkey(move_up,'w')
t.onkey(move_left,'a')
t.onkey(move_down,'s')
t.onkey(move_right,'d')
t.onkey(t.reset,'Escape')
t.mainloop()
