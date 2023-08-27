if __name__ == '__main__':
    def main():
        # break
        for i in range(1, 6):
            if i == 3:
                print("반복문을 종료합니다.")
                break
            print(f"현재 숫자는 {i}입니다.")

        # continue
        for i in range(1, 6):
            if i == 3:
                print("현재 숫자는 3이므로 건너뜁니다.")
                continue
            print(f"현재 숫자는 {i}입니다.")

        # break 예시
        while True:
            name = input("이름을 입력하세요 (종료하려면 'exit'을 입력하세요): ")
            if name == "exit":
                break
            print(f"안녕하세요. {name}님!")

        # continue 예시
        for i in range(1, 11):
            if i % 2 == 0:
                continue
            print(f"{i}는 홀수입니다.")


    main()
