# Stair Pattern
'''
*
* *
* * *
* * * *
* * * * * 
'''

N=int(input("Enter the size N: "))
for i in range(1, N+1):
  for j in range(i):
    print("*", end =' ')
  print()