#Name Jermaine Presbery
#File Name a7p2.py
#Assignment #7

def main():
  num = eval(input("Enter in a series of numbers to recieve sum(INESERT COMMAS BETWEEN NUMBERS): "))
  num_sum = 0
  for i in num:
    num_sum = num_sum + i
    avg = num_sum / len(num)
  print(avg)

main()
