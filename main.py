from selenium import webdriver
from selenium.webdriver.edge.service import Service
from loguru import logger

from utils import get_proba, WebDriver, random_choice_from_list
import encuesta_fields as fields


def main():

    option = webdriver.EdgeOptions()
    option.add_argument("-incognito")

    service = Service(executable_path="./msedgedriver")
    browser = webdriver.Edge(service=service, options=option)

    browser.get("https://forms.gle/nZsA5uDfLJntpsE2A")

    driver = WebDriver(browser)

    # Opciones General
    tipo = get_proba(field=fields.tipo)

    driver.click_field(field=get_proba(field=fields.edad))
    driver.click_field(field=get_proba(field=fields.genero))
    driver.click_field(field=tipo)
    driver.click_field(field=get_proba(field=fields.orientacion_vocacional))
    driver.click_field(field=get_proba(field=fields.trabajaste_profesion))

    # Siguiente
    driver.change_page(
        field='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div',
    )

    # Opciones Estudiante
    if tipo == '//*[@id="i37"]':
        logger.info("Estudiante")
        driver.click_field(field=get_proba(field=fields.estudiante_futuro_laboral))
        driver.click_field(field=get_proba(field=fields.estudiante_satisfecho))

        penso_en_abandonar = get_proba(field=fields.estudiante_abandonar_carrera)
        driver.click_field(field=penso_en_abandonar)

        # Siguiente
        driver.change_page(
            field='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]',
        )
        if penso_en_abandonar == '//*[@id="i24"]':
            logger.info("Estudiante SI penso Abandono")
            driver.click_field(field=get_proba(field=fields.penso_conexion))
            driver.click_field(field=get_proba(field=fields.penso_expectativas))
            driver.click_field(field=get_proba(field=fields.penso_factores))
            driver.click_field(field=get_proba(field=fields.penso_recursos))

            recursos_dispo = get_proba(field=fields.penso_recursos_dispo)
            driver.click_field(field=recursos_dispo)

            # si es otros, se pone vacio
            if recursos_dispo == '//*[@id="i38"]':
                driver.text_field(
                    field='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div[4]/div/div/div/div/div[1]/input',
                    text=" ",
                )

            factores = get_proba(field=fields.penso_factores)
            driver.click_field(field=factores)

            # si es otros, random entre otros motivos factores
            if factores == '//*[@id="i21"]':
                driver.text_field(
                    field='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div[6]/div/div/div/div/div[1]/input',
                    text=random_choice_from_list(fields.factores_otros_motivos),
                )

            # Enviar
            driver.send_form()

        else:
            logger.info("Estudiante NO penso Abandono")

            # Enviar
            driver.send_form()

    # Estudiantes que abandonaron y empezaron otra carrera y estudaintes que abandonaron
    elif tipo == '//*[@id="i46"]' or tipo == '//*[@id="i40"]':
        if tipo == '//*[@id="i40"]':
            logger.info("Estudiante-Abandono")
        else:
            logger.info("Abandono")

        driver.click_field(field=get_proba(field=fields.abandono_conexion))
        driver.click_field(field=get_proba(field=fields.abandono_expectativas))
        driver.click_field(field=get_proba(field=fields.abandono_materias))
        driver.click_field(field=get_proba(field=fields.abandono_recibiste_orien))
        driver.click_field(field=get_proba(field=fields.abandono_recursos))
        driver.click_field(field=get_proba(field=fields.abandono_retomar))

        factores = get_proba(field=fields.abandono_factores)
        driver.click_field(field=factores)

        # si es otros, se pone vacio
        if factores == '//*[@id="i40"]':
            driver.text_field(
                field='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div[6]/div/div/div/div/div[1]/input',
                text=random_choice_from_list(fields.factores_otros_motivos),
            )
 
        recursos_dispo = get_proba(field=fields.abandono_recursos_dispo)
        driver.click_field(field=recursos_dispo)

        # si es otros, se pone vacio
        if recursos_dispo == '//*[@id="i57"]':
            driver.text_field(
                field='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/div[4]/div/div/div/div/div[1]/input',
                text=" ",
            )
            
            
        # Enviar
        driver.send_form()
    elif tipo == '//*[@id="i43"]':
        logger.info("Egresado")

        driver.click_field(field=get_proba(field=fields.egresado_calidad))
        driver.click_field(field=get_proba(field=fields.egresado_conomientos))
        driver.click_field(field=get_proba(field=fields.egresado_estudiar))

        # Enviar
        driver.send_form()

    elif tipo == '//*[@id="i49"]':
        logger.info("No es IT")

        # Enviar
        driver.send_form()
    else:
        logger.info("Error")
        raise "error"


    browser.close()


main()
