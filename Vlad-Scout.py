# This script searches new emails an inbox for links. If a found link/domain has been previously blacklisted, it is
# ignored. If the link has been previously whitelisted, it is ignored. If the link is not known, it is put in domain
# purgatory until a user can decide what to do with it. Not using REST APIs, because Vlad would need to use selenium to
# find links anyway. Not making automatic attack decisions, as a 100% accuracy rate is both imperative and impossible.
# 
# - IMPORTANT - The automated system will not work if 2FA (a very good security practice) is enabled
# This application has two prerequisites in order to run:
# 1) A text file must be created that has an account's email login username on the first line and password on the second
# line. This is to prevent hard-coding credentials
# 2) The Outlook account in question must be configured to automatically open the most recent email upon sign-in, in
# order to retrieve the most recent message.
# ================================================== #
# Importing things
import time
from selenium import webdriver
from ExternalMethods import printVladScoutLogo
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from urllib.parse import urlparse

# ================================================== #
# Initiating lists and variables, etc. Retrieving password
with open("/Users/mrmustard/Desktop/Mild Danger/My Documents/VladScout.txt", 'r') as file:
    credentials = file.readlines()

accountUsername = credentials[0]
accountPassword = credentials[1]
printVladScoutLogo()

while True:
    try:
        # Reading white and blacklists from text file for automatic decision-making
        with open("SITES-whitelistedDomains.txt", 'r') as file:
            whitelistedDomains = file.readlines()

        with open("SITES-blacklistedDomains.txt", 'r') as file:
            blacklistedDomains = file.readlines()

        # Initializing Outlook, allowing user to sign in.
        browser = webdriver.Firefox()
        browser.get('https://outlook.office.com/mail/')

        # Username
        usernameField = WebDriverWait(browser, 5).until(ec.presence_of_element_located((By.CSS_SELECTOR, '#i0116')))
        usernameField.send_keys(accountUsername + Keys.RETURN)
        time.sleep(5)

        # Password
        passwordField = WebDriverWait(browser, 5).until(ec.presence_of_element_located((By.CSS_SELECTOR, '#i0118')))
        passwordField.send_keys(accountPassword)
        passwordField.send_keys(Keys.RETURN)
        time.sleep(5)

        # Submitting
        submitButton = browser.find_element(By.CSS_SELECTOR, "#idSIButton9")
        submitButton.send_keys(Keys.RETURN)
        time.sleep(5)

        # Scan content for links, or the phrase 'https', 'www', etc.
        # not[0]
        rawListOfLinks = browser.find_elements(By.PARTIAL_LINK_TEXT, '')

        # Removing boilerplate links
        rawListOfLinks.remove(rawListOfLinks[0])
        rawListOfLinks.remove(rawListOfLinks[0])

        # Has this link/domain been seen before?
        for link in rawListOfLinks:
            # Comparing the link's domain to other domains in "database" text file.
            linkDomain = urlparse(link.get_attribute('href'))
            
            # If yes and it is a known good domain, ignore it.
            if linkDomain in whitelistedDomains:
                print('Link\'s domain has been whitelisted: ', linkDomain)

            # If yes and it is blacklisted, add this link to the list of sites to attack
            elif linkDomain in blacklistedDomains:
                print('Link\'s domain is blacklisted: ', linkDomain)
                with open("SITES-URLsToAttack.txt", 'r') as file:
                    currentlyAttacking = file.readlines()
                if link not in currentlyAttacking:
                    with open("SITES-URLsToAttack.txt", 'a') as file:
                        file.write(link.get_attribute('href'))
                else:
                    print('Link is already being attacked: ' + str(link.get_attribute('href')))

            # If no, put in purgatory for manual human decision.
            else:
                print('Unknown domain: ', linkDomain)
                with open("SITES-domainPurgatory.txt", 'r') as file:
                    currentPurgatories = file.readlines()
                if linkDomain not in currentPurgatories:
                    with open("SITES-domainPurgatory.txt", 'a') as file:
                        file.write(str(linkDomain))
                else:
                    print('Domain already in purgatory')

        # If a link is found, check for white/blacklist. If match for neither, put in purgatory
        time.sleep(30)
    except TimeoutError:
        print('Encountered a Timeout error. Might mean internet is spotty. Reattempting deployment.')
        time.sleep(5)
