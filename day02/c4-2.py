
# 딕셔너리란? {} 중괄호 선언하고 키:값 형태로 쉼표로 연결
# {key:value, key:value, key:value}
# key 중복 X, vlaue 중복 O
# JS:JSON, JAVA:MAP/DTO, DB: RECORD

dict_a = {'name' : '어벤저스 엔드게임', 'type': '히어로 무비'}
print(dict_a['name'])
print(dict_a['type'])
# print(dict_a.name) 안됨

dict_a['price'] = 5000
print(dict_a)

dict_a['type'] = '호러 무비' # 이미 존재하는 키는 수정
print(dict_a)

del dict_a['price']

print('price' in dict_a) # False
print('name' in dict_a)

print(dict_a.get('name'))
print(dict_a.get('price'))
print("반복문")
for key in dict_a:
    print(dict_a.get(key))
    print(dict_a[key])


pets = [
    {"name": "구름", "age":5},
    {"name": "초코", "age":4}
]

for pet in pets:
    print(pet['name'] , pet['age'] , "살")

character = {
    "name": "기사",
    "level": 12,
    "items": {
        "sword": "불꽃의 검",
        "armor": "풀플레이트"
    },
    "skill": ["베기", "세게 베기", "아주 세게 베기"]
}


for key in character:
    print(key)
    print(type(character.get(key)))
    if type(character.get(key)) in (str, int):
        print(key, ":", character.get(key))
    elif type(character.get(key)) is list:
        for item in character.get(key):
            print(key, ":", item)
    elif type(character.get(key)) is dict:
        for item in character.get(key):
            print(key, ":", character.get(key).get(item))