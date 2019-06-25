import random
import sys
#mycard
a=random.randint(1,13)
b=random.randint(1,13)
c=random.randint(1,13)
d=random.randint(1,13)
e=random.randint(1,13)
f=random.randint(1,13)
g=random.randint(1,13)
h=random.randint(1,13)
i=random.randint(1,13)
j=random.randint(1,13)
k=random.randint(1,13)
mycard=[a,b]

#enemycard\
ea=random.randint(1,13)
eb=random.randint(1,13)
ec=random.randint(1,13)
ed=random.randint(1,13)
ee=random.randint(1,13)
ef=random.randint(1,13)
eg=random.randint(1,13)
eh=random.randint(1,13)
ei=random.randint(1,13)
ej=random.randint(1,13)
ek=random.randint(1,13)
enemycard=[ea,eb]

print(mycard)
h_or_s=input("hit_or_stand")

if h_or_s=="h" and sum(mycard)<=21:
    mycard.append(c)
    print(mycard)
    h_or_s=input("hit_or_stand")
    if h_or_s=="h" and sum(mycard)<=21:
        mycard.append(d)
        print(mycard)
        h_or_s=input("hit_or_stand")
        if h_or_s=="h" and sum(mycard)<=21:
            mycard.append(e)
            print(mycard)
            h_or_s=input("hit_or_stand")
            if h_or_s=="h" and sum(mycard)<=21:
                mycard.append(f)
                print(mycard)
                h_or_s=input("hit_or_stand")
                if h_or_s=="h" and sum(mycard)<=21:
                    mycard.append(g)
                    print(mycard)
                    h_or_s=input("hit_or_stand")
                    if h_or_s=="h" and sum(mycard)<=21:
                        mycard.append(h)
                        print(mycard)
                        h_or_s=input("hit_or_stand")
                        if h_or_s=="h" and sum(mycard)<=21:
                            mycard.append(i)
                            print(mycard)
                            h_or_s=input("hit_or_stand")
                            if h_or_s=="h" and sum(mycard)<=21:
                                mycard.append(j)
                                print(mycard)
                                h_or_s=input("hit_or_stand")
                                if h_or_s=="h" and sum(mycard)<=21:
                                    mycard.append(k)
                                    print(mycard)
                                    h_or_s=input("hit_or_stand")

elif sum(mycard) > 21:
    print("barst")
    print(mycard)
    sys.exit("game_over")

if h_or_s=="s":
    print("enemy's_turn")
    print(enemycard)
    print("please_wait")
if sum(enemycard) <= 18:
    enemycard.append(ec)
    if sum(enemycard) <= 18:
        enemycard.append(ed)
        if sum(enemycard) <= 18:
            enemycard.append(ee)
            if sum(enemycard) <= 18:
                enemycard.append(ef)
                if sum(enemycard) <= 18:
                    enemycard.append(eg)
                    if sum(enemycard) <= 18:
                        enemycard.append(eh)
                        if sum(enemycard) <= 18:
                            enemycard.append(ei)
                            if sum(enemycard) <= 18:
                                enemycard.append(ej)
                                if sum(enemycard) <= 18:
                                    enemycard.append(ek)

if sum(enemycard) > 18:
    print("open_card")
    print("mycard:{}".format(mycard))
    print("enemycard{}:".format(enemycard))

if sum(mycard)>sum(enemycard):
    print("you_win")

if sum(mycard)<sum(enemycard):
    print("you_loose")

if sum(mycard)==sum(enemycard):
    print("draw")
