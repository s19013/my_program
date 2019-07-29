# ここからプレイヤー
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
        if self.building.has_teacher:
            print(f"{self.building.teach()}を勉強した")

    def sleep(self):
        if self.building.has_bed:
            print("もう夜だ\nおやすみ")

class Do_first:
    def next(self,player):
        self.player=player
        next=[None,about_me(),Look_around()]
        while True:
            key_do=input("".format(next))
            try:
                next[int(key_do)]
                break
            except:
                print("有効な入力ではありません！")

    def about_me(self):
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

class KyoyoTo(Do_first):
    has_teacher = True
    def __init__(self):
        Do_first().next()


    def teach(self):
        self.name = "教養棟"
        return input("受けたい授業名を入力してください：")

class Restaurant:
    def __init__(self):
        self.name = ""
        self.menu = ""

    def serve(self):
        return self.menu

class HokuShoku(Restaurant):
    def __init__(self):
        self.name = "北部食堂"
        self.menu = "ビュッフェ"

class Chuo(Restaurant):
    def __init__(self):
        self.name = "中央食堂"
        self.menu = "スープカレー"

# ここからメインの処理
def main(player):
    count = 0
    while count < 3:
        player_move(player)
        if player.building.name == "教養棟":
            player.study()
        else:
            player.eat()
        count += 1
    player.move(Home())
    player.sleep()

def player_move(player):
    option = [None , KyoyoTo(), HokuShoku(), Chuo()]
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
