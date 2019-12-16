import hero_base
import enemy_base
# from hero_base import Human
# from enemy_base import Slime
class Main:
    def __init__(self):
        self.heros_list = []
        self.enemy_list = []

    def criate_heros(self):
        self.man = hero_base.Human("man","debug",90,100,100)

    def criate_enemys(self):
        self.ene = enemy_base.Slime("ene","debug",90,100,100)

    def decide_order(self):
        self.orderlist = [self.man,self.ene]
        self.heros_list=[self.man]
        self.enemy_list=[self.ene]
        self.enemy_list_to_show=[self.ene.name]
        self.hero_next_do(self.man)


    def damage_geter(self,name,damage):
            name.receive_damage(damage)


    def hero_next_do(self,name):
        print("どうする？")
        try:
            want_do = int(input("1:攻撃 2:防御 3:必殺技 4:アイテム 5:ステータス"))
        except Exception as e:
            print("\n入力し直し")
            self.next_do()
        if 1<=want_do and want_do<=5:
            if want_do == 1:
                self.single_attack(name)
                # self.attack(self.attack_base)
            if want_do == 2:
                return name.guard()
            if want_do == 3:
                return print("comming soon")
            if want_do == 4:
                return print("comming soon")
            if want_do == 5:
                return self.show()
        else:
            print("\n入力し直し")
            self.hero_next_do()

    def single_attack(self,name):
        print("0で戻る {}".format(self.enemy_list_to_show))
        target = int(input("ターゲットは？"))
        name.attack(name.attack_base)
        self.damage_geter(self.enemy_list[target - 1],name.set_attack)


    def show(self):
        self.man.show()
        self.ene.show()
