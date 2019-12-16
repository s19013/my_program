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

def die1_test(hp,da):
    man.show()
    man.live = False
    man.recovery_hp(hp)
    man.receive_damage(da)
    man.show()

def receive_damage_test(da):
    man.show()
    man.receive_damage(da)


def poison_test(p=0):
    man.show()
    man.receive_poison_turn(p)
    man.check()
    man.show()
    print("poison_turn:{}".format(man.poison_turn))

def bleeding_test(b=0):
    man.show()
    man.receive_bleeding_turn(b)
    man.check()
    man.show()
    print("bleeding_turn:{}".format(man.bleeding_turn))
    print("attack_base:{}".format(man.attack_base))

def bleeding_and_recovery_test(b=0,r=0):
    man.show()
    man.receive_bleeding_turn(b)
    man.check()
    man.show()
    # 負の値を入れる
    man.receive_bleeding_turn(r)
    man.check()
    man.show()
    print("bleeding_turn:{}".format(man.bleeding_turn))
    print("attack_base:{}".format(man.attack_base))


def critical_test(c=0):
    print("cri_level={}".format(man.cri_level))
    print("cri_turn={}".format(man.cri_turn))
    man.receive_critical_turn(c)
    print("cri_level={}".format(man.cri_level))
    print("cri_turn={}".format(man.cri_turn))

def base_attack_test():
    man.attack(man.attack_base)
    print("attack_base:{}".format(man.attack_d))
    print("cri_level={}".format(man.cri_level))
    print("cri_turn={}".format(man.cri_turn))

def guard_test(df = 0):
    man.receive_defence_turn(df)
    man.guard()
    man.receive_damage(100)

# def next_do_test():
#     man.next_do()

guard_test()
