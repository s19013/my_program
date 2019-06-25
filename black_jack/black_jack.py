import random
import sys

def game():
    def battle(yourcard,comcard):
        if yourcard > comcard:
            print("勝ち")
        elif yourcard <comcard:
            print("負け")
    yourcard=[]
    comcard=[]
    for i in range(2):
        yourcard.append(random.randint(1,13))
        comcard.append(random.randint(1,13))
    print("あなたの手札{}\n計{}".format(yourcard,sum(yourcard)))
#--------------------------------------------------------------
    def myturn():
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
    def comturn():
        while sum(comcard)<18:
            comcard.append(random.randint(1,13))
            if sum(comcard)>21:
                global com_barst
                return True
                break
            elif 18 <= sum(comcard) <=21:
                return sum(comcard)
                break
        print("あいての手札{}\n計{}".format(comcard,sum(comcard)))
#--------------------------------------------------
    if com_barst==True:
        print("相手がバーストしました\nあなたの勝ちです")
        sys.exit()
    else:
        battle(yourcard,comcard)


#--------------------------------------------------

#-------------------------------------------------
game()
