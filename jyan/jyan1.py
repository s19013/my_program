import random
import sys

hand={0:"グー",1:"チョキ",2:"パー"}



def juge(your_nums,com_nums):
    jugemath=(your_nums-com_nums+3)%3
    if your_nums==com_nums:
        return "あいこ"
    if jugemath==1:
        return "負け"
    if jugemath==2:
        return "勝ち"


def aiko():
    while True:
        print("------------------------")
        print("あいこで")
        print(hand)
        #↓ここの（com_num）がさっきのと同じやつしかださない
        com_num2 = random.randint(0, 2)
        your_num2 = int(input())
        # if文入れるよ
        if your_num2 == 0 or your_num2 == 1 or your_num2 == 2:
            break


def print_result(your_hand,com_hand):
  print("\nあなた:{} com:{}".format(hand[your_num],hand[com_num]))

while True:
    print("------------------------")
    print("\nじゃんけん")
    while True:
        print("{}\n数字を入力してください:".format(hand))
        your_num = int(input())
        com_num = random.randint(0, 2)
        # if文入れるよ
        if your_num == 0 or your_num == 1 or your_num == 2:
            break
    print("------------------------")
    print_result(your_num,com_num)
    print(juge(your_num,com_num))
    #if juge(your_num,com_num)=="あいこ":
        #この場合のあいこを考える
        #while True:
            #aiko()
            #print("------------------------")
            #print_result(your_num2,com_num2)
            #print(juge(your_num2,com_num2))
            #if juge(your_num2,com_num2)!="あいこ":
                #break
    print("------------------------")
    cont=input("コンテニュー？(y/n)\n")
    c=cont.upper()
    if c=="Y" or c=="YES":
        break
