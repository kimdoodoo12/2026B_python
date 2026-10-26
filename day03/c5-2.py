
def factorial(n):
    output = 1
    for i in range(1, n+1):
        output *= i
    return output

factorial(2)
factorial(3)


def factorial2(n):
    if n == 0:
        return 1
    else:
        return n *factorial2(n-1)


for 단 in range(2, 10, 1):
    for 곱 in range(1, 10, 1):
        print(단 * 곱)


def 구구단 (단=2, 곱=1):
    if 단 > 9:
        return
    if 곱 > 9:
        구구단(단+1, 1)
        return
    print(단 * 곱)
    구구단(단, 곱 + 1)

구구단()


counter = 0
def fibonacci(n):
    global counter
    counter += 1
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n-2)

print(fibonacci(50))
print(counter)