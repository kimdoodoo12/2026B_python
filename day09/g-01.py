
# Matplotlib: 파이썬에서 시각적으로 표현하는 라이브러리
import matplotlib.pyplot as plt
import matplotlib

# Matplotlib 그래프는 한글 폰트 지원 안함
# ### 한글 폰트 설정 ###
plt.rc('font' , family = 'Malgun Gothic') # 윈도우 맑은 고딕 설정
plt.rcParams['axes.unicode_minus']=False # 음수기호 깨짐 방지
#######################

# 1] 선 차트
epochs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
train_loss = [0.9, 0.7, 0.55, 0.45, 0.38, 0.32, 0.28, 0.25, 0.23, 0.20]
val_loss = [0.95, 0.75, 0.60, 0.52, 0.48, 0.45, 0.44, 0.43, 0.44, 0.45]
# 1) plt.figure(figsize=(가로inch, 세로inch))
plt.figure(figsize=(7, 4))
# 2) 선차트 : plt.plot(x축값, y축값, label = "계열명", color="색상명", linestyle="선종류", marker="점 모양")
plt.plot(epochs, train_loss, label="Train Loss", color="blue", linestyle="-", marker="o")
plt.plot(epochs, val_loss, label="Value Loss", color="red", linestyle="--", marker="s")
# 3) 차트의 제목
plt.title("each model loss statics") # 차트의 제목
plt.xlabel("amount of learning") # x축 제목
plt.ylabel("loss")  # y축 제목
plt.grid() # 구분 선
plt.legend() # 범례 표시

plt.show()
# 2] 막대 차트(비교) plt.bar , 선 차트(추세) ,
classes = ['Cat', 'Dog', 'Bird', 'Fish']
counts = [120, 150, 80, 45]

# 1) plt.bar(x값, y값, color=[색상] , width=막대크기)
bars = plt.bar(classes, counts, color=["#422929", '#444444', '#FFFF00', '#FFA500'], width=0.8)
# 2) 막대 값 레이블 plt.bar_label(막대차트변수, padding=막대와레이블간격 , fontsize=폰트크기)
plt.bar_label(bars, padding=3, fontsize=8)
plt.title('each class sample count')
plt.xlabel('class')
plt.ylabel('sample count')
plt.grid(True, alpha=0.5)

plt.show()
# 3] 산점도(상관관계)
x = [1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5]
y = [2.3, 3.8, 5.1, 7.0, 7.8, 9.2, 10.5]

# 1) 산점도 , plt.scatter(x축값, y축값, color="색상", s=점크기, alpha=투명도)
plt.scatter(x, y, color="purple", s=80, alpha=0.8)
plt.title('studying time and test score of correlation')
plt.xlabel('studying time')
plt.ylabel('test score')

plt.show()
# 4] 히스토그램 (연속형 수치/값 분포)
import numpy as np
# 평균 170을 중심으로 표준편차 5만큼 퍼져있는 종모양
heights = np.random.normal(loc=170, scale=5, size=1000)

# 1) 히스토그램, plt.hist(값, bins="구간개수", color="색상", edgecolor=색상, alpha=투명도)
plt.hist(heights, bins=30, edgecolor='black')
plt.xlabel("heights(cm)")
plt.ylabel("Frequency/Distribution")
plt.show()

# 5] 박스 플롯 (분포 범위내 이상치)
heights = np.random.normal(loc=170, scale=5, size=1000)
data_with_outliers = np.append(heights, [210, 215, 120])
# 1) plt.boxplot(값, ) 데이터들을 사분위수(25%, 50%, 75%) 표현
plt.boxplot(data_with_outliers)
plt.show()

# 6] 한 차트에 2개 이상 그래프 표현
# fig, axs = plt.subplots(행개수, 열개수, figsize=(가로, 세로))
fig, axs = plt.subplots(1, 2, figsize=(10, 4)) # 1줄(행) 차트 2개
# 1행1열 차트 , axs[인덱스].차트종류()
axs[0].plot([1,2,3], [4,5,6])
axs[0].set_title('sub 1: Line Graph')
axs[0].set_xlabel('axis x')
# 1행2열 차트
axs[1].bar(['A', 'B', 'C'], [30,15,40])

# 차트 실행
plt.show()
