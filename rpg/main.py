import hero_base
import enemy_base
import random
# from hero_base import Human
# from enemy_base import Slime
class Main:
    def __init__(self):
        self.heros_list_f = []
        self.heros_list_s= []
        self.enemy_list_f = []
        self.enemy_list_s = []
        self.enemy_list_to_show = []
        self.everyone_list = []
        self.heros_died = False
        self.enemy_died = False


    def criate_heros(self):
        self.man = hero_base.Human("man","hero","debug",200,100,100)
        self.heros_list_f.append(self.man)

    def criate_enemys(self):
        self.ene = enemy_base.Slime("ene","enemy","debug",200,100,100)
        self.enemy_list_f.append(self.ene)

    def make_lists(self):
        #初期化
        self.heros_list_s.clear()
        self.enemy_list_s.clear()
        self.everyone_list.clear()
        self.enemy_list_to_show.clear()
        #味方
        for name in self.heros_list_f:
            if name.live == True:
                self.heros_list_s.append(name)
                self.everyone_list.append(name)
        #敵
        for name in self.enemy_list_f:
            if name.live == True:
                self.enemy_list_s.append(name)
                self.everyone_list.append(name)
        #全員
        for i,name in enumerate(self.enemy_list_s,1):
            tmp = "{}:{}".format(i,name.name)
            self.enemy_list_to_show.append(tmp)
        self.check()
        # self.decide_order()

    def decide_order(self):
        random.shuffle(self.everyone_list)
        self.start_turn()


    def check(self):
        if len(self.enemy_list_s) == 0:
            self.heros_died_setter()
        elif len(self.heros_list_s) == 0:
            self.enemy_died_setter()
        else:
            self.decide_order()

    def start_turn(self):
        for name in self.everyone_list:
            if name.tag == "hero" and name.live == True:
                self.hero_next_do(name)
            if name.tag == "enemy" and name.live == True:
                self.enemy_next_do(name)
        self.make_lists()


    def heros_died_setter(self):
        self.heros_died =True
        print("you win")

    def enemy_died_setter(self):
        self.enemy_died = True
        print("you loose")





    def hero_next_do(self,hero_name):
        print("どうする？")
        try:
            want_do = int(input("1:攻撃 2:防御 3:必殺技 4:アイテム 5:ステータス"))
        except Exception as e:
            print("\n入力し直し")
            self.next_do()
        if 1<=want_do and want_do<=5:
            if want_do == 1:
                self.single_attack(hero_name)
                # self.attack(self.attack_base)
            if want_do == 2:
                return hero_name.guard()
            if want_do == 3:
                return print("comming soon")
            if want_do == 4:
                return print("comming soon")
            if want_do == 5:
                return self.show(hero_name)
        else:
            print("\n入力し直し")
            self.hero_next_do()

    def enemy_next_do(self,enemy_name):
        self.man.receive_damage(enemy_name.attack_base)

    def single_attack(self,hero_name):
        print("0で戻る {}".format(self.enemy_list_to_show))
        try:
            target = int(input("ターゲットは？"))
        except Exception as e:
            print("\n入力し直し")
            self.single_attack(hero_name)
        if target == 0:
            self.single_attack(hero_name)
        else:
            hero_name.attack(hero_name.attack_base)
            self.single_damage_geter(self.enemy_list_s[target - 1],hero_name.set_attack)

    def single_damage_geter(self,target_name,damage):
            target_name.receive_damage(damage)



    def show(self,hero_name):
        self.man.show()
        self.ene.show()
        self.hero_next_do(hero_name)
