import random


class Enemy:

    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self.name = name
        self.hit_points = hit_points
        self.lives = lives
        self.alive = True

    def take_damage(self, damage):
        remaining_points = self.hit_points - damage
        if remaining_points >= 0:
            self.hit_points = remaining_points
            print("I took {} points damage and have {} left"
                  .format(damage, self.hit_points))
        else:
            self.lives -= 1
            if self.lives > 0:
                print("{} lost a life.".format(self.name))
            else:
                print("{} is now dead.".format(self.name))
                self.alive = False

    def __str__(self):
        return "Name : {0.name}, Hit points : {0.hit_points}, Lives : {0.lives}" \
            .format(self)


class Troll(Enemy):

    def __init__(self, name):
        super().__init__(name=name, hit_points=23, lives=1)

    def grunt(self):
        print('Me {0}. {0} stomp you.'.format(self.name))


class Vampire(Enemy):

    def __init__(self, name):
        super().__init__(name=name, hit_points=12, lives=3)

    def dodges(self):
        if random.randint(1, 3) == 3:
            print("**** {} dodges ****".format(self.name))
            return True
        else:
            return False

    def take_damage(self, damage):
        if not self.dodges():
            super().take_damage(damage)


class VampireKing(Vampire):

    def __init__(self, name):
        super().__init__(name=name)
        self.hit_points = 140

    def take_damage(self, damage):
        damage = damage//4
        super().take_damage(damage)
