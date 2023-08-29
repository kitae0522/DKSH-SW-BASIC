def import_1():
    import math
    print(math.sqrt(9))

def import_2():
    from math import sqrt
    print(sqrt(9))

def import_3():
    import time as t
    print(t.time())

if __name__ == '__main__':
    def main():
        import_1()
        import_2()
        import_3()

    main()
