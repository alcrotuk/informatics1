def Fib(n) -> int:
    if n == 2:
        return 1
    if n == 1:
        return 1
    return Fib(n - 1) + Fib(n - 2)


def simpleMult(a):
    while a != 0:
        for i in range(a ** 0.5):
            if a % i == 0:
                arr.append()


def simple(a, flag):
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            flag = False
    return (flag)


def simMult(a, arr, sim):
    while a > 1:
        if a % sim == 0 and simple(sim, True):
            a /= sim
            arr.append(sim)
        else:
            sim += 1
    return (arr)


arr = list()
a = int(input())
flag = True
sim = 2
print(Fib(a))
print(*simMult(a, arr, sim))
