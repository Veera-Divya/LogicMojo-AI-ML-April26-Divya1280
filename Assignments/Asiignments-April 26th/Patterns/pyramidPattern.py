# Pyramid Pattern
'''
    *
   ***
  *****
 *******
*********
'''
N=int(input("Enter the No of lines N: "))
for i in range(0, N):
  print(((N-i)*2)*" " ,end=" ")
  for j in range(2*i+1):
    print("*", end=" ")
  print()