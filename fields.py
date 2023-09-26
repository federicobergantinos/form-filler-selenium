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


# TODO proba
# ¿Que grado de satisfacción sentís con el nivel de apoyo que recibís de tus profesores y la facultad en tu carrera de IT?
estudiante_satisfecho = {
    "Muy satisfecho": {"id": '//*[@id="i5"]', "probability": 0.0},
    "Satisfecho": {"id": '//*[@id="i8"]', "probability": 0.0},
    "Neutral": {"id": '//*[@id="i11"]', "probability": 0.0},
    "Poco": {"id": '//*[@id="i14"]', "probability": 0.0},
    "Nada": {"id": '//*[@id="i17"]', "probability": 0.0},
}

#  ¿Considerás que las oportunidades laborales futuras en el campo de IT son un factor motivador para continuar con tus estudios actuales?
estudiante_futuro_laboral = {
    "si": {"id": '//*[@id="i24"]', "probability": 0.0},
    "no": {"id": '//*[@id="i27"]', "probability": 0.0},
    "no sabe": {"id": '//*[@id="i30"]', "probability": 0.0},
}

#   ¿Alguna vez pensaste en abandonar la carrera?
estudiante_abandonar_carrera = {
    "si": {"id": '//*[@id="i37"]', "probability": 0.0},
    "no": {"id": '//*[@id="i40"]', "probability": 0.0},
}

#  pregunta
campo = {
    "asd": {"id": '//*[@id="i"]', "probability": 0.0},
    "asd": {"id": '//*[@id="i"]', "probability": 0.0},
    "asd": {"id": '//*[@id="i"]', "probability": 0.0},
    "asd": {"id": '//*[@id="i"]', "probability": 0.0},
}
