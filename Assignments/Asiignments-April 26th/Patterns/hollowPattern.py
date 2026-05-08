# Hollow Square Pattern:
'''
*****
*   *
*   *
*   *
*****
'''
side_length = int(input("Enter the side length of pattern side_length: "))
for row in range(1, side_length+1):
  for col in range(1, side_length+1):
    if row == 1 or row==side_length or col ==1 or col == side_length:
      print("*", end ="")
    else:
      print(" ", end = "")
  print()