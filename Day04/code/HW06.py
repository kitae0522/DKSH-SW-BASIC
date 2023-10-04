if __name__ == '__main__':
    def main():
        x = int(input())
        for i in range(x + 1):
            for j in range(x - i):
                print("*", end="")
            print()


    main()
