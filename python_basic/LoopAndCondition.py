import random

# 사용자가 맞춰야하는 마법수를 생성한다.
number = random.randint(1, 100)

print("0과 100 사이의 마법수를 맞춰보세요.")

guess = -1
while guess != number:
    # 사용자로부터 추측값을 입력받는다.
    guess = eval(input("마법수는 무엇일까요?: "))

    if guess == number:
        print("정답, 마법수는", number, "입니다.")
    elif guess > number:
        print("너무 큽니다.")
    else:
        print("너무 작습니다.")

