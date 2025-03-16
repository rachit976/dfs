#TAKE IINPUT
print("half peramid pattern of stars(*):")
n = int(input("please enter the of rows :"))
#outer loop to handle number of rows
for i in range (n):
    for j in range(i+1):
       print("*",end="")
    print()