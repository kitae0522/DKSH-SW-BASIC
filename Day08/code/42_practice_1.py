class Person:
    name = ""
    age = ""

    def introduce(self):
        print(f"안녕하세요! 저는 {self.name}입니다. 나이는 {self.age}살입니다!")


if __name__ == '__main__':
    def main():
        ted = Person()
        ted.name = "송기태"
        ted.age = 19
        ted.introduce()


    main()
