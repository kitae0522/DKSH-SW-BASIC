"""
선택 정렬 알고리즘 [오름차순]

좌측 요소에 인덱스를 고정한 뒤 나머지 요소와 비교하여 최소값으로 교체
한 회전이 끝나면 좌측 요소는 비교 대상 중 가장 작은 값으료 교체되어 있음

원본: [9, 4, 5, 7, 2]

i = 0 , j = 1     [9, 4] 교체     [4, 9, 5, 7, 2]
        j = 2     [4, 5] 유지     [4, 9, 5, 7, 2]
        j = 3     [4, 7] 유지     [4, 9, 5, 7, 2]
        j = 4     [4, 2] 교체     [2, 9, 5, 7, 4]
[1회전 끝. i의 요소에 비교 대상 중 최소값 위치]

i = 1 , j = 2     [9, 5] 교체     [2, 5, 9, 7, 4]
        j = 3     [5, 7] 유지     [2, 5, 9, 7, 4]
        j = 4     [5, 4] 교체     [2, 4, 9, 7, 5]
[2회전 끝. i의 요소에 비교 대상 중 최소값 위치]

i = 2 , j = 3     [9, 7] 교체     [2, 4, 7, 9, 5]
        j = 4     [7, 5] 교체     [2, 4, 5, 9, 7]
[3회전 끝. i의 요소에 비교 대상 중 최소값 위치]

i = 3 , j = 4     [9, 7] 교체     [2, 4, 5, 7, 9]
[4회전 끝, i의 요소에 비교 대상중 최소값 위치]
"""


def selection_sort(num_list):
    for i in range(len(num_list)):
        min_idx = i
        for j in range(i + 1, len(num_list)):
            if num_list[j] < num_list[min_idx]:
                min_idx = j
        num_list[i], num_list[min_idx] = num_list[min_idx], num_list[i]


if __name__ == "__main__":
    def main():
        numbers = [9, 4, 5, 7, 2]
        selection_sort(numbers)
        print(f"최종 결과 = {numbers}")


    main()
