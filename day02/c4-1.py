
# 리스트란? 대괄호[]에 자료를 쉼표로 구분하여 여러 자료들을 저장
# [요소, 요소, 요소], 요소=element
# 인덱스란? 리스트내 요소들이 저장된 순서번호, 0번 시작


list_A = [273, 32, 103, "문자열", True, False]
print(list_A[3])
print(list_A[1:3]) # 1~2 # [32, 103] 슬라이싱
list_A[2] = 7 # 수정

print(list_A[3][1]) # 문자열은 리스트로 '자'가 출력
# print(list_a[1][1]) # 에러

list_2 = [[1,2], [3,4], [5,6]] # 2차원
list_3 = [[[1,2], [3, 4]], [5,6]] # 3차원
print(list_2[1][0])

list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(list_a+list_b)
print(list_a[0] + list_b[0])
print(list_a*3)
print(len(list_a)) # 3

list_aa = [[1] , [2], [3]]
print(list_a+list_aa) # [1, 2, 3, [1], [2], [3]]

list_a.insert(0, 5)
list_a.append(4)

list_c = [1, 2]
list_c + [3]    # 방법 1 [1, 2, 3] 새로운 리스트 생성, 파괴적
print("1번째 방법: ", list_c)
list_c.append(3)    # 방법 2 [1, 2, 3] 기존 리스트 유지, 비파괴적
print("2번째 방법: ", list_c)

list_a = [1, 2, 3, 4, 5]
del list_a[1]
list_a.pop(2) # 2번 인덱스 삭제
print(list_a) # [1, 3, 5]

del list_a[0 : 2] # del 키워드 이용한 슬라이싱 삭제
print(list_a)

list_a.remove(5) # 5라는 값이 존재하면 삭제
print(list_a)

list_a.clear() # 리스트 전체 삭제

list_a = [1, 2, 3, 4, 5]
del list_a[3:]
print(list_a)

# 슬라이싱, [시작인덱스 : 끝 인덱스 : 단계]
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(numbers[0 : 5 : 2]) # 0번부터 5~1번까지 2씩 증가 [ 1, 3 , 5]
print(numbers[: : -1]) # 시작 인덱스 생략시 0, 끝 인덱스 생략시 마지막 인덱스
print(numbers[:: -1])

# 정렬, 리스트명.sort(), 리스트명.sort(reverse=True)
list_e = [52 , 12, 421, 341, 22, 113, 21]
list_e.sort()
print(list_e)
list_e.sort(reverse=True)
print(list_e)


# 내부 확인, 찾을 값 in 리스트
print(52 in list_e)
print(52 not in list_e)

for i in list_e:
    print(i)
for char in "안녕하세요":
    print(char)


for i in range(1, 10):
    for j in range(1, 10):
        print(i, "*", j, "=", i*j)

# for (int i = 1; i < 10; i++){
#     for (int j = 1; j < 10; j++){
#         System.out.println(i + "*" + j + "=" + i*j)
#     }
# }
numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
counter = {}
for number in numbers:
    if number in numbers:
        counter[number] = counter.get(number, 0) + 1

print(counter)
print(type(counter.get(1)))

for item in counter:
    print(counter.get(item))