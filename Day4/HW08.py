if __name__ == '__main__':
    def main():
        T = int(input())
        S = 0
        for i in range(T):
            N = int(input())
            if N:
                S += 1
            else:
                S -= 1
        if S > 0:
            print("Junhee is cute!")
        else:
            print("Junhee is not cute!")


    main()
