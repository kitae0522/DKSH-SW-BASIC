class Country:
    def __init__(self, name, population, capital):
        self.name = name
        self.population = population
        self.capital = capital

    def show(self):
        print("부모 클래스입니다.")


class Korea(Country):
    def __init__(self, name, population, capital):
        super().__init__(name, population, capital)
        self.greeting = "안녕하세요!"

    def greet(self):
        print(self.greeting)


class Japan(Country):
    def __init__(self, name, population, capital):
        super().__init__(name, population, capital)
        self.greeting = "こんにちは!"

    def greet(self):
        print(self.greeting)


if __name__ == '__main__':
    def main():
        korea_obj = Korea("대한민국", 51_740_000, "서울")
        japan_obj = Japan("일본", 125_700_000, "도쿄")
        korea_obj.show()  # 출력 결과: 부모 클래스입니다.
        korea_obj.greet()  # 출력 결과: 안녕하세요!
        print(japan_obj.population)  # 출력 결과: 125700000
        japan_obj.greet()  # 출력 결과: こんにちは!


    main()
