from ducks import Duck, Penguin, Flock, Wing, Mallard

flock = Flock()
donald = Duck()
daisy= Duck()
duck1 = Duck()
duck2 = Duck()
duck3 = Duck()
duck4 = Duck()
duck5 = Duck()
percy = Mallard()

flock.add_duck(donald)
flock.add_duck(daisy)
flock.add_duck(duck1)
flock.add_duck(duck2)
flock.add_duck(duck3)
flock.add_duck(duck4)
flock.add_duck(duck5)
flock.add_duck(percy)

flock.migrate()
