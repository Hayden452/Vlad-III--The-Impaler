# ======================================================================== #
# Importing modules, functions, declaring variables, etc.
import time
import random
from ExternalMethods import SelectPoison, findQuery, replaceAllCapitalsInCharacter, printVladLogo
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from colorama import Fore

version = '1.3'
answerListCounter = 0
listOfTextLists = []
listOfAnswers = []
questionList = []
lowerQuestionList = []
randomValues = []
listOfFillableElements = []
isQuery = False
noSites = False
currentSiteIndex = 0
potentialText = object
tempWord = ''
numberOfAttacks = 0
startTime = time.time()
numberOfFailures = 0

# Vlad
printVladLogo()

# Main
while True:
    # Determining sites to attack
    with open("SITES-URLsToAttack.txt", 'r') as file:
        listOfPhishingSpots = file.readlines()

    if len(listOfPhishingSpots) != 0:
        noSites = False

    if not noSites:
        # Variables that need to be different each time the form is visited
        newNameCounter = 1
        listOfDomainsToAttack = []
        unionEmail = str()
        personalEmail = str()
        personalEmailRandomizing = random.randint(0, 1)
        lapTimeStart = time.time()
        # Attacking each site
        for spot in listOfPhishingSpots:
            try:
                # Site prep:
                numberOfAttacks += 1
                browser = webdriver.Firefox()
                browser.get(spot)

                # Finding all input boxes on page
                listOfImportantElements = browser.find_elements(By.CSS_SELECTOR, "input[type='text']")

                # Finding all phishing queries of the user
                for childElement in listOfImportantElements:
                    while not isQuery:
                        parentElement = childElement.find_element(By.XPATH, '..')
                        try:
                            parentElement.find_element(By.CSS_SELECTOR, "#i1 > span:nth-child(1)")
                            isQuery = True
                            potentialText = parentElement.text
                        except NoSuchElementException:
                            childElement = parentElement
                            isQuery = False
                    isQuery = False

                # Formatting, converting to lowercase
                capitalQuestionList = potentialText.split('\n')
                while 'Your answer' in capitalQuestionList:
                    capitalQuestionList.remove('Your answer')
                while '*' in capitalQuestionList:
                    capitalQuestionList.remove('*')

                for word in capitalQuestionList:
                    for char in word:
                        tempWord = tempWord + (replaceAllCapitalsInCharacter(char))
                    questionList.append(str(tempWord))
                    tempWord = ''
                listOfTextLists.append(questionList)
                # ======================================================================== #
                # Random values selection:

                # Selecting poison (fake data). Must pass (randomBaseNumber, newNameCounter, personalEmailRandomizing)
                # returns in following list format: 
                # randomValues[0] = Full name
                # randomValues[1] = First name
                # randomValues[2] = Last name
                # randomValues[3] = Address
                # randomValues[4] = Password
                # randomValues[5] = all-lowercase union email
                # randomValues[6] = all-lowercase personal email
                # randomValues[7] = apartment number
                # randomValues[8] = city
                # randomValues[9] = age
                # randomValues[10] = zip code
                # randomValues[11] = state
                # randomValues[12] = cell phone
                randomBaseNumber = random.randint(0, 55555)
                randomValues.clear()
                randomValues = SelectPoison(randomBaseNumber, newNameCounter, personalEmailRandomizing)
                # ======================================================================== #
                # Preparation for what the phishing site is looking for
                listOfQuestions = listOfTextLists[currentSiteIndex]

                for question in listOfQuestions:
                    # Returns answers for questions in order. 
                    listOfAnswers.append(findQuery(question, randomValues))

                # Sending answers to text fields 
                for element in listOfImportantElements:
                    element.click()
                    element.send_keys(listOfAnswers[answerListCounter])
                    answerListCounter += 1
                answerListCounter = 0

                # Finding the submit element, submitting form.
                submitElement = browser.find_element(By.CSS_SELECTOR, "span[class='NPEfkd RveJvd snByac']")
                submitElement.click()

                # Closing
                browser.close()

                # Timer
                lapTimeEnd = time.time()

                timeSecondsThisRound = (lapTimeEnd - lapTimeStart) % 60
                totalSeconds = (lapTimeEnd - startTime)
                totalSecondsUpTime = round((totalSeconds % 60), 2)

                totalMinutesUpTime = round((totalSeconds / 60), 1)
                totalHoursUpTime = round((totalMinutesUpTime / 60), 1)
                totalDaysUpTime = round((totalHoursUpTime / 24), 1)

                print(Fore.CYAN + "Number of Attacks: ", str(numberOfAttacks), "    Number of failed attacks: ",
                      numberOfFailures, "    Uptime: ", str(totalDaysUpTime), " days, ", str(totalHoursUpTime),
                      " hours, ", str(totalMinutesUpTime), " minutes, ", str(totalSecondsUpTime), " seconds",
                      "    Last Attack Cycle: ", str(timeSecondsThisRound), " seconds", end='\r')
            except Exception as e:
                print('Encountered a fatal error: ', e)
                numberOfFailures += 1
                print(Fore.CYAN + "Number of Attacks: ", numberOfAttacks, " Number of failed attacks: ",
                      numberOfFailures)
        # Exit code
        time.sleep(30)
        currentSiteIndex = + 1
        listOfAnswers = []
        answerListCounter = 0
    else:
        time.sleep(30)
        noSites = False
