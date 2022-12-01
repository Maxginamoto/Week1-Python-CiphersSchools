n=int(input("n: "))
for i in range(n):
    for j in range(n):
        print(i+1,end="")
    print()
print()
for i in range(n):
    for j in range(n):
        print(j+1,end="")
    print()
print()
for i in range(n):
    for j in range(n):
        print(n-i,end="")
    print()
print()
for i in range(n):
    for j in range(n):
        print(n-j,end="")
    print()
print()
for i in range(n):
    for j in range(n):
        print(max(j+1,i+1,n-j,n-i),end="")
    print()
print()
for i in range(n):
    for j in range(n):
        print(max(i,j,n-i-1,n-j-1)+1,end="")
    print()
print()
#Loved scratching my head over this<3
