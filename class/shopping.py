import math

class CalcFee:
  def __init__(self):
    """初期化"""
    self.shipping_fee=1000 #送料
    self.tax_rate= 0.08#税率
    self.value = 0#合計
    self.sppedy =500 #速達

  def additem(self,price):
    """商品の値段を加算"""
    self.value+=price

  def calc(self,ques):
    """最終的　金額"""
    self.ques=ques
    total=self.value + self.shipping_fee
    if ques=="n":
        pass
    else:
        total+=self.sppedy
    tax=math.ceil(total*self.tax_rate)
    v=math.ceil(total+tax)
    return v

def main():
    shop=CalcFee()
    while True:
        itemlist={"a":200,"b":300,"c":400}
        print("qで終了")
        se_item=input("欲しいものを入力\n{}\n".format(itemlist))

        if se_item in itemlist:
            count=int(input("個数は？\n"))
            for i in range(count):
                shop.additem(itemlist[se_item])
        elif se_item=="q":
            break
        else:
            print("やり直し")
    while True:
        ques_sppedy=input("速達をご希望ですか？\n y/n:")
        if ques_sppedy=="y":
            print("合計{}円です".format(shop.calc("y")))
            break
        elif ques_sppedy=="n":
            print("合計{}円です".format(shop.calc("n")))
            break
        else:
            print("やり直し")
    print("注文を承りました\nご利用ありがとう御座いました")

main()
