#Name Jermaine presbery
#Final Exam
#Date: 4/23/2020
#File Name: Q3.py

def main():
  print("4x^3 - 3")
  print()
  x = eval(input("Enter in a value for x for the problem shown above to receive an answer "))
  print()
  if(x == 0):
    print("Invalid Input")
  else:
    result = 4*(x)**3 - 3
    print(x, "is the number entered and the sum is ", result)
main()
