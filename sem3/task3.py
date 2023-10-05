def triangle(n,s):
    for i in range(1,n//2+1):
        print(s*i)
    if n%2!=0:
        print(s*((n//2)+1))
    for i in range(n//2,0,-1):
        print(s*i)
n=int(input())
s=input()
triangle(n,s)