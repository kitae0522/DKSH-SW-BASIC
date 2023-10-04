def linear_search(num_list, key):
    for idx, item in enumerate(num_list):
        if key == item:
            return idx
    return -1


if __name__ == "__main__":
    def main():
        numbers = [8, 31, 48, 73, 3, 11]
        where_is_73 = linear_search(numbers, 73)
        print(f"{where_is_73}번째 인덱스에 73이 있습니다.")


    main()
