from tkinter import *
import random
from math import sin, cos, pi, log

def hc():
    canvas.create_arc((50,50,300,300),
                  outline='red',
                  start=0,
                  extent=180,
                  )

    canvas.create_arc((300,50,450,500),
                  outline='red',
                  start=0,
                  extent=180,)







root = Tk()
root.title('good morning')
root.geometry('1200x900')

canvas = Canvas(root,width=500,height=500,background='lightgray')
canvas.pack() #add

print(hc())





root.mainloop()