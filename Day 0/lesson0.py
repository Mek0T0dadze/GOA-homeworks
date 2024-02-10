from turtle import*
#drawing house
#step 1 draw a square
speed(10)
width(7)
color("purple")
begin_fill()
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
end_fill()
#end of square

#drawing a door
forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()
#end of door

#drawing a roof
penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#end of roof 

#drawing windows
penup()
goto(20,170)
pendown()
color("cyan")
begin_fill()
left(120)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
penup()
goto(180,170)
pendown()
left((90))
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward((40))
end_fill()



exitonclick()