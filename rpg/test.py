import hero_base
import enemy_base
import os
man=hero_base.Human("man","debug",100,100,100)

# テスト用関数
def die1(hp,da):
    man.show()
    man.live = False
    man.recovery_hp(hp)
    man.receive_damage(da)
    man.show()

def dei2(da):
    man.show()
    man.receive_damage(da)


def izyou(p,b):
    man.show()
    man.receive_poison(p)
    man.receive_bleeding(b)
    man.check()
    man.show()

def critical(c):
    print("cri_level={}".format(man.cri_level))
    print("cri_turn={}".format(man.cri_turn))
    man.critical_turn(c)
    print("cri_level={}".format(man.cri_level))
    print("cri_turn={}".format(man.cri_turn))

def attack():
    man.base_attack()
    print(man.attack_d)


attack()
critical(16)
attack()
