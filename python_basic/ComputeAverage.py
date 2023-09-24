# 사용자로부터 세 개의 숫자를 입력받는다.
number1 = eval(input("첫 번째 숫자를 입력하세요: "))
number2 = eval(input("두 번째 숫자를 입력하세요: "))
number3 = eval(input("세 번째 숫자를 입력하세요: "))

# 평균을 계산한다.
average = (number1 + number2 + number3) / 3

# 결과를 출력한다.
print(number1, number2, number3,
    "의 평균은", average, "입니다.")

