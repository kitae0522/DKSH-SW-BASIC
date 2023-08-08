import random

if __name__ == '__main__':
	def main():
		score = 0
		while True:
			computer_area = random.randint(1, 5)
			user_area = int(input("수비할 위치를 입력하세요 (1: 좌상단, 2: 좌하단, 3: 중앙, 4: 우상단, 5: 우하단, 6: 종료): "))
			if user_area == 6:
				break			
			if computer_area != user_area:
				print("수비를 실패했습니다. 실점했습니다.")
				score -= 1
			else:
				print("수비에 성공했습니다!")
				score += 1
		print(f"최종 점수: {score}점")
	main()