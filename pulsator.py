# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions


from blackhole import Black_Hole


class Pulsator(Black_Hole):
    counter = 30

    def __init__(self, x, y):
        Black_Hole.__init__(self, x, y)
        self.counter = 0

    def update(self, model):
        simsEaten = Black_Hole.update(self, model)
        if (n := len(simsEaten)) > 0:
            self.change_dimension(n, n)
            self.counter = 0
        else:
            self.counter += 1
        if self.counter >= Pulsator.counter:
            self.change_dimension(-1, -1)
            self.counter = 0
        if self.get_dimension() == (0, 0):
            model.remove(self)
