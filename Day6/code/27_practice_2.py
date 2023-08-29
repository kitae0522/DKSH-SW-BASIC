def div_mod(n1, n2):
    if n1 > n2:
        return n1 // n2, n1 % n2
    return n2 // n1, n2 % n1

if __name__ == '__main__':
    def main():
        a, b = 5, 2
        print(div_mod(a, b))
        print(div_mod(b, a))
        
    main()
