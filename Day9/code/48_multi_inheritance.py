class TouchScreen:
    def touch(self, x, y):
        pass


class Computer:
    def compute(self):
        pass


class MobilePhone(TouchScreen, Computer):
    def __init__(self, size):
        self.size = size

    def touch(self, x, y):
        print(f"x축 {x}, y축 {y}를 터치했습니다.")

    def compute(self):
        print("계산 중입니다.")


if __name__ == '__main__':
    def main():
        phone = MobilePhone(6.1)
        phone.touch(1920, 1080)  # 출력 결과: x축 1920, y축 1080를 터치했습니다.
        phone.compute()  # 출력 결과: 계산 중입니다.


    main()
