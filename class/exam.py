class inf_Student:
    """生徒を表す"""
    def __init__(self,id,name,score=0):
        """初期化"""
        self.id=id
        self.name=name
        self.score=score

    def getid(self):
        return self.id

    def getname(self):
        return self.name

    def setscore(self,score):
        """点数を取得"""
        self.score=score

    def getscore(self):
        """点数を設定"""
        return self.score

class CalcScore:
    """点数を計算"""
    def __init__(self):
        """初期化"""
        self.students=[]

    def addstudent(self,student):
        """学生を追加"""
        self.students.append(student)

    def ave(self):
        v=0
        for i in self.students:
            v+=i.getscore()
        ave_v= v/len(self.students)
        return ave_v

p1=inf_Student(10, "satou",score=80)
p2=inf_Student(11, "sasori",score=79)
p3=inf_Student(12, "ouki",score=84)
p4=inf_Student(13, "touwa",score=77)

calc=CalcScore()
calc.addstudent(p1)
calc.addstudent(p2)
calc.addstudent(p3)
calc.addstudent(p4)
print("ave=",calc.ave())
