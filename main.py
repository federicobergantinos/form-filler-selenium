import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from loguru import logger

from utils import get_proba_by_field, WebDriver
import fields


def main():

    option = webdriver.EdgeOptions()
    option.add_argument("-incognito")

    service = Service(executable_path="./msedgedriver")
    browser = webdriver.Edge(service=service, options=option)

    browser.get("https://forms.gle/nZsA5uDfLJntpsE2A")

    driver = WebDriver(browser)

    # Opciones General
    tipo = get_proba_by_field(field=fields.tipo)

    driver.click_field(field=get_proba_by_field(field=fields.edad))
    driver.click_field(field=get_proba_by_field(field=fields.genero))
    driver.click_field(field=tipo)
    driver.click_field(
        field=get_proba_by_field(field=fields.orientacion_vocacional),
    )
    driver.click_field(
        field=get_proba_by_field(field=fields.trabajaste_profesion),
    )

    # Siguiente
    driver.click_field(
        field='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div',
    )

    # Opciones Estudiante
    if tipo == '//*[@id="i37"]':
        logger.info("Estudiante")
        driver.click_field(
            field=get_proba_by_field(
                field=fields.estudiante_abandonar_carrera
            ),
        )
        driver.click_field(
            field=get_proba_by_field(field=fields.estudiante_futuro_laboral),
        )
        driver.click_field(
            field=get_proba_by_field(field=fields.estudiante_satisfecho),
        )
        # Siguiente
        driver.click_field(
            field='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]',
        )
    elif tipo == '//*[@id="i40"]':
        logger.info("Estudiante-Abandono")
    elif tipo == '//*[@id="i43"]':
        logger.info("Egresado")
    elif tipo == '//*[@id="i46"]':
        logger.info("Abandono")
    elif tipo == '//*[@id="i49"]':
        logger.info("No es IT")
    else:
        logger.info("Error")
        raise "error"

    time.sleep(10)
    # Use the following snippets to get elements by their class names
    # textboxes = browser.find_elements_by_class_name("quantumWizTextinputPaperinputInput")
    # checkboxes = browser.find_elements_by_class_name("quantumWizTogglePapercheckboxInnerBox")
    # submitbutton = browser.find_element_by_class_name("appsMaterialWizButtonPaperbuttonContent")

    # # Use the following snippets to get elements by their XPath
    # otherboxes = browser.find_element_by_xpath("<Paste the XPath here>")

    # textboxes[0].send_keys("Hello World")

    # radiobuttons[2].click()

    # checkboxes[1].click()
    # checkboxes[3].click()

    # submitbutton[0].click()

    browser.close()


main()
