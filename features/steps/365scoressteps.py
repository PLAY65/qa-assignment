import time
import logging
import csv

from behave import *
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


@given('launch Chrome browser')
def launchBrowser(context):
    # context.driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
    context.driver = webdriver.Chrome()


@when('open google')
def openGoogle(context):
    context.driver.get("https://www.google.com/")


@then('search 365scores and count results')
def searchScoresAndCountResults(context):
    searchScores(context)
    countResults(context)


def searchScores(context):
    elem = context.driver.find_element(By.NAME, "q")
    # enter search text
    elem.send_keys("365scores in israel")
    #elem.send_keys("Livescore in israel")
    time.sleep(0.2)
    # perform Google search with Keys.ENTER
    elem.send_keys(Keys.ENTER)


def countResults(context):
    list_of_elements = context.driver.find_elements(By.XPATH,
                                                    "//h3/parent::a[contains(@href,'365scores') and contains(@ping,'')]")
    logging.info(f"'Number of links  {len(list_of_elements)}")

    with open('urls365scores.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for elem in list_of_elements:
            print(elem.get_attribute("href"))
            writer.writerow(elem.get_attribute("href"))


@when('navigate by pages and check titles')
def navigateByPagesCheckTitles(context):
    with open('urls365scores.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader)
        data = [list(row) for row in reader]

    for elem in data:
        url = ''.join([str(elem) for i, elem in enumerate(elem)])
        context.driver.get(url)
        get_title = context.driver.title
        logging.info(f"'get_title  {get_title}")
        assert get_title != ""


@then('close browser')
def closeBrowser(context):
    context.driver.close()
