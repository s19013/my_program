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
enemycard=[a,b]

print(mycard)
h_or_s=input("hit_or_stand")
if h_or_s=="h":
    mycard.append(c)
    print(mycard)
    h_or_s=input("hit_or_stand")
    if h_or_s=="h" :
        mycard.append(d)
        print(mycard)
        h_or_s=input("hit_or_stand")
        if h_or_s=="h" :
            mycard.append(e)
            print(mycard)
            h_or_s=input("hit_or_stand")
            if h_or_s=="h" :
                mycard.append(f)
                print(mycard)
                h_or_s=input("hit_or_stand")
                if h_or_s=="h" :
                    mycard.append(g)
                    print(mycard)
                    h_or_s=input("hit_or_stand")
                    if h_or_s=="h" :
                        mycard.append(h)
                        print(mycard)
                        h_or_s=input("hit_or_stand")
                        if h_or_s=="h" :
                            mycard.append(i)
                            print(mycard)
                            h_or_s=input("hit_or_stand")
                            if h_or_s=="h" :
                                mycard.append(j)
                                print(mycard)
                                h_or_s=input("hit_or_stand")
                                if h_or_s=="h" :
                                    mycard.append(k)
                                    print(mycard)
                                    h_or_s=input("hit_or_stand")
elif sum(mycard)>21:
    print("barst")
    sys.exit()


if h_or_s=="s":
    print("enemy's_turn")
