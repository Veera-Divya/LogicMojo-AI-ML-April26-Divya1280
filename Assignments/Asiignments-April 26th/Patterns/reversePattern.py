# Reverse Stair Pattern
'''
Enter the size N: 5
* * * * *
* * * *
* * * 
* *
*
'''
N=int(input("Enter the size N: "))
for i in range(0, N):
  for j in range(N-i):
    print("*", end=' ')
  print()