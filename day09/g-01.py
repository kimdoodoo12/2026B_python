
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

# 차트 실행
plt.show()
