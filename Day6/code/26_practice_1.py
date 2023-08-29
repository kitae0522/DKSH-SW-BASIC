def find_max(n1, n2):
    if n1 > n2:
        return n1
    return n2

    # 삼항연산자를 이용하면, 한 줄 컷을 낼 수 있다. 하지만 가독성에는 좋지 않으니 주의할 것
    # return n1 if n1 > n2 else n2

if __name__ == '__main__':
    def main():
        a, b = 1, 2
        print(find_max(a, b))
        
    main()
