class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"안녕하세요! 저는 {self.name}입니다. 나이는 {self.age}살입니다!")


if __name__ == '__main__':
    def main():
        ted = Person("송기태", 19)
        ted.introduce()


    main()
