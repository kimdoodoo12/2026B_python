# pandas : 데이터 조작 및 분석(표 형태) 라이브러리

import pandas as pd


# 1] 데이터프레임: 2차원(표)

data_list = [ [ 'ant' , 25 , 'seoul'] , ['bee' , 30 , 'busan'] , ['cat' , 35 , 'incheon'] ] # 2차원 리스트 

x = pd.DataFrame(data_list, columns=['name', 'age', 'city'])
print(x)

# 2] 데이터프레임2 , pd.DataFrame(딕셔너리) , 키(열이름)
data_dict = { 
  'name' : ['ant','bee','cat'] , 
  'age' : [25,30,35] , 
  'city' : ['seoul','busan','incheon'] } # 딕셔너리 

df = pd.DataFrame(data_dict)
print(df)

# 3] 컬럼 값 추출, df['열이름']
ages = df['age']
print(ages) # Series(1차원)
print(type(ages)) # <class 'pandas.Series'>
print(type(ages.values)) # <class 'numpy.ndarray'>

# 4] 데이터프레임3 : numpy
import numpy as np
data_np = np.array(data_list) # numpy 자료
df = pd.DataFrame(data_np)
df = pd.DataFrame(
    data_np,
    columns=['name', 'age', 'city'],
    index=['A', 'B', 'C']
)
print(df)
print(df.shape) # 행/열 크기 (3, 3)
print(df.columns) # 컬럼 목록  Index(['name', 'age', 'city'], dtype='str')
print(df.index) # 인덱스 목록  Index(['A', 'B', 'C'], dtype='str')
print(df.values)
print(df.head(5)) # 상위 n개 반환
print(df.tail(2)) # 하위 n개 반환
print(df.info) # 컬럼 이름 , 결축치, 타입 확인

# 6] 인덱싱 = df.iloc(인덱스) / 슬라이싱
print(df.iloc[1]) # 2행
print(df.iloc[1, 2]) # 2행 3열 busan
print(df.loc['B']) # 1행 = B행
print(df.loc['B', 'city']) # B행 city 열

# 7] 슬라이싱 , [시작인덱스:끝인덱스]
print(df.iloc[0:2, 0:1])
print(df.loc['A' :'C', 'name' : 'age'])

# 8] 열 추가, df[새로운열] = 새로운 값
df['score'] = [100, 80, 95]
print(df)

# 9] 값 수정, df[수정할열] = 새로운 값
df['age'] = [31, 52, 40]
print(df)

df.loc['B', 'age'] = 70
print(df)
df.iloc[0,0] = 'apple'
print(df)

# 10] 여러개 수정
df.loc[['A','B'], 'score'] = [50, 60]
print(df)

# 11] 필터링(조건) 
cont1 = df['score'] > 70
cont2 = df['age'] >= 40
print(df[ cont1 | cont2])

# 필터링 이용하여 새로운 열**
df['passed'] = False
df.loc[df['score'] > 70, 'passed'] = True
print(df)

# 12] 컬럼명 변경, df.rename('기존열 이름' : '새로운 컬럼명')
df = df.rename(columns={'city' : '도시', 'age' : '나이'})
df.info

# 13] 집계 , df.describe(), df['열이름'.통계함수()]
print(df.describe())
print(df['나이'].sum())
print(df['passed'].value_counts()) # 자료 빈도 수

# 14] 합치기/병합

df1 = pd.DataFrame({'ID': [1, 2, 3], 'Score': [90, 80, 85]})
df2 = pd.DataFrame({'ID': [4, 5, 6], 'Score': [75, 95, 88]})

# 세로 연결 axios
new_df = pd.concat([df1, df2], axis=0, ignore_index=True)
print(new_df)
new_df = pd.concat([df1, df2], axis=1)
print(new_df)

# 병합 : 교집합(공통 컬럼)
df_info = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Ant', 'Bee', 'Cat']})
df_score = pd.DataFrame({'ID': [2, 3, 4], 'Score': [88, 92, 85]})
# pd.merge(df1, df2, on = '공통컬럼명', how=방향)
df_merged = pd.merge(df_info, df_score, on="ID", how='inner')
print(df_merged)
df_merged = pd.merge(df_info, df_score, on="ID", how='outer')
print(df_merged)