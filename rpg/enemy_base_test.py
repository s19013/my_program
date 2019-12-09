import hero_base
import enemy_base
import os
import subprocess
# 生成
ene=enemy_base.Slime("ene","debug",90,100,100)

# テスト用関数
s = 0
f = 0

def show_test():
    ene.show()

def die1_test(hp,da):
    ene.show()
    ene.live = False
    ene.recovery_hp(hp)
    ene.receive_damage(da)
    ene.show()

def receive_damage_test(da):
    ene.show()
    ene.receive_damage(da)


def poison_test(p=0):
    ene.show()
    ene.receive_poison_turn(p)
    ene.check()
    ene.show()
    print("poison_turn:{}".format(ene.poison_turn))

def bleeding_test(b=0):
    ene.show()
    ene.receive_bleeding_turn(b)
    ene.check()
    ene.show()
    print("bleeding_turn:{}".format(ene.bleeding_turn))
    print("attack_base:{}".format(ene.attack_base))

def bleeding_and_recovery_test(b=0,r=0):
    ene.show()
    ene.receive_bleeding_turn(b)
    ene.check()
    ene.show()
    # 負の値を入れる
    ene.receive_bleeding_turn(r)
    ene.check()
    ene.show()
    print("bleeding_turn:{}".format(ene.bleeding_turn))
    print("attack_base:{}".format(ene.attack_base))


def critical_test(c=0):
    print("cri_level={}".format(ene.cri_level))
    print("cri_turn={}".format(ene.cri_turn))
    ene.critical_turn(c)
    print("cri_level={}".format(ene.cri_level))
    print("cri_turn={}".format(ene.cri_turn))

def base_attack_test():
    ene.attack(ene.attack_base)
    print("attack_base:{}".format(ene.attack_d))
    print("cri_level={}".format(ene.cri_level))
    print("cri_turn={}".format(ene.cri_turn))

def guard_test(df = 0):
    ene.defence_turn(df)
    ene.guard()
    ene.receive_damage(100)

def next_do_test():
    ene.next_do()

next_do_test()
