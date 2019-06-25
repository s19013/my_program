import random
import sys

def cont(con):
    while True:
        print("続けますか？")
        con=input("y/n\n")
        con=con.upper()
        if con=="Y" or con=="YES":
            game()
        elif con=="N" or con=="NO":
            break
        else:
            print("\n入力をやり直してください")
def game():
    def battle(yourcard,comcard):
        if yourcard > comcard:
            print("勝ち")
        elif yourcard < comcard:
            print("負け")
        else:
            print("引き分け")
#-----------------------------------------------------
    yourcard=[]
    comcard=[]
    for i in range(2):
        yourcard.append(random.randint(1,13))
        comcard.append(random.randint(1,13))
    print("あなたの手札{}\n計{}".format(yourcard,sum(yourcard)))

#--------------------------------------------------
    while True:
        if sum(yourcard)>21:
            print(sum(yourcard))
            print("バーストしました")
            print("ゲームオーバー")
            sys.exit()
            break
        print("--------------------")
        print("hit_or_stand")
        hs=input("[h]か[s]を入力してください:")
        hs_up=hs.upper()
        if hs_up=="H" or hs_up=="HIT":
            yourcard.append(random.randint(1,13))
            print("-----------------------------------")
            print("あなたの手札{}\n計{}".format(yourcard,sum(yourcard)))
        elif hs_up=="S" or hs_up=="STAND":
            print("-----------------------------------")
            print("相手のターンです。\nしばらくお待ちください")

            break
        else:
            print("\n入力をやり直してください")
#--------------------------------------------------
    while sum(comcard)<17:
        comcard.append(random.randint(1,13))
        if sum(comcard)>21:
            print("-----------------------------------")
            print("相手がバーストしました\nあなたの勝ちです")
            sys.exit()
            break
        elif 17 <= sum(comcard) <=21:
            break
    print("-----------------------------------")
    print("あいての手札{}\n計{}".format(comcard,sum(comcard)))
    print("あなたの手札{}\n計{}".format(yourcard,sum(yourcard)))

    battle(sum(yourcard),sum(comcard))

#--------------------------------------------------

#-------------------------------------------------
while True:
    game()
    cont(cont)
    break
