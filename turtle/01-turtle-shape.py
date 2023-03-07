import turtle
import time

tObj = turtle.Turtle()
totalSide = 4 #Square
angle = 90 #square

print("Draw multiple object as per below choice:")
print("1) Square, \n 2) Triangle, \n 3) Hexagon, \n 4) Start, \n 5) Circle \n 6) Start-120, \n 7) Reverse Triangle.")

selectChoice = int(input("Please enter no of choise as per above: "))
color = input("Please enter color fo the filled in RRGGBB: ")

tObj.fillcolor(color)
tObj.begin_fill()

if selectChoice == 1:
    totalSide = 4
    angle = 90
elif selectChoice == 2:
    totalSide = 3
    angle = -120
elif selectChoice == 3:
    totalSide = 6
    angle = -60
elif selectChoice == 4:
    totalSide = 5
    angle = 144
elif selectChoice == 6:
    totalSide = 5
    angle = 120
elif selectChoice == 7:
    totalSide = 3
    angle = 120

if selectChoice == 5:
    lenght = int(input("Please enter redious of round: "))
    tObj.circle(lenght)
else:     
    lenght = int(input("Please enter lenght: "))
    for _ in range(totalSide):
        tObj.forward(lenght)
        tObj.right(angle)

        if selectChoice == 6:
                tObj.forward(lenght)
                tObj.right(72 - angle)



tObj.end_fill()

time.sleep(5)