#bmi 計算
box_weight=[]
box_height=[]
class BMI:
    def __init__(self,person,weight,height):
        """初期化"""
        self.person=person
        self.weight=weight
        self.height=height
        self.calcBMI()

    def calcBMI(self):
        """計算"""
        h=self.height/100
        self.bmi=self.weight/(h**2)
        self.printjudge()

    def printjudge(self):
        """結果"""
    #後でreturnにかえる
        print("---")
        print("person{}\nbmi={}".format(self.person,self.bmi))
        b=self.bmi
        if (b<18.5): print("痩せ")
        elif (b<25):print("標準")
        elif(b<30):print("肥満（軽）")
        else:print("肥満（重）")

def input_person():
    #t eは省略
    while True:
        weight=input("体重：")
        if weight=="q":
            break
        else:weight=int(weight)
        height=int(input("身長："))
        box_weight.append(weight)
        box_height.append(height)

    main()

def main():
    for (p,w,h) in zip(range(1,len(box_weight)+1),box_weight,box_height):
        BMI(p,w,h)


input_person()
