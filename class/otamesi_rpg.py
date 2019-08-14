#import rpg3
class aaa:
    def __init__(self,b):
        self.b=b
    def p(self):
        print(self.b)
    def bbb(self,au):
        self.b-=au
        return self.b

hum=aaa(100)
for i in range(5):
    print(hum.bbb(10))
    hum.p()
