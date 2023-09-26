# ¿Qué edad tenés?
edad = {
    "18-20": {"id": '//*[@id="i5"]', "probability": 0.1},
    "21-25": {"id": '//*[@id="i8"]', "probability": 0.3},
    "26-30": {"id": '//*[@id="i11"]', "probability": 0.4},
    "+31": {"id": '//*[@id="i14"]', "probability": 0.2},
}

# ¿Cuál es es tu género?
genero = {
    "Femenino": {"id": '//*[@id="i21"]', "probability": 0.15},
    "Masculino": {"id": '//*[@id="i24"]', "probability": 0.7},
    "No binario": {"id": '//*[@id="i27"]', "probability": 0.05},
    "Prefiero no decirlo": {"id": '//*[@id="i30"]', "probability": 0.1},
}

# #  Sos o fuiste en algún momento estudiante de una carrera universitaria relacionada con Tecnologías de la Información (IT)?
# tipo = {
#     "Sí, soy estudiante en la actualidad": {
#         "id": '//*[@id="i37"]',
#         "probability": 0.18,
#     },
#     "Si, soy estudiante pero abandoné una carrera IT en la antigüedad.": {
#         "id": '//*[@id="i40"]',
#         "probability": 0.28,
#     },
#     "Sí, soy egresado de una carrera relacionada con IT.": {
#         "id": '//*[@id="i43"]',
#         "probability": 0.12,
#     },
#     "Sí, fuí estudiante pero abandoné la carrera.": {
#         "id": '//*[@id="i46"]',
#         "probability": 0.35,
#     },
#     "No, nunca estudié una carrera relacionada con IT.": {
#         "id": '//*[@id="i49"]',
#         "probability": 0.07,
#     },
# }

# TODO
tipo = {
    "Sí, soy estudiante en la actualidad": {
        "id": '//*[@id="i37"]',
        "probability": 1,
    },
    "Si, soy estudiante pero abandoné una carrera IT en la antigüedad.": {
        "id": '//*[@id="i40"]',
        "probability": 0.0,
    },
    "Sí, soy egresado de una carrera relacionada con IT.": {
        "id": '//*[@id="i43"]',
        "probability": 0.0,
    },
    "Sí, fuí estudiante pero abandoné la carrera.": {
        "id": '//*[@id="i46"]',
        "probability": 0.0,
    },
    "No, nunca estudié una carrera relacionada con IT.": {
        "id": '//*[@id="i49"]',
        "probability": 0.0,
    },
}


#  ¿Recibiste algún tipo de orientación vocacional antes de elegir tu carrera?
orientacion_vocacional = {
    "Si": {"id": '//*[@id="i56"]', "probability": 0.68},
    "No": {"id": '//*[@id="i59"]', "probability": 0.32},
}


#  ¿Trabajás o trabajaste en alguna profesión cuya existencia desconocías antes de elegir tu carrera?
trabajaste_profesion = {
    "Si": {"id": '//*[@id="i66"]', "probability": 0.82},
    "No": {"id": '//*[@id="i69"]', "probability": 0.18},
}


# ¿Que grado de satisfacción sentís con el nivel de apoyo que recibís de tus profesores y la facultad en tu carrera de IT?
estudiante_satisfecho = {
    "Muy satisfecho": {"id": '//*[@id="i5"]', "probability": 0.23},
    "Satisfecho": {"id": '//*[@id="i8"]', "probability": 0.34},
    "Neutral": {"id": '//*[@id="i11"]', "probability": 0.28},
    "Poco": {"id": '//*[@id="i14"]', "probability": 0.10},
    "Nada": {"id": '//*[@id="i17"]', "probability": 0.05},
}

#  ¿Considerás que las oportunidades laborales futuras en el campo de IT son un factor motivador para continuar con tus estudios actuales?
estudiante_futuro_laboral = {
    "si": {"id": '//*[@id="i24"]', "probability": 0.73},
    "no": {"id": '//*[@id="i27"]', "probability": 0.18},
    "no sabe": {"id": '//*[@id="i30"]', "probability": 0.09},
}

#   ¿Alguna vez pensaste en abandonar la carrera?
estudiante_abandonar_carrera = {
    "si": {"id": '//*[@id="i37"]', "probability": 0.48},
    "no": {"id": '//*[@id="i40"]', "probability": 0.52},
}


#   ¿Qué factores influyen principalmente en tu pensamiento de abandonar la carrera?
penso_factores = {
    "Falta de apoyo de profesores": {
        "id": '//*[@id="i6"]',
        "probability": 0.07,
    },
    "Dificultad de los cursos": {"id": '//*[@id="i9"]', "probability": 0.07},
    "Condiciones laborales": {"id": '//*[@id="i12"]', "probability": 0.46},
    "Duración de la carrera": {"id": '//*[@id="i15"]', "probability": 0.05},
    "Falta de interés en el tema": {
        "id": '//*[@id="i18"]',
        "probability": 0.23,
    },
    "Otro": {"id": '//*[@id="i21"]', "probability": 0.12},
}

#   ¿Qué tipo de recursos tenes disponible durante tus estudios de IT?
penso_recursos_dispo = {
    "Tutorías": {"id": '//*[@id="i29"]', "probability": 0.06},
    "Grupos de estudio": {"id": '//*[@id="i32"]', "probability": 0.16},
    "No tuve ningún recurso": {"id": '//*[@id="i35"]', "probability": 0.24},
    "Otros": {"id": '//*[@id="i38"]', "probability": 0.54},
}

#  ¿Utilizaste alguno de esos recursos durante tus estudios
penso_recursos = {
    "Sí": {"id": '//*[@id="i45"]', "probability": 0.64},
    "no": {"id": '//*[@id="i48"]', "probability": 0.36},
}

#   ¿Sentiste que tenes una conexión clara entre los conocimientos adquiridos en la carrera de IT y su aplicabilidad en el mundo real?
penso_conexion = {
    "Mayoritariamente sí": {"id": '//*[@id="i55"]', "probability": 0.47},
    "Mayoritariamente no": {"id": '//*[@id="i58"]', "probability": 0.53},
}

#  ¿Experimentas algún tipo de conflicto entre tus expectativas sobre la carrera de IT y la realidad de los estudios?
penso_expectativas = {
    "si": {"id": '//*[@id="i65"]', "probability": 0.77},
    "no": {"id": '//*[@id="i68"]', "probability": 0.23},
}

#  ¿Qué porcentaje de materias aprobadas tenías antes de abandonar la carrera de IT?
abandono_materias = {
    "Menos de 20%": {"id": '//*[@id="i5"]', "probability": 0.23},
    "Entre 20% y 40%": {"id": '//*[@id="i8"]', "probability": 0.18},
    "Entre 40% y 60%": {"id": '//*[@id="i11"]', "probability": 0.37},
    "Entre 60% y 80%": {"id": '//*[@id="i14"]', "probability": 0.14},
    "Más de 80%": {"id": '//*[@id="i17"]', "probability": 0.08},
}

#   ¿Qué factores influyeron principalmente en tu decisión de abandonar la carrera?
abandono_factores = {
    "Falta de apoyo de profesores": {
        "id": '//*[@id="i25"]',
        "probability": 0.03,
    },
    "Dificultad de los cursos": {"id": '//*[@id="i28"]', "probability": 0.05},
    "Condiciones laborales": {"id": '//*[@id="i31"]', "probability": 0.54},
    "Duración de la carrera": {"id": '//*[@id="i34"]', "probability": 0.08},
    "Falta de interés en el tema": {
        "id": '//*[@id="i37"]',
        "probability": 0.21,
    },
    "Otro": {"id": '//*[@id="i40"]', "probability": 0.09},
}

#   8) ¿Qué tipo de recursos tuviste disponible durante tus estudios de IT?
abandono_recursos_dispo = {
    "Tutorías": {"id": '//*[@id="i48"]', "probability": 0.07},
    "Grupos de estudio": {"id": '//*[@id="i51"]', "probability": 0.14},
    "No tuve ningún recurso": {"id": '//*[@id="i54"]', "probability": 0.27},
    "Otros": {"id": '//*[@id="i57"]', "probability": 0.52},
}

#   ¿Utilizaste alguno de esos recursos durante tus estudios?
abandono_recursos = {
    "Sí": {"id": '//*[@id="i64"]', "probability": 0.36},
    "no": {"id": '//*[@id="i67"]', "probability": 0.64},
}

#   ¿Sentiste que tenías una conexión clara entre los conocimientos adquiridos en la carrera de IT y su aplicabilidad en el mundo real?
abandono_conexion = {
    "Mayoritariamente sí": {"id": '//*[@id="i74"]', "probability": 0.41},
    "Mayoritariamente no": {"id": '//*[@id="i77"]', "probability": 0.59},
}

#  ¿Experimentaste algún tipo de conflicto entre tus expectativas sobre la carrera de IT y la realidad de los estudios?
abandono_expectativas = {
    "si": {"id": '//*[@id="i84"]', "probability": 0.83},
    "no": {"id": '//*[@id="i87"]', "probability": 0.17},
}

# ¿Recibiste orientación vocacional para explorar diferentes especialidades dentro de IT antes de tomar la decisión de abandonar?
abandono_recibiste_orien = {
    "si": {"id": '//*[@id="i94"]', "probability": 0.89},
    "no": {"id": '//*[@id="i97"]', "probability": 0.11},
}

#  ¿Pensás retomar tus estudios de IT en algún momento futuro?
abandono_retomar = {
    "si": {"id": '//*[@id="i104"]', "probability": 0.25},
    "no": {"id": '//*[@id="i107"]', "probability": 0.32},
    "tal vez": {"id": '//*[@id="i110"]', "probability": 0.43},
}


#  pregunta
campo = {
    "asd": {"id": '//*[@id="i"]', "probability": 0.0},
    "asd": {"id": '//*[@id="i"]', "probability": 0.0},
    "asd": {"id": '//*[@id="i"]', "probability": 0.0},
    "asd": {"id": '//*[@id="i"]', "probability": 0.0},
}
