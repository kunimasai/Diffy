from turtle import *
from math import sqrt

tur = Turtle() # instance of turtle
tur.speed(5) # set turtle speed
tur.hideturtle()

DIFFY_LIST = [] #set global empty list for capturing all diffys

def diffy(a):
    '''input: starting values for the four corners in an array(list) format.
       output: an array of all diffys
    '''
    temp = []
    i = 0
    DIFFY_LIST.append(a[0:4])

    # base case
    if a.count(0) == 4:
        return temp

    a.append(a[0])
    while i < len(a)-1:
        temp.append(abs(a[i]-a[i+1]))
        i += 1

    diffy(temp)
    return DIFFY_LIST

def question():
    corners_list = []
    corners = input('Please enter 4 numbers for the 4 corners of a square. Seperate the numbers with commas. For example: 1,2,3,4: ')
    corners = corners.split(',')
    for n in corners:
        corners_list.append(int(n))
    return corners_list

def draw_line(length):
    '''draw the basic line, this is necessary because we're going to annotate the lines with sqaure corner values
       input: length of line (one side of the square)
       output: line of length length
    '''
    tur.width(2)
    tur.forward(length)

def draw_square(size, j):
    '''draw square plus annotating the corners of the squres with corner values
       input: length of line (one side of the square), and an array index counter
       output: a square
    '''
    k = 0
    for i in range(4):
        tur.write(DIFFY_LIST[j][k], font=("Arial", 12, "bold"))
        draw_line(size)
        tur.right(90)
        k += 1


def diffy_squares(square_count, size):
    '''draw alternating squares: turning each square 45 degrees
       input: number of sqaures to draw, length of line (one side of the sqaure)
       output: draw alternating squares
    '''
    angle = 90
    hypo = size
    j = 0
    for i in range(square_count):
        draw_square(hypo, j)
        size = hypo/2.0
        tur.penup()
        tur.forward(size)
        tur.pendown()
        tur.right(angle-45)
        hypo = sqrt(size**2 + size**2)
        j += 1

        
diffy(question())
diffy_squares(len(DIFFY_LIST), 400)
DIFFY_LIST
print('The total number of diffy squares we will get from {} is: {}.  Here are the steps: \n {}'.format(DIFFY_LIST[0], len(DIFFY_LIST), DIFFY_LIST))

tur.done()