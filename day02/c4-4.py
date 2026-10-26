numbers = [103, 52, 273, 32, 77]

print(min(numbers))
print(max(numbers))
print(sum(numbers))

numbers_reversed = reversed(numbers)
print(*numbers_reversed)
print(type(numbers_reversed))
print(type(numbers))
print(numbers)


# 이터러블 : 요소들을 하나씩 차례로 꺼내기 가능한 객체 의미
# 이터레이터: 이터러블 중에서 하나씩 차례로 빼낼 수 있는 요소
# 이터레이터 포함된 타입 : 리스트 / 딕셔너리 / 문자열 / 튜플 등
# 이터레이터 하나씩 꺼내는 함수 = next() 함수

print(enumerate(numbers))
print(*enumerate(numbers))
print(list(enumerate(numbers)))

for index, value in enumerate(numbers):
    print(index, value)


dict_a = {"name":"kimdoodoo", "age": 25}
for key, value in dict_a.items():
    print(key, value)


array = [1, 2, 3, 4, 5]
output = [1 for item in array if item != 1]
print(output)

test = [i * i for i in range(0, 20, 2)]
print(test)

print("\n".join(["안녕하세요1", "안녕하세요2"]))
print("-".join("유재석"))


output = [x for x in range(1, 101) if "{:b}".format(x).count("0") == 1]
for i in range(1, 101):
    print("{} : {}".format(i, "{:b}".format(i)))
print("합계:", sum(output))