class Parent:
    def display(self):
        print("부모입니다.")


class Child(Parent):
    def display(self):
        print("자식입니다.")


if __name__ == '__main__':
    def main():
        app = Child()
        app.display()  # 출력 결과: 자식입니다.


    main()
