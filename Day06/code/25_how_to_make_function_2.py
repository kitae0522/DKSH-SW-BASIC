def quadratic_formula(a, b, c):
    r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    return r1, r2

if __name__ == '__main__':
    def main():
        r1_1, r1_2 = quadratic_formula(1, 2, -8)
        r2_1, r2_2 = quadratic_formula(2, -6, -8)
        print(f'1. 해는 {r1_1} 또는 {r1_2}이다.')
        print(f'2. 해는 {r2_1} 또는 {r2_2}이다.')
            
    main()
