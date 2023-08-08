if __name__ == '__main__':
	def main():
		# 반복 횟수, 가장 높은 점수의 학생의 입력 순서, 높은 점수 비교를 위한 변수
		idx, max_idx, maximum, sum_score = 1, -1, 0, 0
		while idx <= 5:
			score = int(input("성적을 입력하세요: "))
			sum_score += score
			if score > maximum:
				maximum = score
				max_idx = idx
			idx += 1
		print(f"평균: {sum_score / 5}")
		print(f"가장 높은 점수를 입력한 순서: {max_idx}")
	main()