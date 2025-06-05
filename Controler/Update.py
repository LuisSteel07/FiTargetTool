import sqlite3
import json

from Controler.Controler import get_routine, get_client
from Model.Dia import Dia
from Model.Peso import Peso
from Model.Progreso import Progreso
from Model.Rutina import Rutina
from Model.Ejercicios import Ejercicios
from Utils.generate_models_json import generate_models_ejercicio_json


def update_client(id: int, nombre: str, edad: int, rutina: int, progreso: int, pesos: int, foto: str):
    conn = sqlite3.connect("Clientes.db")
    cur = conn.cursor()

    query = (
        f"UPDATE Cliente set Nombre = '{nombre}', Edad = {edad}, Rutina = {rutina}, Progreso = {progreso}, Pesos = "
        f"{pesos}, Foto = '{foto}' where id = {id}")

    cur.execute(query)
    conn.commit()

    conn.close()


def update_rutina(id: int, day: str, ejercise: Ejercicios):
    new_routine: str = ""
    conn = sqlite3.connect("Clientes.db")
    cur = conn.cursor()

    routine = get_routine(id)

    if day == Dia.LUNES.value:
        routine.lunes.append(ejercise)
        new_routine = json.dumps({"ejers": generate_models_ejercicio_json(routine.lunes)})
    elif day == Dia.MARTES.value:
        routine.martes.append(ejercise)
        new_routine = json.dumps({"ejers": generate_models_ejercicio_json(routine.martes)})
    elif day == Dia.MIERCOLES.value:
        routine.miercoles.append(ejercise)
        new_routine = json.dumps({"ejers": generate_models_ejercicio_json(routine.miercoles)})
    elif day == Dia.JUEVES.value:
        routine.jueves.append(ejercise)
        new_routine = json.dumps({"ejers": generate_models_ejercicio_json(routine.jueves)})
    elif day == Dia.VIERNES.value:
        routine.viernes.append(ejercise)
        new_routine = json.dumps({"ejers": generate_models_ejercicio_json(routine.viernes)})
    elif day == Dia.SABADO.value:
        routine.sabado.append(ejercise)
        new_routine = json.dumps({"ejers": generate_models_ejercicio_json(routine.sabado)})
    elif day == Dia.DOMINGO.value:
        routine.domingo.append(ejercise)
        new_routine = json.dumps({"ejers": generate_models_ejercicio_json(routine.domingo)})

    cur.execute(f"UPDATE Rutina set {day} = '{new_routine}' where id = {id}")
    conn.commit()
    conn.close()


def update_peso(id: int, new_peso):
    conn = sqlite3.connect("Clientes.db")
    cur = conn.cursor()

    fetch_data = cur.execute(f"SELECT * from Pesos WHERE ID = {id}").fetchone()
    pesos = Peso(id, json.loads(fetch_data[1])["pesos"])

    pesos.list_pesos.append(new_peso)

    new_pesos = json.JSONEncoder().encode({"pesos": pesos.list_pesos})

    cur.execute(f"Update Pesos SET pesos = '{new_pesos}' where id = {id}")
    conn.commit()

    conn.close()


def update_progress(id: int, datas: list):
    conn = sqlite3.connect("Clientes.db")
    cur = conn.cursor()

    fetch_data = cur.execute(f"SELECT * from Progreso WHERE ID = {id}").fetchone()

    progress = Progreso(id,
                        json.loads(fetch_data[1])["progress"],
                        json.loads(fetch_data[2])["progress"],
                        json.loads(fetch_data[3])["progress"],
                        json.loads(fetch_data[4])["progress"],
                        json.loads(fetch_data[5])["progress"],
                        json.loads(fetch_data[6])["progress"],
                        json.loads(fetch_data[7])["progress"],
                        json.loads(fetch_data[8])["progress"],
                        json.loads(fetch_data[9])["progress"],
                        json.loads(fetch_data[10])["progress"],
                        json.loads(fetch_data[11])["progress"],
                        json.loads(fetch_data[12])["progress"],
                        json.loads(fetch_data[13])["progress"],
                        json.loads(fetch_data[14])["progress"],
                        json.loads(fetch_data[15])["progress"]
                        )

    for i in range(0, 14):
        if i == 0:
            progress.pecho.append(datas[i])

            new_progress = json.JSONEncoder().encode({"progress": progress.pecho})

            cur.execute(f"UPDATE Progreso SET Pecho = '{new_progress}' where id = {id}")
            conn.commit()
        elif i == 1:
            progress.trapecio.append(datas[i])

            new_progress = json.JSONEncoder().encode({"progress": progress.trapecio})

            cur.execute(f"UPDATE Progreso SET trapecio = '{new_progress}' where id = {id}")
            conn.commit()
        elif i == 2:
            progress.romboides.append(datas[i])

            new_progress = json.JSONEncoder().encode({"progress": progress.romboides})

            cur.execute(f"UPDATE Progreso SET romboides = '{new_progress}' where id = {id}")
            conn.commit()
        elif i == 3:
            progress.dorsal.append(datas[i])

            new_progress = json.JSONEncoder().encode({"progress": progress.dorsal})

            cur.execute(f"UPDATE Progreso SET dorsal = '{new_progress}' where id = {id}")
            conn.commit()
        elif i == 4:
            progress.espalda_baja.append(datas[i])

            new_progress = json.JSONEncoder().encode({"progress": progress.espalda_baja})

            cur.execute(f"UPDATE Progreso SET espaldabaja = '{new_progress}' where id = {id}")
            conn.commit()
        elif i == 5:
            progress.biceps.append(datas[i])

            new_progress = json.JSONEncoder().encode({"progress": progress.biceps})

            cur.execute(f"UPDATE Progreso SET biceps = '{new_progress}' where id = {id}")
            conn.commit()
        elif i == 6:
            progress.triceps.append(datas[i])

            new_progress = json.JSONEncoder().encode({"progress": progress.triceps})

            cur.execute(f"UPDATE Progreso SET triceps = '{new_progress}' where id = {id}")
            conn.commit()
        elif i == 7:
            progress.ante_brazo.append(datas[i])

            new_progress = json.JSONEncoder().encode({"progress": progress.ante_brazo})

            cur.execute(f"UPDATE Progreso SET antebrazo = '{new_progress}' where id = {id}")
            conn.commit()
        elif i == 8:
            progress.deltoide_posterior.append(datas[i])

            new_progress = json.JSONEncoder().encode({"progress": progress.deltoide_posterior})

            cur.execute(f"UPDATE Progreso SET deltoideposterior = '{new_progress}' where id = {id}")
            conn.commit()
        elif i == 9:
            progress.deltoide_lateral.append(datas[i])

            new_progress = json.JSONEncoder().encode({"progress": progress.deltoide_lateral})

            cur.execute(f"UPDATE Progreso SET deltoidelateral = '{new_progress}' where id = {id}")
            conn.commit()
        elif i == 10:
            progress.deltoide_anterior.append(datas[i])

            new_progress = json.JSONEncoder().encode({"progress": progress.deltoide_anterior})

            cur.execute(f"UPDATE Progreso SET deltoideanterior = '{new_progress}' where id = {id}")
            conn.commit()
        elif i == 11:
            progress.cuadriceps.append(datas[i])

            new_progress = json.JSONEncoder().encode({"progress": progress.cuadriceps})

            cur.execute(f"UPDATE Progreso SET cuadriceps = '{new_progress}' where id = {id}")
            conn.commit()
        elif i == 12:
            progress.isquiotibiales.append(datas[i])

            new_progress = json.JSONEncoder().encode({"progress": progress.isquiotibiales})

            cur.execute(f"UPDATE Progreso SET isq = '{new_progress}' where id = {id}")
            conn.commit()
        elif i == 13:
            progress.gluteos.append(datas[i])

            new_progress = json.JSONEncoder().encode({"progress": progress.gluteos})

            cur.execute(f"UPDATE Progreso SET gluteos = '{new_progress}' where id = {id}")
            conn.commit()
        elif i == 14:
            progress.pantorrillas.append(datas[i])

            new_progress = json.JSONEncoder().encode({"progress": progress.pantorrillas})

            cur.execute(f"UPDATE Progreso SET pantorrillas = '{new_progress}' where id = {id}")
            conn.commit()

    conn.close()


def change_rutine(rutine: int, client_id: int):
    conn = sqlite3.connect("Clientes.db")
    cur = conn.cursor()

    cur.execute(f"UPDATE Cliente set Rutina = {rutine} where id = {client_id}")
    conn.commit()
    c= get_client(client_id=client_id)
    print(c.rutina.id)
    conn.close()


def update_client_data(id: int, nombre: str, edad: int, photo: str):
    conn = sqlite3.connect("Clientes.db")
    cur = conn.cursor()

    query = f"UPDATE Cliente set Nombre = '{nombre}', Edad = {edad}, Foto = '{photo}'  where id = {id}"

    cur.execute(query)
    conn.commit()
    conn.close()


def update_routine_full_day(identifier: int, day: str, list_ejers: list[Ejercicios]):
    conn = sqlite3.connect("Clientes.db")
    cur = conn.cursor()

    routine_ejers = json.JSONEncoder().encode({"ejers": generate_models_ejercicio_json(list_ejers)})

    cur.execute(f"UPDATE Rutina set {day} = '{routine_ejers}' where id = {identifier}")

    conn.commit()
    conn.close()


def update_full_routine(identifier: int, routine: Rutina):
    for day in range(0, 6):
        if day == 0:
            update_routine_full_day(identifier, Dia.LUNES.value, routine.lunes)
        if day == 1:
            update_routine_full_day(identifier, Dia.MARTES.value, routine.martes)
        if day == 2:
            update_routine_full_day(identifier, Dia.MIERCOLES.value, routine.miercoles)
        if day == 3:
            update_routine_full_day(identifier, Dia.JUEVES.value, routine.jueves)
        if day == 4:
            update_routine_full_day(identifier, Dia.VIERNES.value, routine.viernes)
        if day == 5:
            update_routine_full_day(identifier, Dia.SABADO.value, routine.sabado)
        if day == 6:
            update_routine_full_day(identifier, Dia.DOMINGO.value, routine.domingo)
