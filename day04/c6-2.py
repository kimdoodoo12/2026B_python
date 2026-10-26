
list_number = [52, 273, 32, 72, 100]

# 예외 클래스 : Excpetion (예외 최상위 클래스)

try:
    number_input = int(input("정수입려: "))
    print("{}번째 요소: {}".format(number_input, list_number[number_input]))
except ValueError as e:
    print(e)
except IndexError as e:
    print(e)
except Exception as e: # 최상위 예외는 마지막
    print(e)

# raise: 강제로 예외 발생 , 주로 CRUD 실패 500 의미
number = input("정수를 입력해줘")
number = int(number)
if number > 0:
    raise NotImplementedError
else:
    raise NotImplementedError

