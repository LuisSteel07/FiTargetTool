from Model.Ejercicios import Ejercicios


def generate_models_ejercicio_json(ejercicios: list[Ejercicios]) -> list[dict]:
    list_ejers: list[dict] = []

    for ejer in ejercicios:
        dict_ejers = {
            "name": ejer.name[0],
            "reps": ejer.reps[0],
            "weights": ejer.weights
        }
        list_ejers.append(dict_ejers)

    return list_ejers