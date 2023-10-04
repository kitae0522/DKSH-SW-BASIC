if __name__ == "__main__":
    def main():
        N, M = map(int, input().split())
        V = []
        C = {}
        for _ in range(N):
            st = input()
            if len(st) >= M:
                V.append(st)
                if st in C:
                    C[st] += 1
                else:
                    C[st] = 1
        V = sorted(V, key=lambda x: (-C[x], -len(x), x))
        for i in range(len(V)):
            if i == 0 or V[i - 1] != V[i]:
                print(V[i])


    main()
