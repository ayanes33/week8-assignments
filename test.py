#Draw rectangle in pythn using turtle
import turtle

t=turtle.Turtle()
l=int(input("enter the lenght of the rectangle"))
w=int(input("enter the width of the rectangle"))

#drawing first side
t.forward(l) #forward turtle by 1 unit
t.left(90) #turn turtle by 90 degree

#drawing second side
t.forward(w) #forward turtle by w unit
t.left(90) #turn turtle by 90 degree

#drawing third side
t.forward(l) #forward turtle by w unit
t.left(90) #turn turtle by 90 degree

#drawing fourth side
t.forward(w) #forward turtle by w unit
t.left(90) #turn turtle by 90 degree

turtle.done()

