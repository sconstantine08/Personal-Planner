eventName = []
eventMonth = []
eventDay = []
eventYear = []


def addEvent():
    name=input("What is the event: ")
    eventName.append(name)
    
    year=int(input("What is the year: "))
    eventYear.append(year)
    
    month=int(input("What is the month (number): "))
    month= validateMonth(month)
    
    day=int(input("What is the date: "))
    day= validateDay(month,day,year)
    eventDay.append(day)
    
    if month==1:
        eventMonth.append("January")
    elif month==2:
        eventMonth.append("February")
    elif month==3:
        eventMonth.append("March")
    elif month==4:
        eventMonth.append("April")
    elif month==5:
        eventMonth.append("May")
    elif month==6:
        eventMonth.append("June")
    elif month==7:
        eventMonth.append("July")
    elif month==8:
        eventMonth.append("August")
    elif month==9:
        eventMonth.append("September")
    elif month==10:
        eventMonth.append("October")
    elif month==11:
        eventMonth.append("November")
    elif month==12:
        eventMonth.append("December")
        
# Check for and adjust month input if necessary
def validateMonth(monthC):
    while monthC<1 or monthC>12:
        monthC= int(input("Invalid month. Please enter a value from 1-12: "))
    return monthC
    


# Check if a given year is a leap year
def leap_year(yearC):
    if (yearC % 4==0 and yearC % 100 != 0) or yearC % 400==0:
        yearC=1
    else:
        yearC= 0
    return yearC
    

# Check for and adjust day input if necessary
def validateDay(monthE, dayE, yearE):
    valid=0
    
    if monthE==4 or monthE==6 or monthE==9 or monthE==11:
        if dayE>=1 and dayE<=30:
            valid=1
    elif monthE==2:
        if leap_year(yearE)==1:
            if dayE>=1 and dayE<=29:
                valid=1
        else:
            if dayE>=1 and dayE<=28:
                valid=1
    else:
        if dayE>=1 and dayE<=31:
            valid=1
          
          
    while not valid:
        
        if monthE==4 or monthE==6 or monthE==9 or monthE==11:
            dayE=int(input("Invalid day. Please enter a value from 1-30: "))
            if dayE>=1 and dayE<=30:
                valid=1
        elif monthE==2:
            if leap_year(yearE)==1:
                dayE=int(input("Invalid day. Please enter a value from 1-29: "))
                if dayE>=1 and dayE<=29:
                    valid=1
            else:
                dayE=int(input("Invalid day. Please enter a value from 1-28: "))
                if dayE>=1 and dayE<=28:
                    valid=1
        else:
            dayE=int(input("Invalid day. Please enter a value from 1-31: "))
            if dayE>=1 and dayE<=31:
                valid=1
                
    return dayE
    
# Date: Month Day, Year
def printEvents():
    
    print ("******************** List of Events ********************")
     
    for i in range(len(eventName)):
        print(eventName[i])
        print("Date: "+str(eventMonth[i])+" "+ str(eventDay[i])+", "+ str(eventYear[i]))


    
    
#*********** MAIN **********

addEvent()
    # Prompt the user to see if they want to enter more events
second=input("Do you want to enter another event? NO to stop: ")
while second != "NO":
    addEvent()
    second=input("Do you want to enter another event? NO to stop: ")
    
printEvents()