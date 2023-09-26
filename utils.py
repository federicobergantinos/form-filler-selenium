import random
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def get_proba(field):
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


def random_choice_from_list(str_list):
    """
    This function returns a random string from a given list of strings.
    """
    return random.choice(str_list)


class WebDriver:
    def __init__(self, browser):
        self.browser = browser

    def click_field(self, field):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, field))).click()

    def text_field(self, field, text):
        wait = WebDriverWait(self.browser, 10)
        wait.until(
            EC.presence_of_element_located((By.XPATH, field))
        ).send_keys(text)

    def change_page(self, field):
        time.sleep(2)
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, field))).click()
        wait = WebDriverWait(self.browser, 10)

    def send_form(self):
        self.change_page(
            field='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]',
        )
