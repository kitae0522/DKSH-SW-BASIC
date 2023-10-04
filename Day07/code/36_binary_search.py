def binary_search(num_list, key):
    left = 0
    right = len(num_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if num_list[mid] < key:
            left = mid + 1
        elif num_list[mid] > key:
            right = mid - 1
        else:
            return mid
    return -1


if __name__ == "__main__":
    def main():
        numbers = [1, 3, 8, 11, 31, 48, 73]
        where_is_31 = binary_search(numbers, 31)
        print(f"{where_is_31}번째 인덱스에 31이 있습니다.")


    main()
