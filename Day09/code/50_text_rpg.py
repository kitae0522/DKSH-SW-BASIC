import random
import math


class Object:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power
        self.ability_power = 0

    def attack(self, target_class):
        print(f"{self.name}이 {target_class.name}을 {self.power}만큼 공격했습니다!")
        target_class.hp -= self.power
        if self.is_dead(target_class):
            print(f"{target_class.name}을 물리쳤습니다!")
        else:
            print(f"{target_class.name}을 물리치지 못했습니다.")

    def is_dead(self, target_class):
        if target_class.hp <= 0:
            return True
        return False


class Player(Object):
    def __init__(self, name, hp, power, job):
        super().__init__(name, hp, power)
        self.job = job
        self.money = 0
        self.critical_hit_probability = 0.3


class Warrior(Player):
    def __init__(self, name, hp, power, job):
        super().__init__(name, hp, power, job)

    def attack(self, target_class):
        dmg = self.power
        if self.critical_hit_probability > random.random():
            dmg = math.ceil(dmg * 1.5)
            print(f"크리티컬!")
        print(f"{self.name}이 {target_class.name}을 {dmg}만큼 공격했습니다!")
        target_class.hp -= dmg
        if self.is_dead(target_class):
            print(f"{target_class.name}을 물리쳤습니다!")
        else:
            print(f"{target_class.name}을 물리치지 못했습니다.")


class Wizard(Player):
    def __init__(self, name, hp, power, job):
        super().__init__(name, hp, power, job)
        self.ability_power = power + 1
        self.power = 0

    def attack(self, target_class):
        print(f"{self.name}이 {target_class.name}을 {self.ability_power}만큼 공격했습니다!")
        target_class.hp -= self.ability_power
        if self.is_dead(target_class):
            print(f"{target_class.name}을 물리쳤습니다!")
        else:
            print(f"{target_class.name}을 물리치지 못했습니다.")


class Monster(Object):
    def __init__(self, name, hp, power):
        super().__init__(name, hp, power)

    def cure(self):
        add_hp = random.randint(1, 5)
        self.hp += add_hp
        print(f"{self.name}이 {add_hp}만큼 회복했습니다!")


class TextRPG:
    def __init__(self):
        self.player = None
        self.monster = None

    def print_guide(self):
        print("=" * 30)
        print(f"{self.player.name}의 남은 피: {self.player.hp} / {self.monster.name}의 남은 피: {self.monster.hp}")

    def create_obj(self):
        player_job = int(input("원하는 직업을 선택하세요.\n"
                               "1. 전사\n"
                               "2. 마법사\n"
                               ">> "))
        nickname = input("소환사의 이름을 적어주세요.\n"
                         ">> ")
        if player_job == 1:
            self.player = Warrior(nickname, 10, 5, "전사")
        else:
            self.player = Wizard(nickname, 10, 5, "마법사")
        self.monster = Monster("고블린", 25, 3)

    def run(self):
        self.create_obj()
        while True:
            self.print_guide()
            self.player.attack(self.monster)
            if self.monster.hp <= 0:
                break

            self.print_guide()
            monster_next_move = random.choice(["attack", "cure"])
            if monster_next_move == "attack":
                self.monster.attack(self.player)
            else:
                self.monster.cure()

            if self.player.hp <= 0:
                break


if __name__ == '__main__':
    def main():
        app = TextRPG()
        app.run()


    main()
