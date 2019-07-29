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
            print(f"{self.building.stading()}を勉強した")

    def sleep(self):
        if self.building.has_bed:
            print("今日はもう寝よう\nおやすみ")

    #def taklking(self):
    #    print()

class Do_base:
    def do(self,player):
        self.player=player
        next=[None,about_me(),Look_around()]
        if player.building.name=="図書館":
            next.append(studing())
        while True:
            key_do=input("".format(next))
            try:
                next[int(key_do)]
                break
            except:
                print("有効な入力ではありません！")

    def about_me():
        money=6000
        print("{}円".format(money))

    def Look_around():
        print(".....")
        print("知り合いはいないようだ")

# ここから建物
class Home:
    has_bed = True

    def __init__(self):
        self.name = "マイホーム"

class library(Do_base):
    study = True

    def __init__(self):
        self.name="図書館"
        Do_base().do(player)

    def studing(self):
        subject=[None,]
        subject_key=input("")

#メイン
def main(player):
    count = 0
    while count < 3:
        player_move(player)
        count += 1
    player.move(Home())
    player.sleep()

def player_move(player):
    option = [None ,library()]
    while True:
        key = input("どこに移動しますか？　1.{0[1].name} 2.{0[2].name} 3.{0[3].name}：".format(option))
        try:
            player.move(option[int(key)])
            break
        except:
            print("有効な入力ではありません！")

if __name__ == '__main__':
    ore = Person(Home())
    main(ore)
