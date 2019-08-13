import random
class human:
    def __init__(self,name,hp,mp):
        self.name=name
        self.hp=hp
        self.mp=mp

    def getname(self):
        return self.name
    def gethp(self):
        return self.hp
    def getmp(self):
        return self.mp

    def receive_damage(self,damage):
        self.damage=damage
        self.hp-=self.damage
        return self.hp

    def attack(self,trick):
        return trick

    def remaing_mp(self,used_mp):
        self.used_mp=used_mp

class info:
    def show_info(self,name,hp,mp):
        self.name=name
        self.hp=hp
        self.mp=mp
        print("""{}
HP:{}
MP:{}""".format(self.name,self.hp,self.mp))
man=human("man",100,100)
info().show_info(man.getname(),man.gethp(),man.getmp())
