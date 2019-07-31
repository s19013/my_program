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
            v+=i.getscore
        ave_v= v/len(self.students)
        return ave_v

p1=inf_Student
