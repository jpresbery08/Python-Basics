#Name Jermaine presbery
#Final Exam
#Date: 4/23/2020
#File Name: Q2.py

def main():
  print("Peter")
  print("Hourly Wage: $15.00")
  print()
  print("Paul")
  print("Hourly Wage: $17.00")
  print()
  print("Simon")
  print("Hourly Wage: $19.00")
  print()
  worker_choice = input("Enter one of the employees name shown above: ")
  worker_hours = eval(input("Enter in the amount of hours they worked: "))

  peter_salary = 15.00
  paul_salary = 17.00
  simon_salary = 19.00

  if(worker_choice == "Peter"):
    peter_result = peter_salary * worker_hours
    peter_pay = round(peter_result, 2)
    print("Peter worked ", worker_hours, "and will be geting paid $", peter_pay )
  elif(worker_choice == "Paul"):
    paul_result = paul_salary * worker_hours
    paul_pay = round(paul_result, 2)
    print("Paul worked ", worker_hours, "and will be geting paid $", paul_pay )
  elif(worker_choice == "Simon"):
    simon_result = simon_salary * worker_hours
    simon_pay = round(simon_result, 2)
    print("Simon worked ", worker_hours, "and will be geting paid $", simon_pay )
  else:
     print("The entered is not an employee.")

main()
    
