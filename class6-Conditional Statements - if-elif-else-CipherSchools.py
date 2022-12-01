a=True
if a==True:
    print("a is true")
else:
    print("a is false")
print("end")
a=False
if a==True:
    print("a is true")
else:
    print("a is false")
print("end")
isFriend=int(input("isFriend: True(1) or False(0):"))
isBlocked=int(input("isBlocked: True(1) or False(0):"))
isAdmin=int(input("isAdmin: True(1) or False(0):"))
isMarkZuckerberg=int(input("isMarkZuckerberg: True(1) or False(0):"))
if isMarkZuckerberg==True or (isFriend==True or isAdmin==True) and isBlocked==False:
    print("has access")
else:
    print("access denied")
