#char.py

class Character:

    def __init__(self, hp, atk, dfc, name, wep):
        self.hp=hp
        self.atk=atk
        self.dfc=dfc
        self.wep=wep

class Player(Character):
    def __init__(self, hp, atk, dfc, name, wep):
        Character.__init__(self, hp, atk, dfc, name, wep)

    def help():
        pass
    def health():
        pass
    def go():
        pass
    def attack(): 
        pass
    def quit():
        pass

class Demoman(Player):
    def __init__(self, name):
        Player.__init__(self, 30, 8, 10, name, "Grenade Launcher")

class Soldier(Player):
    def __init__(self, name):
        Player.__init__(self, 30, 10, 8, name, "Rocket Launcher")

class Pyro(Player):
    def __init__(self, name):
        Player.__init__(self, 15, 9, 7, "Robot", "Flamlethrower")
