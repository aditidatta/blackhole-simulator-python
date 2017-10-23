# A Hunter is both a Mobile_Simulton and Pulsator: it updates
#   like a Pulsator, but it moves (either in a straight line
#   or in pursuit of Prey) and displays as a Pulsator.


from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from prey import Prey
from math import atan2


class Hunter(Pulsator,Mobile_Simulton):
   
    def __init__(self,x,y):
        Pulsator.__init__(self, x, y)
        Mobile_Simulton.__init__(self, x, y, self._width, self._height, 0, 5)
        self.randomize_angle()
    
    def update(self,temp_set):
        to_remove = temp_set.find(lambda item: isinstance(item,Prey))
        x1, y1 = self.get_location()
        temp = 200
        closest = None
        for item in to_remove:
            if self.contains(item.get_location()):
                    temp_set.remove(item)
            elif self.distance(item.get_location()) < 200:
                c = self.distance(item.get_location())
                #d = min(temp,c )
                #temp = d
                if temp > c:
                    temp = c
                    closest = item
        if closest is not None:
            x2,y2 = closest.get_location()
            angle = atan2(y2-y1, x2-x1)        
            self.set_angle(angle)
        self.move()
        #return to_remove
        
        
    
