if __name__ == '__main__':
    def main():
        name = input("당신의 이름은 무엇인가요? : ")
        age = int(input(f"{name}님 반가워요! 나이는 어떻게 되세요? : "))
        _ = input(f"이제 나이가 바뀌어서 {age - 2}살이거나 {age - 1}살이시겠네요. : ")
        school = input("그렇다면, 현재 어디 학교에 다니고 계신가요? : ")
        school = school[0:school.find("교") + 1]
        print(f"{school}에 재학 중이시군요. 좋은 하루 보내세요!")


    main()
