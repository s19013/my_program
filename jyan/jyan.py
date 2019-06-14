import random
import sys

# 判定とコンピュータの処理を短くする
#

hand={1:"グー",2:"チョキ",3:"パー"}

def print_result(your_hand,com_hand):
    print("あなた:{} com:{}".format(your_hand,com_hand))


while True:
    print("じゃんけん")
    # you
    print("{}\n数字を入力してください:".format(hand))
    your_num=int(input())


    com_num=random.randint(1,3)

    print_result(hand[your_num],hand[com_num])

    
