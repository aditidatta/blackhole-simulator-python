# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


#from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random


class Floater(Prey):
    radius = 5
    def __init__(self, x, y):
        Prey.__init__(self, x, y, 10, 10, 0 , 5)
        self.randomize_angle()
        
        
    def update(self, model):
        time  = random() 
        if time < .3:
            angle =  random() - .5
            speed_change = random() + .5
            speed = self.get_speed()+speed_change
            if speed < 3:
                speed = 3
            if speed >7:
                speed = 7
            self.set_velocity(speed,angle)
        self.move()
        

    
    def display(self, the_canvas):
        
        the_canvas.create_oval(self._x-Floater.radius, self._y - Floater.radius,self._x+Floater.radius,self._y+Floater.radius, fill='red')
        
        
        
        