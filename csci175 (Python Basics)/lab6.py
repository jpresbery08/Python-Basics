#Chinese New Year


def main():
    # Gets user birthday and converts
    userBirth = input("Enter in your birthdate (mm/dd/yyyy): ")

    # split into components
    monthStr, dayStr, yearStr = userBirth.split("/")

    print()

    #Converts mm to month name
    if(monthStr == "01"):
        monthStr = "January"
    elif(monthStr == "02"):
        monthStr = "February"
    elif(monthStr == "03"):
        monthStr = "March"
    elif(monthStr == "04"):
        monthStr = "April"
    elif(monthStr == "05"):
        monthStr = "May"
    elif(monthStr == "06"):
        monthStr = "June"
    elif(monthStr == "07"):
        monthStr = "July"
    elif(monthStr == "08"):
        monthStr = "August"
    elif(monthStr == "09"):
        monthStr = "September"
    elif(monthStr == "10"):
        monthStr = "October"
    elif(monthStr == "11"):
        monthStr = "November"
    elif(monthStr == "12"):
        monthStr = "December"



    #Years in range from 1994 -2020
    if(yearStr == "1994"):
        #outputs users birthday as well as the animal
        print("Your birthday is ", monthStr, dayStr+ ",", yearStr, "the year of the dog" )
    elif(yearStr == "1995"):
        #outputs users birthday as well as the animal
        print("Your birthday is ", monthStr, dayStr+ ",", yearStr, "the year of the pig" )
    elif(yearStr == "1996"):
        #outputs users birthday as well as the animal
        print("Your birthday is ", monthStr, dayStr+ ",", yearStr, "the year of the rat" )
    elif(yearStr == "1997"):
        #outputs users birthday as well as the animal
        print("Your birthday is ", monthStr, dayStr+ ",", yearStr, "the year of the ox" )
    elif(yearStr == "1998"):
        #outputs users birthday as well as the animal
        print("Your birthday is ", monthStr, dayStr+ ",", yearStr, "the year of the tiger" )
    elif(yearStr == "1999"):
        #outputs users birthday as well as the animal
        print("Your birthday is ", monthStr, dayStr+ ",", yearStr, "the year of the rabbit" )
    elif(yearStr == "2000"):
        #outputs users birthday as well as the animal
        print("Your birthday is ", monthStr, dayStr+ ",", yearStr, "the year of the dragon" )

    elif(yearStr == "2001"):
        #outputs users birthday as well as the animal
        print("Your birthday is ", monthStr, dayStr+ ",", yearStr, "the year of the snake" )

    elif(yearStr == "2002"):
        #outputs users birthday as well as the animal
        print("Your birthday is ", monthStr, dayStr+ ",", yearStr, "the year of the horse" )
    elif(yearStr == "2003"):
        #outputs users birthday as well as the animal
        print("Your birthday is ", monthStr, dayStr+ ",", yearStr, "the year of the sheep" )

    elif(yearStr == "2004"):
        #outputs users birthday as well as the animal
        print("Your birthday is ", monthStr, dayStr+ ",", yearStr, "the year of the monkey" )

    elif(yearStr == "2005"):
        #outputs users birthday as well as the animal
        print("Your birthday is ", monthStr, dayStr+ ",", yearStr, "the year of the chicken" )

    elif(yearStr == "2006"):
        #outputs users birthday as well as the animal
        print("Your birthday is ", monthStr,  dayStr+ ",", yearStr, "the year of the dog" )

    elif(yearStr == "2007"):
        #outputs users birthday as well as the animal
        print("Your birthday is ", monthStr, dayStr+ ",", yearStr, "the year of the pig" )

    elif(yearStr == "2008"):
        #outputs users birthday as well as the animal
        print("Your birthday is ", monthStr, dayStr+ ",", yearStr, "the year of the rat" )

    elif(yearStr == "2009"):
        #outputs users birthday as well as the animal
        print("Your birthday is ", monthStr, dayStr+ ",", yearStr, "the year of the ox" )

    elif(yearStr == "2010"):
        #outputs users birthday as well as the animal
        print("Your birthday is ", monthStr, dayStr+ ",", yearStr, "the year of the tiger" )

    elif(yearStr == "2011"):
        #outputs users birthday as well as the animal
        print("Your birthday is ", monthStr, dayStr+ ",", yearStr, "the year of the rabbit" )

    elif(yearStr == "2012"):
        #outputs users birthday as well as the animal
        print("Your birthday is ", monthStr, dayStr+ ",", yearStr, "the year of the dragon" )

    elif(yearStr == "2013"):
        #outputs users birthday as well as the animal
        print("Your birthday is ", monthStr, dayStr+ ",", yearStr, "the year of the snake" )

    elif(yearStr == "2014"):
        #outputs users birthday as well as the animal
        print("Your birthday is ", monthStr, dayStr+ ",", yearStr, "the year of the horse" )

    elif(yearStr == "2015"):
        #outputs users birthday as well as the animal
        print("Your birthday is ", monthStr, dayStr+ ",", yearStr, "the year of the sheep" )

    elif(yearStr == "2016"):
        #outputs users birthday as well as the animal
        print("Your birthday is ", monthStr, dayStr+ ",", yearStr, "the year of the monkey" )

    elif(yearStr == "2017"):
        #outputs users birthday as well as the animal
        print("Your birthday is ", monthStr, dayStr+ ",", yearStr, "the year of the chicken" )

    elif(yearStr == "2018"):
        #outputs users birthday as well as the animal
        print("Your birthday is ", monthStr, dayStr+ ",", yearStr, "the year of the dog" )

    elif(yearStr == "2019"):
        #outputs users birthday as well as the animal
        print("Your birthday is ", monthStr, dayStr+ ",", yearStr, "the year of the pig" )

    elif(yearStr == "2020"):
        #outputs users birthday as well as the animal
        print("Your birthday is ", monthStr, "", dayStr+ ",", yearStr, "the year of the rat" )


main()
