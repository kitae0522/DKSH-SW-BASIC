if __name__ == '__main__':
    def main():
        travel_list = []
        travel_list.append("서울")
        travel_list.append("부산")
        travel_list.append("제주도")
        print(travel_list)

        travel_list.insert(1, "대구")
        print(travel_list)

        travel_list2 = ["일본", "스페인", "영국"]
        travel_list.extend(travel_list2)
        print(travel_list)

        travel_list.remove("대구")
        print(travel_list)


    main()
