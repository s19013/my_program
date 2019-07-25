#プレーヤーの動き
class Person:
    def __init__(self, building):
        self.building = building    # 現在地
        print(f"{self.building.name}にいる")

    def move(self, building):
        self.building = building    # 現在地の更新
        print(f"{self.building.name}に移動した")

    def eat(self):
        print(f"{self.building.serve()}を食べた")

    def study(self):
        if self.building.study:
            print(f"{self.building.teach()}を勉強した")

    def sleep(self):
        if self.building.has_bed:
            print("今日はもう寝よう\nおやすみ")

    #def taklking(self):
    #    print()


# ここから建物
class Home:
    has_bed = True

    def __init__(self):
        self.name = "マイホーム"

class library:
    study = True

    def __init__(self):
        self.name="図書館"

    def teach(self):
