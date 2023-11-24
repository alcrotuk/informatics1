s=input()
s = s[1:]
x, y, z = s[:2], s[2:4], s[4:]
def f(x):
    x10 = int(x, 16)
    a10 = 255 - x10
    a16 = hex(a10)[2:]
    return a16
print("#"+f(x)+f(y)+f(z))


