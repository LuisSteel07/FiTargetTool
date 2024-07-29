import sqlite3
import json
from Model.Dia import Dia
from Model.Peso import Peso
from Model.Progreso import Progreso
from Model.Rutina import Rutina


def update_client(id: int, nombre: str, edad: int, rutina: int, progreso: int, pesos: int, foto: str):
    conn = sqlite3.connect("Clientes.db")
    cur = conn.cursor()

    query = (
        f"UPDATE Cliente set Nombre = '{nombre}', Edad = {edad}, Rutina = {rutina}, Progreso = {progreso}, Pesos = "
        f"{pesos}, Foto = '{foto}' where id = {id}")

    cur.execute(query)
    conn.commit()

    conn.close()


def update_rutina(id: int, day: str, ejercise: str):
    new_rutina = 0
    conn = sqlite3.connect("Clientes.db")
    cur = conn.cursor()

    fetch_data = cur.execute(f"select * from Rutina where id = {id}").fetchone()

    rutina = Rutina(id,
                    fetch_data[1],
                    json.loads(fetch_data[2])["ejers"],
                    json.loads(fetch_data[3])["ejers"],
                    json.loads(fetch_data[4])["ejers"],
                    json.loads(fetch_data[5])["ejers"],
                    json.loads(fetch_data[6])["ejers"],
                    json.loads(fetch_data[7])["ejers"],
                    json.loads(fetch_data[8])["ejers"]
                    )

    if day == Dia.LUNES.value:
        rutina.lunes.append(ejercise)
        new_rutina = json.JSONEncoder().encode({"ejers": rutina.lunes})
    elif day == Dia.MARTES.value:
        rutina.martes.append(ejercise)
        new_rutina = json.JSONEncoder().encode({"ejers": rutina.martes})
    elif day == Dia.MIERCOLES.value:
        rutina.miercoles.append(ejercise)
        new_rutina = json.JSONEncoder().encode({"ejers": rutina.miercoles})
    elif day == Dia.JUEVES.value:
        rutina.jueves.append(ejercise)
        new_rutina = json.JSONEncoder().encode({"ejers": rutina.jueves})
    elif day == Dia.VIERNES.value:
        rutina.viernes.append(ejercise)
        new_rutina = json.JSONEncoder().encode({"ejers": rutina.viernes})
    elif day == Dia.SABADO.value:
        rutina.sabado.append(ejercise)
        new_rutina = json.JSONEncoder().encode({"ejers": rutina.sabado})
    elif day == Dia.DOMINGO.value:
        rutina.domingo.append(ejercise)
        new_rutina = json.JSONEncoder().encode({"ejers": rutina.domingo})

    cur.execute(f"UPDATE Rutina set {day} = '{new_rutina}' where id = {id}")
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
    conn.close()


def update_client_data(id: int, nombre: str, edad: int):
    conn = sqlite3.connect("Clientes.db")
    cur = conn.cursor()

    query = f"UPDATE Cliente set Nombre = '{nombre}', Edad = {edad} where id = {id}"

    cur.execute(query)
    conn.commit()
    conn.close()
