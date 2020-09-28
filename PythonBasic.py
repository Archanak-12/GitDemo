# a=1
# while a<=5:
#     b = 1
#     while b<=5:
#         print(a,"*",b, "=", a*b)
#         b = b+1
#     a = a+1
# for i in range(1, 6):
#    for j in range(1, 6):
#        if i == j and j == i:
#            print("*",end="")
#            i = i + 1
#            j = j + 1
#        else:
#            print(" ",end="")
#    print()
# x = 0
# y = 4
# for i in range(5):
#    for j in range(5):
#        if i == x and j == y:
#            print("*",end="")
#            x = x + 1
#            y = y - 1
#        elif i == j:
#            print("*",end="")
#        else:
#            print(end=" ")
#    print()
# for i in range(1, 6):
#     for j in range(1, 6):
#         #if (i+j)%2 == 0:
#         #if i+j>=6:
#         if i+j >= 6:
#         #if i + j <= 6:
#         #if i >= j:
#         #if j <= i:
#         #if j <= i:
#         #if i <= j:
#         #if i != j:
#             print("* ",end="")
#         else:
#             print(" ",end="")
#     print()
for i in range(1, 6):
    for j in range(1, 6):
        #if i+j <= 6:
        if j<=i:
            print(j ,end="")
        else:
            print(" ",end="")
    print()