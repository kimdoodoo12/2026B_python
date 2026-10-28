import numpy as np

# 1차원 배열 통계 함수

x = np.array([1,2,3,4,5])
print(np.min(x), np.max(x)) # 최솟값, 최댓값
print(np.argmin(x), np.argmax(x)) # 최소값 위치, 최대값 위치
print(np.sum(x))
print(np.sum(x), np.mean(x), np.median(x)) # 합계 평균 중앙값
print(np.var(x)) # 분산: 평균으로부터  요소 값들이 떨어진 정도
print(np.std(x)) # 표준편차: 분산에 양의 제곱근 사용하여 데이터 단위 맞춘 값
print(np.sqrt(x)) # 양의 제곱근(루트)


# 2차원 배열 통계 함수
# np.통계함수(2차원배열, axis = 생략시 1차원 평탄화, 0이면 열 기준, 1이면 행 기준)
y = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(np.min(y), np.max(y)) # 1 9
print(np.min(y, axis=0), np.max(y, axis=1)) # axis = 0 열 단위 , axis=1 행 단위
print(np.argmin(y), np.argmax(y)) # 1차원 기준으로 인덱스 순번 반환
print(np.sum(y, axis=0), np.sum(y, axis=1))
print(np.sum(y, axis=0), np.mean(y, axis=0), np.median(y, axis=1))
print(np.var(y), np.std(y), np.sqrt(y))
