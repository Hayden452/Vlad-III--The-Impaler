# This script searches new emails an inbox for links. If a found link/domain has been previously blacklisted, it is
# ignored. If the link has been previously whitelisted, it is ignored. If the link is not known, it is put in domain
# purgatory until a user can decide what to do with it. Not using REST APIs, because Vlad would need to use selenium to
# find links anyway. Not making automatic attack decisions, as a 100% accuracy rate is both imperative and impossible.
# Will require initial login.
# ================================================== #
# Importing things
import time
from selenium import webdriver
from ExternalMethods import printVladScoutLogo
from selenium.webdriver.common.by import By

# ================================================== #
# Initiating lists and variables, etc.


# Initializing Outlook, allowing user to sign in.
browser = webdriver.Firefox()
browser.get('https://outlook.office.com/mail/')
proceed = input("Once ready, strike the 'return' key to initialize the scout.")
printVladScoutLogo()

while True:
    # Click on newest email every 5 seconds
    mostRecentEmail = browser.find_element(By.CSS_SELECTOR, '.epBmH > div:nth-child(2)')
    mostRecentEmail.click()

    # Scan content for links, or the phrase 'https', 'www', etc
    listOfLinks = browser.find_elements(By.PARTIAL_LINK_TEXT, '')
    print(listOfLinks)

    # If a link is found, check for white/blacklist. If match for neither, put in purgatory
    time.sleep(5)
