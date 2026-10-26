string_a = "age:{}".format(10)
print(string_a)
string_b = "{}{}{}".format(1, "hi", True)
print(string_b)

i = input("입력 = ")
x = []
for w in i.split():
    x.append(w[::-1])
y = ' '.join(x)
z = ''.join(c for c in y if c not in "ong")
print(z)