if __name__ == '__main__':
    def main():
        travel_list = []
        while True:
            print("=" * 30)
            print("여행 장소 관리 프로그램")
            print("=" * 30)
            print("1. 여행 장소 목록 출력하기")
            print("2. 여행 장소 추가하기")
            print("3. 여행 장소 삭제하기")
            print("4. 프로그램 종료하기")
            cmd = int(input("메뉴를 선택하세요: "))
            if cmd == 1:
                print(f"|> 여행 장소 목록: {travel_list}")
            elif cmd == 2:
                travel_list.append(input("|> 추가할 여행 장소를 입력하세요: "))
            elif cmd == 3:
                travel_list.remove(input("|> 삭제할 여행 장소를 입력하세요: "))
            elif cmd == 4:
                break
            print()


    main()
