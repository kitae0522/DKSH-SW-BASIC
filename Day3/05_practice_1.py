if __name__ == '__main__':
	def main():
		price_pencil = 2000
		price_pen = 3000
		num_pencil = int(input("구매할 연필의 개수를 입력하세요: "))
		num_pen = int(input("구매할 펜의 개수를 입력하세요: "))
		total_price = price_pencil * num_pencil + price_pen * num_pen

		if total_price > 20000:
			total_price *= 0.9
			print("20,000원이 넘어가게 되어, 10% 할인 되셨습니다!")
		print(f"총합: {int(total_price)}원")
	main()