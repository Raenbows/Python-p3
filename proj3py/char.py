#char.py

class Character:

    def __init__(self, hp, atk, dfc, name, ammo, life, x, y):
        self.hp=hp
        self.atk=atk
        self.dfc=dfc
        self.ammo=ammo
        self.life=life
        self.x=x
        self.y=y

    def calcHP(self, damage):
        self.hp=self.hp+damage
        if self.hp <= 0:
            self.life=False

    def calc_damage(self, opponent):
        damage=randint(0,6)+self.str-opponent.dfc
        if damage <=0:
            print ("{} reflected {}'s {} with a {}!".format(opponent.name, self.name, self.ammo, opponent.ammo))
        else:
            opponent.hp=opponent.hp-damage
            print ("{} shoots a {} at {} for {} points of damage!".format(self.name, self.ammo, opponent.name, str(damage)))
               

class Player(Character):
    def __init__(self, hp, atk, dfc, name, ammo, life, x, y):
        Character.__init__(self, hp, atk, dfc, name, ammo, life, x, y)

    def help():
        print("go [N, E, S, W]\n quit\n attack\n health\n hp\n")

    def health():
        print ("{} has {} health points.".format(self.name, self.hp))
        
    def go(direction, player, board):
        pass
    def attack():
        
        pass
    def quit():
        pass

class Demoman(Player):
    def __init__(self, name):
        Player.__init__(self, 30, 8, 10, name, "grenade", True, 2, 0)

class Soldier(Player):
    def __init__(self, name):
        Player.__init__(self, 30, 10, 8, name, "rocket", True, 2, 0)

class Pyro(Player):
    def __init__(self, name):
        Player.__init__(self, 15, 9, 7, "Robot", "flamlethrower", True, None, None)
