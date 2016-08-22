#Wanna'Meeting.py
import sys
import string

times = ["2M12","2M34","2M56","2T12","2T34","2T56","2N12","2N34",
        "3M12","3M34","3M56","3T12","3T34","3T56","3N12","3N34",
        "4M12","4M34","4M56","4T12","4T34","4T56","4N12","4N34",
        "5M12","5M34","5M56","5T12","5T34","5T56","5N12","5N34",
        "6M12","6M34","6M56","6T12","6T34","6T56","6N12","6N34",
        "7M12","7M34","7M56","7T12","7T34","7T56","7N12","7N34",
        "1M12","1M34","1M56","1T12","1T34","1T56","1N12","1N34"]
weekday = ["SEGUNDA","TERCA","QUARTA","QUINTA","SEXTA","SABADO","DOMINGO"]

peopletimes = {}

def main():

    #filepath = raw_input("Nome do arquivo: ")

    filepath = "/home/igormacedo/Documents/Python/wannaMeeting/times"
    loadFile(filepath)
    printSomeonesSchedule("Igor Macedo")
    freetime = reunionTime(["Igor Macedo"])
    showMeetingResult(freetime)

##Loads the file with the schedule for everyone and creates a dictionary the contains
##eveyone's schedule
def loadFile(filepath):
    f = open(filepath, 'r')
    for line in f:
        newentry = line.split("-")
        peopletimes[newentry[0]] = {}
        schedule = newentry[1].split(";")
        for i in range(0,len(times)):
            peopletimes[newentry[0]][times[i]] = schedule[i]

    #print peopletimes

def printSomeonesSchedule(name): #gets string with name to print the schedule dictionary
    schedule = peopletimes[name]
    for day in range(0,7):
        print weekday[day] + "\t",
        print "| " + schedule[times[8*day]] + " |",
        print "| " + schedule[times[8*day+1]] + " |",
        print "| " + schedule[times[8*day+2]] + " |",
        print "| " + schedule[times[8*day+3]] + " |",
        print "| " + schedule[times[8*day+4]] + " |",
        print "| " + schedule[times[8*day+5]] + " |",
        print "| " + schedule[times[8*day+6]] + " |",
        print "| " + schedule[times[8*day+7]] + " |"

def reunionTime(names): # list of names to compare times
    freetime = {}
    for time in times:
        freetime[time] = []

    for name in names:
        schedule = peopletimes[name]
        for time in times:
            if schedule[time] == "VAGO":
                freetime[time].append(name)

    #print freetime
    return freetime

def showMeetingResult(freetime): #dictionary with names with free time at each time
    for time in times:
        print time + ": ",
        print freetime[time]



if __name__ == '__main__':
    sys.exit(main())
