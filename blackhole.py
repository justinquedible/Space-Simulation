# Black_Hole inherits from only Simulton, updating by finding/removing
#   any Prey-derived class whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey


class Black_Hole(Simulton):
    radius = 10

    def __init__(self, x, y):
        Simulton.__init__(self, x, y, Black_Hole.radius * 2, Black_Hole.radius * 2)

    def update(self, model):
        simsEaten = model.find(lambda s: isinstance(s, Prey) and self.contains(s.get_location()))
        model.simultons.difference_update(simsEaten)
        return simsEaten

    def display(self, canvas):
        w, h = self.get_dimension()
        canvas.create_oval(self._x - w/2, self._y - h/2,
                           self._x + w/2, self._y + h/2, fill="#000000")

    def contains(self, xy):
        radius = self.get_dimension()[0] / 2
        return self.distance(xy) < radius
