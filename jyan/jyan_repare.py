import random
import sys
def cont(cont):
    while True:
        print("------------------------------")
        print("続けますか？")
        cont=input("(y/n):")
        cont=cont.upper()
        if cont=="N" or cont=="NO":
            break
        elif cont=="Y" or cont=="YES":
            game()
        else:
            print("\n正しいアルファベットを入れてください\n")

#-------------------------------------------------------------------------------------------------
def game():
    def print_result(your_hand,com_hand):
        print("------------------------------\nあなた:{} com:{}".format(hand[your_hand],hand[com_hand]))
    def juge(your_num,com_num):
        jugemath=(your_num-com_num+3)%3
        if your_num==com_num:
            return "あいこ"
        if jugemath==1:
            return "負け"
        if jugemath==2:
            return "勝ち"
    def aiko():
        while True:
            hand={0:"グー",1:"チョキ",2:"パー"}
            print("\n------------------------")
            print("あいこで")
            print(hand)
        #↓ここの（com_num）がさっきのと同じやつしかださな
            while True:
                try:
                    your_num2 = int(input())
                    com_num2 = random.randint(0, 2)
                    break
                except:
                    print("正しい数字を入れてください")

            print_result(your_num2, com_num2)
            print(juge(your_num2, com_num2))
            if juge(your_num2,com_num2)!="あいこ":
                break

#---------------------------------------------------------------------------------------------
    hand={0:"グー",1:"チョキ",2:"パー"}
    print("------------------------")
    print("じゃんけん")
    while True:
        #なぜtryを使うとifを使わずに処理できるのか調べる
        try:#breakするまで繰り返す
            print("{}\n数字を入力してください:".format(hand))
            your_num = int(input())
            com_num = random.randint(0, 2)
            break;
        except:
            print("正しい数字を入れてください")
    print_result(your_num,com_num)
    print(juge(your_num,com_num))
    if juge(your_num,com_num)=="あいこ":
        aiko()
#------------------------------------------------------------------------------
while True:
    game()
    cont(cont)
    break
