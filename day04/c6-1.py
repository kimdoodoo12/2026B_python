



# 구문 오류 : 실행 전 오류, 실행 자체 불가능
# 런타임 오류: 실행중 오류, 예외

print('프로그램 시작')

# list_a[1] 실행중 오류

# input이 int로 형변환이 되는데 만약 사용자가 숫자가 아닌 다른 자료를 입력한 경우 예외가 발생
number_input_a = int(input("정수입력> "))

user_input_a = input("정수입력> ")
if user_input_a.isdigit():
    user_input_a = number_input_a

    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2*3.14*number_input_a)

else:
    print('정수를 입력하지 않았음')


try:
    number_input_b = int(input("정수 입력"))
    print("원의 반지름:", number_input_b)
    print("원의 둘레:", 2*3.14*number_input_b)
except:
    print("무언가 잘못됨")



list_input_a = ["52", "274", "32", "스파이", "103"]

list_number = []
for item in list_input_a:
    try:
        float(item) # 예외가 발생하면 다음으로 진행은 안됨
        list_number.append(item) # 예외없이 통과했으면 새로운 리스트 대입
    except:
        pass

print("{}내부에 있는 숫자는".format(list_input_a))
print("{}입니다".format(list_number))


try:
    number_input_b = int(input("정수입력> "))
except:
    print("정수를 입력하지 않음")
else:
    print("원의 반지름:", number_input_b)
    print("원의 둘레:", 2*3.14*number_input_b)
finally:
    print("일단 프로그램이 어떻게든 끝났습니다")

    #try내부에서 return으로 끝나도 finally 구문은 무조건 실행이 됨

