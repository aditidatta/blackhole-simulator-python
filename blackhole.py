# A Black_Hole is a Simulton; it updates by removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey
#import model

class Black_Hole(Simulton):
    radius = 10
    
    def __init__(self,x,y):
        Simulton.__init__(self, x, y, 20, 20)
        
    def contains(self,xy):
        distance  = self.distance(xy)
        return distance < Black_Hole.radius
    
    def update(self,temp_set):
        to_remove=set()
        preys = temp_set.find(lambda item: isinstance(item,Prey))
        for item in preys:
            if self.contains(item.get_location()):
                to_remove.add(item)
                temp_set.remove(item)
        print(len(to_remove))
        return to_remove
        
        
    
    def display(self,the_canvas):
        width, height = 
        the_canvas.create_oval(self._x-self.get_dimension()[0]/2, self._y-self.get_dimension()[1]/2, self._x+self.get_dimension()[0]/2, self._y+self.get_dimension()[1]/2,fill = 'black')
