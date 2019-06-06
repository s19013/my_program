import random
import sys
enemycard=["d","e","f"]

print("じゃんけん")
#you
you=input("[グー:a　チョキ:b　パー:c]")

if you=="a":
    print("あなた:グー")
elif you=="b":
    print("あなた:チョキ")
else:
    print("あなた:パー")
#enemy
enemy=random.choice(enemycard)
if enemy=="d":
    print("敵:グー")
if enemy=="e":
    print("敵:チョキ")
if enemy=="f" :
    print("敵:パー")
#you=a
if you=="a" and enemy=="d":
    print("あいこ")
if you=="a" and enemy=="e":
    print("勝ち")
if you=="a" and enemy=="f":
    print("負け")
if you=="b" and enemy=="d":
    print("勝ち")
if you=="b" and enemy=="e":
    print("あいこ")
if you=="b" and enemy=="f":
    print("負け")
if you=="c" and enemy=="d":
    print("勝ち")
if you=="c" and enemy=="e":
    print("負け")
if you=="c" and enemy=="f":
    print("あいこ")
