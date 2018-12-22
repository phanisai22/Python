import ducks

flock = ducks.Flock()

duck1 = ducks.Duck()
duck2 = ducks.Duck()
duck3 = ducks.Duck()
duck4 = ducks.Duck()
duck5 = ducks.Duck()
duck6 = ducks.Duck()
duck7 = ducks.Duck()
penguin = ducks.Penguin()

flock.add_duck(duck1)
flock.add_duck(duck2)
flock.add_duck(duck3)
flock.add_duck(duck4)
flock.add_duck(penguin)
flock.add_duck(duck5)
flock.add_duck(duck6)
flock.add_duck(duck7)

flock.migrate()
