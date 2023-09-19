class A:
    def introduce(self):
        print("A")


class B(A):
    def introduce(self):
        print("B")


class C(A):
    def introduce(self):
        print("C")


class D(B, C):
    pass


if __name__ == '__main__':
    def main():
        x = D()
        x.introduce()  # 출력 결과: B
        print(D.mro())


    main()
