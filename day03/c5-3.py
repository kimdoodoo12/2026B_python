

# 특징: 초기화 이후 수정 불가능
# 사용처: 읽기모드용 VO, 리스트보다 메모리 효율좋다
# (요소, 요소, 요소)
# 튜플 선언

tuple_test = (10, 20, 30)

print(tuple_test[0], tuple_test[2])

# 수정은 되지 않음
# tuple_test[0] = 40


tuple_test = 10, 20, 30, 40


a, b = 10, 20
# 스왑 가능
a, b = b, a

# 구조 분해
# name, age = {name: "유재석", age:10}
# name, age = ["유재석", 10]
c, d = [30, 40] 
print(c)


# 함수/연산 결과는 항상 1개
def test():
    return 10, 20 # 결과는 1개 (10과 20을 튜플로 묶은 튜플 1개)

c, d = test()

def call_10_items(func) : # 값 대신에 함수
    func()

def print_hello():
    print("안녕")

call_10_items(print_hello)


# 리스트.stream.forEach(), 리스트.stream.map(), 리스트.steram.filter()

def power(item):
    return item * item

def under_3(item):
    return item < 3

list_input_a = [1, 2, 3, 4, 5]

output_a = map(power, list_input_a)
print(list(output_a))

output_b = filter(under_3, list_input_a)
print(list(output_b))

power = lambda item: item*item

output_a = map(lambda item: item*item, list_input_a)


