# Hunter inherits from the Pulsator (1st) and the Mobile_Simulton (2nd) class:
#   updating/displaying like its Pulsator base, but also moving (either in
#   a straight line or in pursuit of Prey), like its Mobile_Simultion base.


from prey import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2


class Hunter(Pulsator, Mobile_Simulton):
    sight = 200

    def __init__(self, x, y):
        Pulsator.__init__(self, x, y)
        w, h = self.get_dimension()
        Mobile_Simulton.__init__(self, x, y, w, h, 0, 5)
        self.randomize_angle()

    def update(self, model):
        self.move()
        Pulsator.update(self, model)
        simsSeen = model.find(lambda s: isinstance(s, Prey) and self.distance(s.get_location()) <= Hunter.sight)
        closest = sorted(simsSeen, key=lambda s: self.distance(s.get_location()))[0] if simsSeen else None
        if closest is not None:
            x1, y1 = closest.get_location()
            x2, y2 = self.get_location()
            newAngle = atan2(y1-y2, x1-x2)
            self.set_angle(newAngle)
