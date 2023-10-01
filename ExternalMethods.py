import linecache
import random
from colorama import Fore, Style
version = '1.3'

def findQuery(question, values):
    randomValues = values
    answer = str()
    isAnswered = False
    if "name" in question:
        if "first name" in question:
            answer = randomValues[1]
            isAnswered = True
        elif "last name"  in question:

            answer = randomValues[2]
            isAnswered = True
        else:
            answer = randomValues[0]
            isAnswered = True
    elif "address" in question or "email" in question:
        if "email address" in question:
            if "student email" in question:
                answer = randomValues[5]
                isAnswered = True
            elif "not school email" in question:
                answer = randomValues[6]
                isAnswered = True
            elif "school email" in question:
                answer = randomValues[5]
                isAnswered = True
            elif "personal email" in question:
                answer = randomValues[6]
                isAnswered = True
            else:
                answer = randomValues[6]
                isAnswered = True
        elif "residential address" or "apt#" or "apartment number" in question:
            answer = randomValues[7]
            isAnswered = True
    elif "password" in question or "credential" in question:
        answer = randomValues[4]
        isAnswered = True
    elif "city" in question:
        answer = randomValues[8]
        isAnswered = True
    elif "age" in question:
        answer = randomValues[9]
        isAnswered = True
    elif "zip code" in question:
        answer = randomValues[10]
        isAnswered = True
    elif "cell number" in question:
        answer = randomValues[12]
        isAnswered = True
    elif "state" in question:
        answer = randomValues[11]
        isAnswered = True
    elif isAnswered == False:
        print("ERROR: Unknown Query")
        answer = 'Unknown Query'
    isAnswered = False
    
    return answer

listOfReturnValues = []
listOfResidential = ['Ayers', 'Hope', "Watters", 'Hurt', 'Grace', 'Craig',
                    'DeHoney', 'Dodd', 'Grey', 'Jarman', 'Lee', 'Paschall',
                    'Pollard', 'Rogers', 'Sullivan', 'Wright']

def SelectPoison(randomBaseNumber, newNameCounter, personalEmailRandomizing):
# Choosing fake details
    fullNameAndUnionEmail = linecache.getline("DATA/PERSONAL_DATA-NamesAndEmails-All.txt", (randomBaseNumber * newNameCounter) % 61466)
    
    firstName = ' '.join(fullNameAndUnionEmail.split()[:1])

    lastName = ' '.join(fullNameAndUnionEmail.split()[1:2])

    fullName = firstName + ' ' + lastName

    address = linecache.getline("DATA/PERSONAL_DATA-FakeAddresses.txt", (randomBaseNumber * newNameCounter) % 9456)
    
    cityOnlyAddress = address.split(',')
    cityOnly = cityOnlyAddress[0]

    password = linecache.getline("DATA/PERSONAL_DATA-RandomPasswords-All.txt", (randomBaseNumber * newNameCounter) % 116665)

    capUnionEmail = ' '.join(fullNameAndUnionEmail.split()[2:])

    match personalEmailRandomizing:
        case 0: 
            capPersonalEmail = str(firstName + '.' + lastName + str(random.randint(0,50)) + str(random.randint(0,50)) + '@gmail.com')
        case 1:
            capPersonalEmail = str(firstName + str(linecache.getline("RandomPassword-Words.txt", (randomBaseNumber * newNameCounter) % 55555)) + '@gmail.com')
    
    aptNumber = str(listOfResidential[randomBaseNumber % 16]) + ' ' + str(random.randint(100, 550))

    decider = random.randint(0,1)
    listOfCities = ['Jackson', cityOnly]
    city = listOfCities[decider]

    zipCode = str(3 + random.randint(1000, 9999))

    age = random.randint(17, 22)

    listOfStates = [
    'Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado',' Connecticut', 'Delaware', 
    'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 
    'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 
    'Montana ', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 
    'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island ', 'South Carolina', 'South Dakota',
    'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'Tennessee', 
    'Tennessee', 'Tennessee', 'Tennessee', 'Tennessee', 'Tennessee', 'Tennessee', 'Tennessee', 'Tennessee', 'Tennessee', 
    'Tennessee', 'Tennessee', 'Tennessee', 'Tennessee', 'Tennessee', 'Tennessee', 'Tennessee', 'Tennessee', 'Tennessee', 
    'Tennessee', 'Tennessee', 'Tennessee', 'Tennessee', 'Tennessee', 'Tennessee', 'Tennessee', 'Tennessee', 'Tennessee', 
    'Tennessee', 'Tennessee', 'Tennessee', 'Tennessee', 'Tennessee', 'Tennessee', 'Tennessee', 'Tennessee', 'Tennessee']

    state = listOfStates[random.randint(0,77)]

    cellDecider = random.randint(0,997)

    personalCellPhone = str(731 + random.randint(0,9) + random.randint(0,9) + random.randint(0,9) + random.randint(0,9) + random.randint(0,9) + random.randint(0,9) + random.randint(0,9))
    trapCellPhonesList = [str(7313942922), (2026225000), (8008291040), (8008294059), (3128291199), (2023243000), (8002256324), (5184657551), (5058891300), (9072764441), (7702163000), (4102658080)]
    if cellDecider % 2:
          cellPhone = personalCellPhone
          if cellDecider < 500:
               cellPhone = str(731 + random.randint(0,9) + random.randint(0,9) + random.randint(0,9) + random.randint(0,9) + random.randint(0,9) + random.randint(0,9) + random.randint(0,9))
          else:
               cellPhone = '731' + '-' + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + '-' + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
    else:
        cellPhone = trapCellPhonesList[cellDecider % len(trapCellPhonesList)]


    listOfReturnValues.append(fullName)
    listOfReturnValues.append(firstName)
    listOfReturnValues.append(lastName)
    listOfReturnValues.append(address)
    listOfReturnValues.append(password)
    listOfReturnValues.append(capUnionEmail)
    listOfReturnValues.append(capPersonalEmail)
    listOfReturnValues.append(aptNumber)
    listOfReturnValues.append(city)
    listOfReturnValues.append(age)
    listOfReturnValues.append(zipCode)
    listOfReturnValues.append(state)
    listOfReturnValues.append(cellPhone)

    return listOfReturnValues

def replaceAllCapitalsInCharacter(someChar):
    outputChar = someChar
    match someChar:
         case 'A':
              outputChar = 'a'
         case 'B':
              outputChar = 'b'
         case 'C':
              outputChar = 'c'
         case 'D':
              outputChar = 'd'
         case 'E':
              outputChar = 'e'
         case 'F':
              outputChar = 'f'
         case 'G':
              outputChar = 'g'
         case 'H':
              outputChar = 'h'
         case 'I':
              outputChar = 'i'
         case 'J':
              outputChar = 'j'
         case 'K':
              outputChar = 'k'
         case 'L':
              outputChar = 'l'
         case 'M':
              outputChar = 'm'
         case 'N':
              outputChar = 'n'
         case 'O':
              outputChar = 'o'
         case 'P':
              outputChar = 'p'
         case 'Q':
              outputChar = 'q'
         case 'R':
              outputChar = 'r'
         case 'S':
              outputChar = 's'
         case 'T':
              outputChar = 't'
         case 'U':
              outputChar = 'u'
         case 'V':
              outputChar = 'v'
         case 'W':
              outputChar = 'w'
         case 'X':
              outputChar = 'x'
         case 'Y':
              outputChar = 'y'
         case 'Z':
              outputChar = 'z'
    return outputChar

def printVladLogo():
     print("__     __  _          _      ____       _____   _   _   _____")
     print("\ \   / / | |        / \    |  _ \     |_   _| | | | | | ____| ")
     print(" \ \ / /  | |       / _ \   | | | |      | |   | |_| | |  _|   ")
     print("  \ V /   | |___   / ___ \  | |_| |      | |   |  _  | | |___")  
     print("   \_/    |_____| /_/   \_\ |____/       |_|   |_| |_| |_____| ")
     print(Fore.GREEN + ">:)           " + Fore.GREEN + 'version ' + version + Style.RESET_ALL)
     print("    ___   __  __   ____       _      _       _____   ____  ")
     print("   |_ _| |  \/  | |  _ \     / \    | |     | ____| |  _ \ ")
     print("    | |  | |\/| | | |_) |   / _ \   | |     |  _|   | |_) |")
     print("    | |  | |  | | |  __/   / ___ \  | |___  | |___  |  _ < ")
     print("   |___| |_|  |_| |_|     /_/   \_\ |_____| |_____| |_| \_\ ")
     print("\n\n")
     print(Style.RESET_ALL)

def printVladScoutLogo():
     print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
     print('__     __  _          _      ____    _   ____  ')
     print('\ \   / / | |        / \    |  _ \  ( ) / ___|')
     print(' \ \ / /  | |       / _ \   | | | | |/  \___ \\')
     print('  \ V /   | |___   / ___ \  | |_| |      ___) |')
     print('   \_/    |_____| /_/   \_\ |____/      |____/')
     print('\n')
     print('      ____     ____    ___    _   _   _____')
     print('     / ___|   / ___|  / _ \  | | | | |_   _|')
     print('     \___ \  | |     | | | | | | | |   | |  ')
     print('      ___) | | |___  | |_| | | |_| |   | |  ')
     print('     |____/   \____|  \___/   \___/    |_| ')
     print('\n\n')
     print(Style.RESET_ALL)