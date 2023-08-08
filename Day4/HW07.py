if __name__ == '__main__':
    def main():
        while True:
            n, m = map(int, input().split())
            if not n and not m:
                break
            if n > m:
                print("Yes")
            else:
                print("No")


    main()
