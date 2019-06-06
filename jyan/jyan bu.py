import random
a=1
b=3
c=5

d=7
e=11
f=13

enemycard=[d,e,f]

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
elif enemy=="e":
    print("敵:チョキ")
else:
    print("敵:パー")
#you=a
if you*enemy==7:
    print("あいこ")
elif you*enemy==11:
    print("勝ち")
elif you*enemy==13:
    print("負け")
#you=b
elif you*enemy==21:
    print("負け")
elif you*enemy==33:
    print("あいこ")
elif you*enemy==39:
    print("勝ち")

#you=c
elif you*enemy==35:
    print("勝ち")
elif you*enemy==55:
    print("負け")
else:
    print("あいこ")
