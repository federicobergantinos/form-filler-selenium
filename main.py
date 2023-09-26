import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from loguru import logger

from utils import get_proba_by_field, WebDriver
import encuesta_fields


def main():

    option = webdriver.EdgeOptions()
    option.add_argument("-incognito")

    service = Service(executable_path="./msedgedriver")
    browser = webdriver.Edge(service=service, options=option)

    browser.get("https://forms.gle/nZsA5uDfLJntpsE2A")

    driver = WebDriver(browser)

    # Opciones General
    tipo = get_proba_by_field(field=encuesta_fields.tipo)

    driver.click_field(field=get_proba_by_field(field=encuesta_fields.edad))
    driver.click_field(field=get_proba_by_field(field=encuesta_fields.genero))
    driver.click_field(field=tipo)
    driver.click_field(
        field=get_proba_by_field(field=encuesta_fields.orientacion_vocacional),
    )
    driver.click_field(
        field=get_proba_by_field(field=encuesta_fields.trabajaste_profesion),
    )

    # Siguiente
    driver.change_page(
        field='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div',
    )

    # Opciones Estudiante
    if tipo == '//*[@id="i37"]':
        logger.info("Estudiante")
        driver.click_field(
            field=get_proba_by_field(
                field=encuesta_fields.estudiante_futuro_laboral
            ),
        )
        driver.click_field(
            field=get_proba_by_field(
                field=encuesta_fields.estudiante_satisfecho
            ),
        )
        penso_en_abandonar = get_proba_by_field(
            field=encuesta_fields.estudiante_abandonar_carrera
        )
        driver.click_field(
            field=penso_en_abandonar,
        )

        # Siguiente
        driver.change_page(
            field='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]',
        )
        if penso_en_abandonar == '//*[@id="i24"]':
            logger.info("Estudiante SI penso Abandono")
            driver.click_field(
                field=get_proba_by_field(field=encuesta_fields.penso_conexion),
            )
            driver.click_field(
                field=get_proba_by_field(
                    field=encuesta_fields.penso_expectativas
                ),
            )
            driver.click_field(
                field=get_proba_by_field(field=encuesta_fields.penso_factores),
            )
            driver.click_field(
                field=get_proba_by_field(field=encuesta_fields.penso_recursos),
            )
            driver.click_field(
                field=get_proba_by_field(
                    field=encuesta_fields.penso_recursos_dispo
                ),
            )

            # Enviar
            driver.send_form()

        else:
            logger.info("Estudiante NO penso Abandono")

            # Enviar
            driver.send_form()

    elif tipo == '//*[@id="i46"]' or tipo == '//*[@id="i40"]':
        if tipo == '//*[@id="i40"]':
            logger.info("Estudiante-Abandono")
        else:
            logger.info("Abandono")

        driver.click_field(
            field=get_proba_by_field(field=encuesta_fields.abandono_conexion),
        )
        driver.click_field(
            field=get_proba_by_field(
                field=encuesta_fields.abandono_expectativas
            ),
        )
        driver.click_field(
            field=get_proba_by_field(field=encuesta_fields.abandono_factores),
        )
        driver.click_field(
            field=get_proba_by_field(field=encuesta_fields.abandono_materias),
        )
        driver.click_field(
            field=get_proba_by_field(
                field=encuesta_fields.abandono_recibiste_orien
            ),
        )
        driver.click_field(
            field=get_proba_by_field(field=encuesta_fields.abandono_recursos),
        )
        driver.click_field(
            field=get_proba_by_field(
                field=encuesta_fields.abandono_recursos_dispo
            ),
        )
        driver.click_field(
            field=get_proba_by_field(field=encuesta_fields.abandono_retomar),
        )

        # Enviar
        driver.send_form()
    elif tipo == '//*[@id="i43"]':
        logger.info("Egresado")

        driver.click_field(
            field=get_proba_by_field(field=encuesta_fields.egresado_calidad),
        )
        driver.click_field(
            field=get_proba_by_field(
                field=encuesta_fields.egresado_conomientos
            ),
        )
        driver.click_field(
            field=get_proba_by_field(field=encuesta_fields.egresado_estudiar),
        )

        # Enviar
        driver.send_form()

    elif tipo == '//*[@id="i49"]':
        logger.info("No es IT")

        # Enviar
        driver.send_form()
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
