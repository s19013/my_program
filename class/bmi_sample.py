#bmi計算
class BMI:
    def __init__(self,weight,height):
        """初期化"""
        self.weight=weight
        self.height=height
        self.calcBMI()

    def calcBMI(self):
        """計算"""
        h=self.height/100
        self.bmi=self.weight/(h**2)

    def printjudge(self):
        """結果"""
    #後でreturnにかえる
        print("---")
        print("bmi=",self.bmi)
        b=self.bmi
        if (b<18.5): print("痩せ")
        elif (b<25):print("標準")
        elif(b<30):print("肥満（軽）")
        else:print("肥満（重）")


p1=BMI(weight=65,height=165)
p1.printjudge()
