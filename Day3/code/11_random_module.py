import random

if __name__ == '__main__':
    def main():
        print(random.random())  # 0.0과 1.0 사이의 부동소수점(float) 난수를 생성한다.
        print(random.randint(1, 10))  # 1과 10 사이 정수(int) 난수를 생성한다. [1, 10]

        list_example = ["봄", "여름", "가을", "겨울"]
        print(random.choice(list_example))  # 주어진 시퀀스에서 임의의 항목을 선택한다. 지금은 그냥 넘어가도 돼요.
        random.shuffle(list_example)  # 주어진 시퀀스의 항목들을 무작위로 섞는다. 이것도 그냥 넘어가도 돼요.
        print(list_example)


    main()
