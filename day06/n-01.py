import numpy as np

# 리스트/ 튜플
x = np.array([1, 2, 3, 4])
print(x)
x = np.array([
    [1,2,3],
    [4,5,6]
])
print(x)

# 동적 타입은 느리다. numpy는 정적타입
x = np.array([1, True, "안녕"])
print(x)

# 0으로 배열 초기화, .zeros((행개수, 열개수))
x = np.zeros((2, 3))
# [[0, 0, 0]
#  [0, 0, 0]]
print(x)

# 1으로 배열 초기화 .ones
x = np.ones((2, 3))
print(x)

# range(시작값, 끝 값, 단계)
x = np.arange(0, 10, 2)
print(x)

# linspace(시작값, 끝값, 사이 범위)
x = np.linspace(0, 1, 5)
print(x)

# numpy는 리스트 또는 튜플 타입의 자료들을 numpy 타입으로 변환
x = np.array((2, 3))
print(x)


# 배열 길이 확인
x = np.array([[1, 2, 3], [4, 5, 6]]) # 2차원
print(x.shape) # (2, 3) 2행 3열

# 배열 타입 확인
x = np.array([1.0, 2.0, 3.0])
print(x.dtype) # float64 int64

# 배열 차원/개수 확인
x = np.array([[[1], [2]], [[2],[3]], [[3],[4]]])
print(x.size) # 요수/자료 개수
print(x.ndim) # 차원수

# 배열의 데이터 타입 , np.array(리스트/튜플 , dtype = np.타입명)
# np.타입명(비트수)
# np.bool_ : 언더바 주의(파이썬 bool vs Numpy bool_)
# np.bytes : 영문 또는 일부 특수문자(아스키코드) 1바이트
x = np.array([1,2,3], dtype=np.int64)
print(x.dtype)
x = np.array([1.0 , 2.0, 3.0] , dtype=np.float32)
print(x.dtype)
x = np.array([True, False, True], dtype=np.bool_)
print(x.dtype)
x = np.array(['apple', 'banana', 'cherry222'], dtype=np.bytes_)
print(x.dtype)

# 타입변환  .astype(np.새로운타입)
x = np.array([1.5 , 2.5 , 3.5], dtype=np.float32)
y = x.astype(np.int64)
print(y)

# 타입 지정한 이유 : 1] 메모리 효율성/속도 2] 테서플로우/파이토치 라이브러리