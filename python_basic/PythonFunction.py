# 점수에 대한 성적을 출력한다.
def printGrade(score):
    if score >= 90.0:
        print('A')
    elif score >= 80.0:
        print('B')
    elif score >= 70.0:
        print('C')
    elif score >= 60.0:
        print('D')
    else:
        print('F')

def main():
    score = eval(input("Input your score: "))
    print("Your grade is", end = " ")
    printGrade(score)

main() # main 함수를 호출한다.
