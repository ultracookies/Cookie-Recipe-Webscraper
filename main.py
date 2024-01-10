from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

import recipe
import json

driver = webdriver.Safari()

desert = "key lime pie"

print('about to get')
url = "https://www.allrecipes.com/search/results/?search=" + desert
driver.get(url)
print('has been got')

def _test_(card):
    card.click()
    ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)
    your_element = WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions) \
        .until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "heading-content")))
    recipe_name = driver.find_element(By.CLASS_NAME, "heading-content").text
    your_element = WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions) \
        .until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "ingredients-item")))
    ingredients = driver.find_elements(By.CLASS_NAME, "ingredients-item")
    your_element = WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions) \
        .until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "instructions-section-item")))
    steps = driver.find_elements(By.CLASS_NAME, "instructions-section-item")
    new_ingredients = []
    for i in range(len(ingredients)):
        new_ingredients.append(ingredients[i].text)
    new_steps = []
    for i in range(len(steps)):
        new_steps.append(steps[i].text)
    cookies = recipe.Recipe(recipe_name, new_ingredients, new_steps)
    y = json.dumps(cookies.__dict__)
    print(y)


try:
    # b = driver.find_element(By.ID, "search-block")
    # b.send_keys("gloreo cookies")
    # b.send_keys(Keys.ENTER)

    ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)
    your_element = WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions) \
        .until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "card__recipe")))
    print('finding cards')
    cards = driver.find_elements(By.CLASS_NAME, "card__recipe")
    print('found cards')

    for i in range(len(cards)):
        driver.get("https://www.allrecipes.com/search/results/?search=" + desert)
        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)
        your_element = WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions) \
            .until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "card__recipe")))

        cards = driver.find_elements(By.CLASS_NAME, "card__recipe")
        _test_(cards[i])

    # # rating = driver.find_elements(By., ".recipe-ratings .rating-star")
    # #
    # # print(len(rating))
    #
    # your_element = WebDriverWait(driver, 10, 2) \
    #     .until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "heading-content")))
    #
    # recipe_name = driver.find_element(By.CLASS_NAME, "heading-content").text
    #
    # your_element = WebDriverWait(driver, 10, 2) \
    #     .until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "ingredients-item")))
    #
    # ingredients = driver.find_elements(By.CLASS_NAME, "ingredients-item")
    #
    # your_element = WebDriverWait(driver, 10, 2) \
    #     .until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "instructions-section-item")))
    #
    # steps = driver.find_elements(By.CLASS_NAME, "instructions-section-item")
    #
    # new_ingredients = []
    # for i in range(len(ingredients)):
    #     new_ingredients.append(ingredients[i].text)
    #
    # # new_ingredients = ""
    # # new_ingredients.join([ingredients[i].text + "\n" for i in range(len(ingredients))])
    #
    # new_steps = []
    # for i in range(len(steps)):
    #     new_steps.append(steps[i].text)
    #
    # cookies = recipe.Recipe(recipe_name, new_ingredients, new_steps)
    # y = json.dumps(cookies.__dict__)
    #
    # # with open("recipes.json", "w") as file:
    # #     file.write(y)
    # #     file.flush()
    # #     file.close()
    #
    # # y = json.dumps(cookies, indent=4, cls=recipe.RecipeEncoder)
    #
    # print(y)


    # print("INGREDIENTS for " + recipe_name)
    # for i in range(len(ingredients)):
    #     print(ingredients[i].text)
    #
    # print("\n---------\n")
    #
    # print("INSTRUCTIONS")
    # for i in range(len(steps)):
    #     print(steps[i].text)
finally:
    driver.quit()
