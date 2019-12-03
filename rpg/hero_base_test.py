import hero_base
import enemy_base
import os
import subprocess
# 生成
man=hero_base.Human("man","debug",90,100,100)

# テスト用関数
s = 0
f = 0

def show_test():
    man.show()

def die1_test(hp,da,ty):
    man.show()
    man.live = False
    man.recovery_hp(hp)
    man.receive_damage(da,ty)
    man.show()

def receive_damage_test(da,ty):
    man.show()
    man.receive_damage(da,ty)


def poison_test(p):
    man.show()
    man.receive_poison_turn(p)
    man.check()
    man.show()
    print("poison_turn:{}".format(man.poison_turn))

def bleeding_test(b):
    man.show()
    man.receive_bleeding_turn(b)
    man.check()
    man.show()
    print("bleeding_turn:{}".format(man.bleeding_turn))
    print("attack_base:{}".format(man.attack_base))

def bleeding_and_recovery_test(b,r):
    man.show()
    man.receive_bleeding_turn(b)
    man.check()
    man.show()
    man.receive_bleeding_turn(r)
    man.check()
    man.show()
    print("bleeding_turn:{}".format(man.bleeding_turn))
    print("attack_base:{}".format(man.attack_base))


def critical_test(c):
    print("cri_level={}".format(man.cri_level))
    print("cri_turn={}".format(man.cri_turn))
    man.critical_turn(c)
    print("cri_level={}".format(man.cri_level))
    print("cri_turn={}".format(man.cri_turn))

def base_attack_test():
    man.attack(man.attack_base)
    print("attack_base:{}".format(man.attack_d))
    print("cri_level={}".format(man.cri_level))
    print("cri_turn={}".format(man.cri_turn))
