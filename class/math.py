import math

class CalcFee:
  def __init__(self):
    """初期化"""
    self.shipping_fee=1000 #送料
    self.tax_rate= 0.08#税率
    self.value = 0#合計

  def additem(self,price):
    """商品の値段を加算"""
    self.value+=price

  def calc(self):
    """最終的　金額"""
    total=self.value + self.shipping_fee
    tax=math.ceil(total*self.tax_rate)
    v=math.ceil(total+tax)
    return v

def main():
  f=CalcFee()
  f.additem(500)
  print(f.calc(),"円")

main()


#print(CalcFee().calc())だとinitのせいでvalueがリセットされてしまうかもしれない
#
