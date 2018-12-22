class Wing:
    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("wee, this is fun.")
        elif self.ratio == 1:
            print("This is hard work but i'm flying.")
        else:
            print("think i can only walk.")


class Duck:

    def __init__(self):
        self.wing = Wing(1.8)

    def walk(self):
        print("waddle, waddle, waddle")

    def swim(self):
        print("come on in, the water is lovely.")

    def quack(self):
        print("quack , quack, quack")

    def fly(self):
        self.wing.fly()


class Penguin(object):

    def walk(self):
        print("waddle, waddle, waddle")

    def swim(self):
        print("come on in, but it's a bit chilly in the south here. ")

    def quack(self):
        print("i can't quack. I'm a penguin!")


class Flock(object):
    def __init__(self):
        self.flock = []

    def migrate(self):
        for duck in self.flock:
            try:
                duck.fly()
            except AttributeError:
                pass

    def add_duck(self, duck: Duck) -> None:
        self.flock.append(duck)


if __name__ == '__main__':
    donald = Duck()
    donald.fly()

    print()

    # percy = Penguin()
    # test_duck(percy)
