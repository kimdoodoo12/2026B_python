

def print_3time():
    print("안녕")
    print("안녕")
    print("안녕")
print_3time()

for i in range(0, 3, 1):
    print("안녕하세요")


def print_n_times(value, n):
    for i in range(n):
        print(value)

print_n_times("WSG", 4)


def print_n_times(n, *values):
    for i in range(n):
        for value in values:
            print(value)
        print()

print_n_times(3, "hi", "what", "a funyy python")


def print_ntimes(value, n=2):
    for i in range(n):
        print(value)
print_ntimes("안녕해요")

print_n_times(3, "hi", end=",")


def sum_all(start,end):
    output = 0
    for i in range(start, end+ 1):
        output += i
    return output

print("0 to 100", sum_all(0, 100))
print("0 to 100", sum_all(0, 1000))
print("50 to 100", sum_all(50, 100))
print("500 to 1000", sum_all(0, 100))


def sum_all(start=0, end=100, step=1):
    output=0
    for i in range(start, end + 1, step):
        output += i
    return output

print("A.", sum_all(0, 100, 10))
print("B.", sum_all(end=100))
print("C.", sum_all(end=100, step=2))