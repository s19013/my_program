# import hero_base
# import enemy_base
from hero_base import Human
from enemy_base import Slime

class Main:
    def criate_crature(self):
        self.hum = hero_base.Human("man","debug",90,100,100)
        self.ene = enemy_base.Slime("ene","debug",90,100,100)

    def decide_order(self):
        self.heros_list=[hum]
        self.enemy_list=[ene]
        self.orderlist = [self.hum,self.ene]
