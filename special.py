# Spawner inherits only from Simulton.
# It spawns a random Prey (e.g. Ball, Floater) from its location.
# The rate that it spawns Prey slows down the more Prey instances
#   that exist in the model, using a simplified logistic growth equation:
#   SpawnRate = population(1 - population/maxPopulation)


from simulton import Simulton
from prey import Prey
from ball import Ball
from floater import Floater
from random import random


class Prey_Spawner(Simulton):
    radius = 10
    baseSpawnRate = 1  # initial Prey objects spawned per 10 cycles, or 1 second
    maxPopulation = 50

    def __init__(self, x, y):
        Simulton.__init__(self, x, y, Prey_Spawner.radius * 2, Prey_Spawner.radius * 2)
        self.cycle_count = 0

    def update(self, model):
        self.cycle_count += 1
        if self.cycle_count >= 10:
            population = len(model.find(lambda s: isinstance(s, Prey)))
            spawnRate = int(Prey_Spawner.baseSpawnRate + population * (1 - population / Prey_Spawner.maxPopulation))
            for _ in range(spawnRate):
                x, y, = self.get_location()
                if random() < 0.5:
                    model.add(Ball(x, y))
                else:
                    model.add(Floater(x, y))
            self.cycle_count = 0

    def display(self, canvas):
        canvas.create_oval(self._x - Prey_Spawner.radius, self._y - Prey_Spawner.radius,
                           self._x + Prey_Spawner.radius, self._y + Prey_Spawner.radius, fill="#800080")