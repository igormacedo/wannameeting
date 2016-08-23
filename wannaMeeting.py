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

    filepath1 = "/home/igormacedo/Documentos/Python/wannameeting/times"
    filepath2 = "/home/igormacedo/Documents/Python/wannaMeeting/times"
    loadFile(filepath2)
    choice = 1

    while choice != 0:
        print "Menu"
        print "1 - Lista de Nomes"
        print "2 - Imprimir Horario"
        print "3 - Comparar Horarios Livres"
        print "4 - Comparar com meu horario"
        print "0 - Exit\n"

        choice = int(raw_input("Escolha um numero: "))
        if (choice == 1):
            print sorted(peopletimes.keys())
            print "\n"
        elif (choice == 2):
            printTimes()
            print "\n"
        elif (choice == 3):
            printReunionResults()
            print "\n"
        elif (choice == 4):
            compararUmaPessoa()
            print "\n"
        elif (choice == 0):
            print "Preparing to exit\n"
        else:
            print "No valid option selected\n"


    #printSomeonesSchedule("Igor Macedo")
    #freetime = reunionTime(["Igor Macedo"])
    #showMeetingResult(freetime)

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

##========================= Print schedule ============================================

def printTimes():
    name = raw_input("Nomes: ")
    printSomeonesSchedule(name)
    print "\n\n"

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

#========================= Reunion Time =============================================

def printReunionResults():
    print "Enter sem nome para sair"
    print "Digite os nomes que precisam estar na reuniao (enter para cada nome): "
    names = []
    while True:
        name = raw_input()
        if name != "":
            names.append(name)
        else:
            break

    if len(names) != 0:
        freetime = reunionTime(names)
        print "\n"
        showMeetingResult(freetime)
    else:
        print "Nenhum nome de input."

def reunionTime(names): # list of names to compare times
    freetime = {}
    for time in times:
        freetime[time] = []

    for name in names:
        if name in peopletimes.keys():
            schedule = peopletimes[name]
            for time in times:
                if schedule[time] == "VAGO":
                    freetime[time].append(name)
        else:
            print "O nome \"" + name +"\" nao esta na lista."

    return freetime

def showMeetingResult(freetime): #dictionary with names with free time at each time
    for time in times:
        print time + ": ",
        print freetime[time]

##===========================  Comparar com meu horario ==========================================

def compararUmaPessoa():
    meunome = ""
    while meunome not in peopletimes.keys():
        meunome = raw_input("Quem eh voce: ")

    myfreelist = getMyfreetimelist(meunome)
    whocanmeet = getDictofWhoCanMeetwithU(myfreelist, meunome)
    showMeetingResult(whocanmeet)

def getMyfreetimelist(nome):
    myfreelist = []
    schedule = peopletimes[nome]
    for time in schedule.keys():
        if schedule[time] == "VAGO":
            myfreelist.append(time)

    return myfreelist

def getDictofWhoCanMeetwithU(myfreelist, meunome):
    whocanmeet = {}
    for time in times:
        whocanmeet[time] = []

    for name in peopletimes.keys():
        if name == meunome:
            continue

        schedule = peopletimes[name]
        for time in myfreelist:
            if schedule[time] == "VAGO":
                whocanmeet[time].append(name)

    return whocanmeet

if __name__ == '__main__':
    sys.exit(main())
