import time

from selenium.webdriver.common.keys import Keys

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

import recipe
import json

driver = webdriver.Safari()

desert = "cookies"

driver.get("https://tasty.co/search?q= " + desert + "&sort=popular")

try:
    recipes = driver.find_elements(By.CLASS_NAME, "feed-item")
    recipes[0].click()

    ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)
    your_element = WebDriverWait(driver, 10, 2) \
        .until(expected_conditions.presence_of_all_elements_located((By.CLASS_NAME, "ingredient")))

    ingredients = driver.find_elements(By.CLASS_NAME, "ingredient")

    your_element = WebDriverWait(driver, 10, 2) \
        .until(expected_conditions.presence_of_all_elements_located((By.CLASS_NAME, "xs-mb2")))

    # steps = driver.find_elements(By.CLASS_NAME, "xs-mb2")
    steps = driver.find_element(By.XPATH, "//ol[li/@class='xs-mb2']")

    # print(len(steps))
    # for i in range(len(steps)):
    #     print(steps[i].text)
    # print(steps[0].text)
    print(steps.text)

    # ingredients = driver.find_elements(By.CLASS_NAME, "ingredients__section")
    # print(len(ingredients))

finally:
    driver.quit()