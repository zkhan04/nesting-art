import math
from tkinter import *
from tkinter import ttk

window = Tk()
window.title("end result")
w = Canvas(window, bg="blue", height=800, width=800)

# uses built-in sin function, but for degrees 
def sin(theta):
    return math.sin(theta * math.pi / 180)

# uses built-in cos function, but for degrees
def cos(theta):
    return math.cos(theta * math.pi / 180)

# uses degree rotation to calculate square length, and coordinates of each individual point
def inscribe_square(cx, cy, l, ro, theta, border, back):
    h = l / (abs(cos(ro)) + abs(sin(ro)))
    r = h * math.sqrt(2) / 2
    x0, y0 = coordinates(cx, cy, r, 45 + theta + ro)
    x1, y1 = coordinates(cx, cy, r, 135 + theta + ro)
    x2, y2 = coordinates(cx, cy, r, 225 + theta + ro)
    x3, y3 = coordinates(cx, cy, r, 315 + theta + ro)
    w.create_polygon(x0, y0, x1, y1, x2, y2, x3, y3, outline=border, fill=back)

# converts polar to cartesian coordinates
def coordinates(cx, cy, r, theta):
    xi = (r * cos(theta) + cx)
    yi = (r * sin(theta) + cy)
    x = round(xi)
    y = round(yi)
    return (x, y)

# inscribes many squares inside of each other, creating the 'vortex' pattern which is repeated across the canvas
def pattern(cx, cy, l, theta, i, border, back):
    inscribe_square(cx, cy, l, 0, 0, border, back)
    for a in range(i):
        t = theta * a
        inscribe_square(cx, cy, l, theta, t, border, back)
        l = l / (abs(cos(theta)) + abs(sin(theta)))

# places many vortexes next to each other. toggles theta forward/backwards, allowing for the connected effect
def finish(n, theta, i, border, back):
    shift = 1
    for a in range(n):
        if n % 2 == 0:
            shift *= -1
        for b in range(n):
            pattern(a * 800 / n + 400/n, b * 800/n + 400/n, 800 / n, theta * shift, i, border, back)
            shift *= -1

# takes user input for parameters for finish function, spits out art
if __name__ == '__main__':
    n = int(input("How many squares wide/tall should the art be? "))
    theta = int(input("How far in degrees do you want the pattern to rotate each level? "))
    i = int(input("How many nested squares do you want in each pattern? "))
    border = input("What color do you want the lines to be? ")
    back = input("What color do you want the background to be? ")
    finish(n, theta, i, border, back)
    w.pack()
    window.mainloop()
