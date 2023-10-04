if __name__ == '__main__':
    def main():
        a, b, c = 1, 2, -8
        r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
        r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
        print(f'해는 {r1} 또는 {r2}이다.')
        
    main()
