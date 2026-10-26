
print(range(5))

print(list(range(5)))

print(list(range(3, 6)))

print(list(range(0, 10, 2)))


for i in range(1, 11, 2):
    print(i)

print(list(range(7,0,-1)))

key_list = ["name", "hp"]
value_list = ["기사", 30]
character = {}

for key, value in key_list, value_list:
    character[key] = value

print(character)

limit = 10000
sum_value = 0
i = 1
for i in range(1, 10000):
    if (sum_value > limit):
            break
    sum_value += i

print("{}를 더할 때, {}을 넘으면 그때의 값은 {}입니다".format(i-1, limit, sum_value))

max_value = 0
a = 0
b = 0

for i in range(1, 100):
     j = 100 - i
     if (j * i > max_value):
          max_value = j * i
          a = j
          b = i
print("최대가 되는 경우: {} * {} = {}".format(a, b, max_value))