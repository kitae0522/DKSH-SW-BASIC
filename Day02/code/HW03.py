if __name__ == '__main__':
    def main():
        # 💩
        item = 3
        str(type(item)) == "<class 'int'>" and print(1)
        str(type(item)) == "<class 'float'>" and print(2)
        str(type(item)) == "<class 'str'>" and print(3)

        # isinstance()를 사용해보는 것은 어떨까?
        # isinstance($[ele], $[data_type]) -> bool
        # $[ele]의 자료형이 $[data_type]과 같다면 True를, 아니면 False를 리턴한다.

        # ✅
        item = 3
        isinstance(item, int) and print(1)
        isinstance(item, float) and print(2)
        isinstance(item, str) and print(3)


    main()
