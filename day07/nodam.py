import numpy as np

data = np.genfromtxt('C:\\Users\\GRAM\\Downloads\\2026B_python\\day07\\nodam.csv', delimiter=',')
print(f"데이터형태: {data.shape}")

six_month = data[::, -1]
# print(six_month)

nomarlized_six_month = (six_month - np.min(six_month)) / (np.max(six_month) - np.min(six_month))
print(nomarlized_six_month)
print(data[nomarlized_six_month <= 0.1])
print(data[::, -1])