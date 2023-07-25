"""
우리는 항상 파이썬 파일을 만들 때

if __name__ == '__main__':
    def main():
        pass


    main()

으로 형태를 짜주고, def main() 안에서 코드를 짤 것이다.
항상 새로운 파일을 만들면 위와 같이 적어두도록 하자.

이유는 나중에 다시 설명한다.

<출력문>
print($[something], sep=' ', end='\n') : $[something]을 ' '으로 구분하고, 끝에 '\n'을 추가하여 출력하는 함수이다.
이때, sep과 end는 print 함수의 옵션으로 넣어줘도 되고 안 넣어준다면 default 값이 들어간다.
$[something]의 갯수는 몇개가 되든지 맘껏 넣어도 된다.

print("Hello") # $[something]으로 "Hello"가 들어간 경우
print(1) # $[something]으로 1이 들어간 경우
print(1+1) # $[something]으로 1+1의 연산 결과가 들어간 경우
print(1, 2, 3) # $[something]으로 1, 2, 3을 넣은 경우, sep=' '이므로 1 2 3이 출력된다.
print(1, 2, 3, sep=' | ') # $[something]으로 1, 2, 3을 넣은 경우, sep=' | '이므로 1 | 2 | 3이 출력된다.

<입력문>
input($[something]) : $[something]을 출력하고, 입력받은 값을 문자열로 리턴함.
input("한 가지 정수를 입력하시오. > ") # "한 가지 정수를 입력하시오. > "를 출력하고 값을 입력받음.
input(1) # "1"을 출력하고 값을 입력받음.
"""

if __name__ == '__main__':
    def main():
        pass


    main()
