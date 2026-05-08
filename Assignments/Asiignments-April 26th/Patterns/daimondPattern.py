# Diamond Pattern
'''
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
'''

N = int(input("Enter the No of lines You want in above pyramid: "))
for i in range(0, N + 1):
    print(((N - i) * 2) * " ", end=" ")
    for j in range(2 * i + 1):
        print("*", end=" ")
    print()
for i in range(1, N + 1):
    print((i * 2) * " ", end=" ")
    for j in range(2 * (N - i) + 1):
        print("*", end=" ")
    print()



