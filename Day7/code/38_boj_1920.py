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
            return 1
    return 0


if __name__ == "__main__":
    def main():
        n = int(input())
        numbers = sorted(list(map(int, input().split())))
        m = int(input())
        targets = list(map(int, input().split()))
        for target in targets:
            print(binary_search(numbers, target))


    main()
