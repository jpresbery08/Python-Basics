def temp():
  temp = eval(input("Enter in a temparture for water to find out whtther it is a solid, liquid, or gas: "))
  if(temp <= 32):
    print("The temperature you entered will turn the wter into a solid.")
  elif(temp >= 33 and temp <= 211 ):
    print("The temperature you entered will turn the wter into a liquid.")
  elif(temp >= 212):
    print("The temperature you entered will turn the wter into a gas.")

temp()
