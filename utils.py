import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def get_proba_by_field(field):
    # Create a weighted list based on the probabilities for each age option
    weighted_options = []
    for option, details in field.items():
        count = int(details["probability"] * 100)
        weighted_options.extend([option] * count)

    # Choose a random option from the weighted list
    selected_option = random.choice(weighted_options)

    # Retrieve the XPath of the selected option
    selected_xpath = field[selected_option]["id"]
    return selected_xpath


class WebDriver:
    def __init__(self, browser):
        self.browser = browser

    def click_field(self, field):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, field))).click()
