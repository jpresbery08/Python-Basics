

def secConvert():
    time1 = input("Enter the time for the first runner (mm:ss): ")
    time2 = input("Enter the time for the second runner (mm:ss): ")


    min, sec = time1.split(":")

    min1, sec1 = time2.split(":")

    int(min)
    int(sec)
    int(min1)
    int(sec1)

    time1 = min + sec
    time2 = min1 + sec



    if(time1 < time2):
        print("Runner 1 is the winner.")
        print("Train more like Time next time runner 2.")
    elif(time1 > time2):
        print("Runner 2 is the winner.")
        print("Train more like Time next time runner 1.")
    else:
        print("Welp I guess its a draw")



def main():

    secConvert()



main()
