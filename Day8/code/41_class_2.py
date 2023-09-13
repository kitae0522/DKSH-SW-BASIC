class Dog:
    def __init__(self, name, age, breed, fur_color):
        self.name = name
        self.age = age
        self.breed = breed
        self.fur_color = fur_color

    def run(self):
        print(self.name + ": 헥헥")

    def bark(self):
        print(self.name + ": 멍멍")


if __name__ == '__main__':
    def main():
        dog1 = Dog("산체", 1, "치와와", "갈색")
        dog2 = Dog("밍키", 1, "푸들", "흰색")
        dog1.run()
        dog2.bark()


    main()
