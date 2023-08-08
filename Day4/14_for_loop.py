"""
for $[변수] in $[범위]:
    실행할 문장

# 이때 범위는 시퀀스(list, tuple, ....), 문자열 혹은 range() 함수를 사용할 수 있다.
-> 범위에 포함된 각각의 연속되는 요소가 변수에 저장되고 각 요소에 대해 실행할 문장이 한번씩 수행됨.

range(10) -> 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
range(3, 8) -> 3, 4, 5, 6, 7
range(10, 36, 5) -> 10, 15, 20, 25, 30, 35
"""

if __name__ == '__main__':
    def main():
        for char in "Hello World!":
            print(char)
        for item in [1, 2, 3, 4]:
            print(item)
        for idx in range(10):
            print(idx)


    main()
