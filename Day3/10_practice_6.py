if __name__ == '__main__':
	def main():
		score = int(input("시험 점수를 입력하세요: "))
		if score >= 90:
			print("A")
		elif score >= 80:
			print("B")
		elif score >= 70:
			print("C")
		else:
			print("D")
	main()