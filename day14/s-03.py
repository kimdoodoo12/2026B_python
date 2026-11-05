
# 1] 항 추가하는 함수
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures() # 객체 생성
poly.fit([[2]]) # 특성(2)
print(poly.transform([[2]]))  # [[1. 2. 4.]]
# 2] 절편 제외
poly = PolynomialFeatures(include_bias=False)
poly.fit([[2]])
print(poly.transform([[2]])) # [[2. 4.]]
# 3] 특성 2개 인경우
poly = PolynomialFeatures(include_bias=False)
poly.fit([[2, 3]])          # 특성(2, 3) 규칙
print(poly.transform([[2, 3]])) # 2,3 / 4, 9 / 6

# ** 특성 3개인 경우
poly = PolynomialFeatures()
poly.fit([[2,3,4]])
print(poly.transform([[2,3,4]])) # 2, 3, 4 / 4, 9 , 16 / 6, 12, 8 / 1
# 수동으로 특성의 제곱항을 만들지 않고 자동(PolynomialFeatures)으로 다항 추가

# 다항 회귀 모델
import pandas as pd
df = pd.read_csv('./day13/Fish.csv')
# 1) 특성과 타깃 구성
X = df[['Length2', 'Height', 'Width']]
Y = df['Weight'] # 타깃 1개
# 2) 훈련용/테스트용 분리 8:2
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# 3) 과소적합 방지하고자 다항 만들기 == PolynomialFeatures
poly = PolynomialFeatures(include_bias=False)
poly.fit(X_train) # 학습할 특성들을 규칙(제곱/곱셈)
X_train_poly = poly.transform(X_train)
X_test_poly = poly.transform(X_test)
print(X_train.shape)    # (127, 3) 127, 3(특성)
print(X_train_poly.shape) # (127, 9) 127행 9(특성 -> 항 추가됨 확인)

# 4) 모델 학습
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train_poly, Y_train) # 훈련용 다항이 추가된 특성으로 학습

# 5) 결정 계수
from sklearn.metrics import r2_score
Y_pred = model.predict(X_test_poly) # 테스트용 다항 특성으로 예측
print('r2: ', r2_score(Y_test, Y_pred)) # r2_score(정답지, 예측값)
# r2:  0.9719372415762594

# 3] 다항의 차수 늘리기, degree = 10, 10제곱까지 하여 항 수 늘리기/ 생략시 2제곱
poly = PolynomialFeatures(include_bias=False, degree=10)
poly.fit(X_train)
X_train_poly2 = poly.transform(X_train)
print(X_train_poly2.shape) # 차수2 --> 차수 10 증가에 따른 (127, 9) -> (127, 285)
X_test_poly2 = poly.transform(X_test)
# 학습 후 결정계수 확인

# 4) 모델 학습
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train_poly2, Y_train) # 훈련용 다항이 추가된 특성으로 학습

# 5) 결정 계수
from sklearn.metrics import r2_score
Y_pred = model.predict(X_test_poly2) # 테스트용 다항 특성으로 예측
print('r2: ', r2_score(Y_test, Y_pred)) # r2_score(정답지, 예측값)
# r2:  0.07276663213888512
# *] 모델 구현에서 다양한 속성값
# *] 특성이 너무 많아지면 훈련데이터가 과하게 집합하여 과댁적합이 발생하여 점수가 낮아진다.


# 4] 특성이 많아짐에 따라 특성간의 단위 표준화 (0~1)
from sklearn.preprocessing import StandardScaler
ss = StandardScaler() # 객체 생성
ss.fit(X_train_poly) # 다항 추가 된 학습 특성
X_train_scaled = ss.transform(X_train_poly)
X_test_scaled = ss.transform(X_test_poly)    
print(X_train_poly[0]) # [ 16.2          4.5924       2.6316 ... ]
print(X_train_scaled[0]) # [-1.14878727 -1.06273398 -1.10441696 ... ]
# 평균보다 작으면 음수, 평균+1편준보다 크면 1이상

# 5] 규제 : 기울기(가중치) 크기에 페널티를 부여 하여 특성 오차 확인하여 특성 완만/제외
# 1) 릿지
from sklearn.linear_model import Ridge
# 2) alpha(규제강도) : 값이 커질수록 가중치/기울기 0에 가깝게 규제
alpha_list = [0.001, 0.01, 0.1 , 1, 10, 100]
score_list = []
# 반복하여 최적의 규제 강도 찾기
for alpha in alpha_list:
    model = Ridge(alpha=alpha) # 강도 설정하여 릿지 모델 생성
    model.fit(X_train_scaled, Y_train)
    # 학습데이터 점수와 테스트용 점수 격차 적은 alpha 찾기
    print(alpha, "--- 훈련용 학습 데이터 점수 vs 테스트용 학습데이터 점수 ---")
    print("Train R2: ", model.score(X_train_scaled,Y_train))
    print("Test R2: ", model.score(X_test_scaled,Y_test))
    score = model.score(X_train_scaled,Y_train)-model.score(X_test_scaled, Y_test)
    score_list.append(score)

print(score_list.index(max(score_list)), score_list.index(min(score_list)))
# alpha가 10인 경우 가장 점수 격차가 적어 최적의 alpha는 10

# 3) 라쏘 모델
from sklearn.linear_model import Lasso
lasso = Lasso(alpha=10) # 임의의 강도 지점 라쏘 모델 객체 생성
lasso.fit(X_train_scaled, Y_train)
print(lasso.score(X_train_scaled, Y_train))
print(lasso.score(X_test_scaled, Y_test))

# 제거된 특성
import numpy as np
zero_features = np.sum(lasso.coef_ == 0)
print('기울기 0으로 제거된 특성 수: ', zero_features)

# 특성이 적으면 (과소적합/모델 단순) --> 항추가(PolynomialFeatures) /degree 제곱의 차수 
# 특성이 많으면 (과대적합/모델 편향) --> 규제(L1라쏘), L2릿지)