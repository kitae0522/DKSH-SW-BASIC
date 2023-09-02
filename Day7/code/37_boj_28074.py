if __name__ == "__main__":
    def main():
        MOBIS = ("M", "O", "B", "I", "S")
        word = input()
        result = True
        for item in MOBIS:
            if item not in word:
                result = False
                break
        print("YES" if result else "NO")


    main()
