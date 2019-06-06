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
yourcard=[a,b]

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

#player
print("yourcard:{} sum[{}]\n".format(yourcard,sum(yourcard)))
h_or_s=input("hit or stand?\n(please enter alphabet: hit=h, stand=s):")



if h_or_s=="h" and sum(yourcard)<=21:
    yourcard.append(c)
    print("yourcard:{} sum[{}]\n".format(yourcard,sum(yourcard)))
    h_or_s=input("hit or stand?\n(please enter alphabet: hit=h, stand=s):")
    if h_or_s=="h" and sum(yourcard)<=21:
        yourcard.append(d)
        print("yourcard:{} sum[{}]\n".format(yourcard,sum(yourcard)))
        h_or_s=input("hit or stand?\n(please enter alphabet: hit=h, stand=s):")
        if h_or_s=="h" and sum(yourcard)<=21:
            yourcard.append(e)
            print("yourcard:{} sum[{}]\n".format(yourcard,sum(yourcard)))
            h_or_s=input("hit or stand?\n(please enter alphabet: hit=h, stand=s):")
            if h_or_s=="h" and sum(yourcard)<=21:
                yourcard.append(f)
                print("yourcard:{} sum[{}]\n".format(yourcard,sum(yourcard)))
                h_or_s=input("hit or stand?\n(please enter alphabet: hit=h, stand=s):")
                if h_or_s=="h" and sum(yourcard)<=21:
                    yourcard.append(g)
                    print("yourcard:{} sum[{}]\n".format(yourcard,sum(yourcard)))
                    h_or_s=input("hit or stand?\n(please enter alphabet: hit=h, stand=s):")
                    if h_or_s=="h" and sum(yourcard)<=21:
                        yourcard.append(h)
                        print("yourcard:{} sum[{}]\n".format(yourcard,sum(yourcard)))
                        h_or_s=input("hit or stand?\n(please enter alphabet: hit=h, stand=s):")
                        if h_or_s=="h" and sum(yourcard)<=21:
                            yourcard.append(i)
                            print("yourcard:{} sum[{}]\n".format(yourcard,sum(yourcard)))
                            h_or_s=input("hit or stand?\n(please enter alphabet: hit=h, stand=s):")
                            if h_or_s=="h" and sum(yourcard)<=21:
                                yourcard.append(j)
                                print("yourcard:{} sum[{}]\n".format(yourcard,sum(yourcard)))
                                h_or_s=input("hit or stand?\n(please enter alphabet: hit=h, stand=s):")
                                if h_or_s=="h" and sum(yourcard)<=21:
                                    yourcard.append(k)
                                    print("yourcard:{} sum[{}]\n".format(yourcard,sum(yourcard)))
                                    h_or_s=input("hit or stand?\n(please enter alphabet: hit=h, stand=s):")


if sum(yourcard) > 21:
    print("yourcard:{} sum[{}]\n".format(yourcard,sum(yourcard)))
    sys.exit("barst  game_over")

#enemy
if h_or_s=="s":
    print("enemy's_turn　please_wait\n")
    print("enemycard(now){} sum[{}]".format(enemycard,sum(enemycard)))

if sum(enemycard)<=17:
    enemycard.append(ec)
    if sum(enemycard)<=17:
        enemycard.append(ed)
        if sum(enemycard)<=17:
            enemycard.append(ee)
            if sum(enemycard)<=17:
                enemycard.append(ef)
                if sum(enemycard)<=17:
                    enemycard.append(eg)
                    if sum(enemycard)<=17:
                        enemycard.append(eh)
                        if sum(enemycard)<=17:
                            enemycard.append(ei)
                            if sum(enemycard)<=17:
                                enemycard.append(ej)
                                if sum(enemycard)<=17:
                                    enemycard.append(ek)

if sum(enemycard) > 21:
    print("enemy was barsted {} sum[{}]\n you_win".format(enemycard,sum(enemycard)))
    sys.exit()


#battle
if sum(enemycard) > 17:
    print("open_card\n")
    print("yourcard:{} sum[{}]  enemycard:{} sum[{}]".format(yourcard,sum(yourcard),enemycard,sum(enemycard)))

if sum(yourcard)>sum(enemycard):
    print("you_win")

if sum(yourcard)<sum(enemycard):
    print("you_loose")

if sum(yourcard)==sum(enemycard):
    print("draw")
