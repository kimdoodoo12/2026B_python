# 범주형(문자) 특성 갖는 학습 방법
# 1) 실습에 필요한 펭귄 계측 데이터
import seaborn as sns
df = sns.load_dataset('penguins')

# 2) 전처리 : 결측 제외
df = df.dropna().reset_index(drop=True)
df.info()

# 3) 다중분류 실습 위한 특성/타깃
X = df.drop(columns=['species'])
Y = df['species']

# 4) 분리
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# 5) 복합형 파이프라인 위한 수치형과 범주형 특성 분리
num_features = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']
cat_features = ['island', 'sex', ]

# 6) 복합 특성 
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
# pp = ColumnTransformer(transformers=[('식별자', 전처리기, 컬럼목록)])
# OneHotEnncoder: 범주형 자료들을 0과1로 표현
#   drop='first' : 첫번째 범주에 대한 카테고리는 제외
# 0 1 0
# 0 0 1
# 0 0 0 # 모두 0으로 채워진 행이면 첫번째 범주로 의미 가짐
# sparse_output=False : 변환된 자료들을 numpy배열로 반환
pp = ColumnTransformer(transformers=[
    ('num', StandardScaler(), num_features), # 수치형 특성
    ('cat', OneHotEncoder(drop='first', sparse_output=False), cat_features)
])

# 파이프라인 만들기
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
# Pipeline([('식별자', '변환기/모델')])
pipe = Pipeline([('pp', pp), ('model', LogisticRegression())])
# 학습하기
pipe.fit(X_train, Y_train)
Y_pred = pipe.predict(X_test)
print(Y_pred[:3]) # ['Gentoo' 'Chinstrap' 'Adelie']
print(pipe.classes_)
# 리포트(모델 평가지표)
from sklearn.metrics import classification_report, f1_score
print(f1_score(Y_test, Y_pred))

