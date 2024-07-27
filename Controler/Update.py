from Controler import *
import json
from Model.Dia import Dia


def update_client(id: int, nombre: str, edad: int, rutina: int, progreso: int, pesos: int, foto: str):
    conn = sqlite3.connect("Clientes.db")
    cur = conn.cursor()

    query = (
        f"UPDATE Cliente set Nombre = '{nombre}', Edad = {edad}, Rutina = {rutina}, Progreso = {progreso}, Pesos = "
        f"{pesos}, Foto = '{foto}' where id = {id}")

    cur.execute(query)
    conn.commit()


def update_rutina(id: int, day: str, ejercise: str):
    new_rutina = 0
    conn = sqlite3.connect("Clientes.db")
    cur = conn.cursor()

    rutina = get_rutine(id)

    if day == Dia.LUNES.value:
        rutina.lunes.append(ejercise)
        new_rutina = json.JSONEncoder().encode({"ejers": rutina.lunes})
    if day == Dia.MARTES.value:
        rutina.martes.append(ejercise)
        new_rutina = json.JSONEncoder().encode({"ejers": rutina.martes})
    if day == Dia.MIERCOLES.value:
        rutina.miercoles.append(ejercise)
        new_rutina = json.JSONEncoder().encode({"ejers": rutina.miercoles})
    if day == Dia.JUEVES.value:
        rutina.jueves.append(ejercise)
        new_rutina = json.JSONEncoder().encode({"ejers": rutina.jueves})
    if day == Dia.VIERNES.value:
        rutina.viernes.append(ejercise)
        new_rutina = json.JSONEncoder().encode({"ejers": rutina.viernes})
    if day == Dia.SABADO.value:
        rutina.sabado.append(ejercise)
        new_rutina = json.JSONEncoder().encode({"ejers": rutina.sabado})
    if day == Dia.DOMINGO.value:
        rutina.domingo.append(ejercise)
        new_rutina = json.JSONEncoder().encode({"ejers": rutina.domingo})

    cur.execute(f"UPDATE Rutina set {day} = '{new_rutina}' where id = {id}")
    conn.commit()


def update_peso(id: int, new_peso):
    conn = sqlite3.connect("Clientes.db")
    cur = conn.cursor()

    pesos = get_pesos(id)
    pesos.list_pesos.append(new_peso)

    new_pesos = json.JSONEncoder().encode({"pesos": pesos.list_pesos})

    cur.execute(f"Update Pesos SET pesos = '{new_pesos}' where id = {id}")
    conn.commit()


def update_progress(id: int, datas: list):
    conn = sqlite3.connect("Clientes.db")
    cur = conn.cursor()

    progress = get_progress(id)

    for i in range(0, 14):
        if i == 0:
            progress.pecho.append(datas[i])

            new_progress = json.JSONEncoder().encode({"progress": progress.pecho})

            cur.execute(f"UPDATE Progreso SET Pecho = '{new_progress}' where id = {id}")
            conn.commit()
        if i == 1:
            progress.trapecio.append(datas[i])

            new_progress = json.JSONEncoder().encode({"progress": progress.trapecio})

            cur.execute(f"UPDATE Progreso SET trapecio = '{new_progress}' where id = {id}")
            conn.commit()
        if i == 2:
            progress.romboides.append(datas[i])

            new_progress = json.JSONEncoder().encode({"progress": progress.romboides})

            cur.execute(f"UPDATE Progreso SET romboides = '{new_progress}' where id = {id}")
            conn.commit()
        if i == 3:
            progress.dorsal.append(datas[i])

            new_progress = json.JSONEncoder().encode({"progress": progress.dorsal})

            cur.execute(f"UPDATE Progreso SET dorsal = '{new_progress}' where id = {id}")
            conn.commit()
        if i == 4:
            progress.espalda_baja.append(datas[i])

            new_progress = json.JSONEncoder().encode({"progress": progress.espalda_baja})

            cur.execute(f"UPDATE Progreso SET espaldabaja = '{new_progress}' where id = {id}")
            conn.commit()
        if i == 5:
            progress.biceps.append(datas[i])

            new_progress = json.JSONEncoder().encode({"progress": progress.biceps})

            cur.execute(f"UPDATE Progreso SET biceps = '{new_progress}' where id = {id}")
            conn.commit()
        if i == 6:
            progress.triceps.append(datas[i])

            new_progress = json.JSONEncoder().encode({"progress": progress.triceps})

            cur.execute(f"UPDATE Progreso SET triceps = '{new_progress}' where id = {id}")
            conn.commit()
        if i == 7:
            progress.ante_brazo.append(datas[i])

            new_progress = json.JSONEncoder().encode({"progress": progress.ante_brazo})

            cur.execute(f"UPDATE Progreso SET antebrazo = '{new_progress}' where id = {id}")
            conn.commit()
        if i == 8:
            progress.deltoide_posterior.append(datas[i])

            new_progress = json.JSONEncoder().encode({"progress": progress.deltoide_posterior})

            cur.execute(f"UPDATE Progreso SET deltoideposterior = '{new_progress}' where id = {id}")
            conn.commit()
        if i == 9:
            progress.deltoide_lateral.append(datas[i])

            new_progress = json.JSONEncoder().encode({"progress": progress.deltoide_lateral})

            cur.execute(f"UPDATE Progreso SET deltoidelateral = '{new_progress}' where id = {id}")
            conn.commit()
        if i == 10:
            progress.deltoide_anterior.append(datas[i])

            new_progress = json.JSONEncoder().encode({"progress": progress.deltoide_anterior})

            cur.execute(f"UPDATE Progreso SET deltoideanterior = '{new_progress}' where id = {id}")
            conn.commit()
        if i == 11:
            progress.cuadriceps.append(datas[i])

            new_progress = json.JSONEncoder().encode({"progress": progress.cuadriceps})

            cur.execute(f"UPDATE Progreso SET cuadriceps = '{new_progress}' where id = {id}")
            conn.commit()
        if i == 12:
            progress.isquiotibiales.append(datas[i])

            new_progress = json.JSONEncoder().encode({"progress": progress.isquiotibiales})

            print(new_progress)

            cur.execute(f"UPDATE Progreso SET isq = '{new_progress}' where id = {id}")
            conn.commit()
        if i == 13:
            progress.gluteos.append(datas[i])

            new_progress = json.JSONEncoder().encode({"progress": progress.gluteos})

            cur.execute(f"UPDATE Progreso SET gluteos = '{new_progress}' where id = {id}")
            conn.commit()
        if i == 14:
            progress.pantorrillas.append(datas[i])

            new_progress = json.JSONEncoder().encode({"progress": progress.pantorrillas})

            cur.execute(f"UPDATE Progreso SET pantorrillas = '{new_progress}' where id = {id}")
            conn.commit()
