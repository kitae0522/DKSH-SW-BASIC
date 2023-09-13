class Dog:
    name = ""
    age = 0
    breed = ""
    fur_color = ""

    def run(self):
        print(self.name + ": 헥헥")

    def bark(self):
        print(self.name + ": 멍멍")


if __name__ == '__main__':
    def main():
        dog1 = Dog()
        dog1.name = "산체"
        dog1.age = 1
        dog1.breed = "치와와"
        dog1.fur_color = "갈색"
        dog1.run()

        dog2 = Dog()
        dog2.name = "밍키"
        dog2.age = 1
        dog2.breed = "푸들"
        dog2.fur_color = "회색"
        dog2.bark()


    main()
