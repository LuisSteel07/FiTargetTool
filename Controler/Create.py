import sqlite3
from Controler.Update import update_progress, update_peso


def create_client(nombre: str, edad: int, peso: int, rutina: int, foto: str, data_progress: list):
    conn = sqlite3.connect("Clientes.db")
    cur = conn.cursor()

    query = (f'insert into Cliente (Nombre, Edad, Rutina, Progreso, Pesos, Foto) values("{nombre}", {edad}, {rutina}, '
             f'{create_progress(data_progress)}, {create_pesos(peso)}, "{foto}")')

    cur.execute(query)
    conn.commit()
    conn.close()


def create_pesos(initial_peso) -> int:
    conn = sqlite3.connect("Clientes.db")
    cur = conn.cursor()

    e: int = 1
    while True:
        id = cur.execute(f"select id from Pesos where id = {e}").fetchone()
        if id is None:
            query = (f"insert into Pesos (id, pesos) values({e}"
                     ",'{\"pesos\":[]}')")
            cur.execute(query)
            conn.commit()
            conn.close()
            update_peso(e, initial_peso)
            return e
        else:
            e = e + 1
            continue


def create_routine(nombre: str):
    conn = sqlite3.connect("Clientes.db")
    cur = conn.cursor()

    query = (f"insert into Rutina (nombre, lunes, martes, miercoles, jueves, viernes, sabado, domingo) values('{nombre}',"
             "'{\"ejers\":[]}','{\"ejers\":[]}','{\"ejers\":[]}','{\"ejers\":[]}','{\"ejers\":[]}','{\"ejers\":[]}',"
             "'{\"ejers\":[]}')")

    cur.execute(query)
    conn.commit()
    conn.close()


def create_progress(data: list) -> int:
    conn = sqlite3.connect("Clientes.db")
    cur = conn.cursor()

    query = (
        "insert into Progreso (pecho, trapecio, romboides, dorsal, espaldabaja, biceps, triceps, antebrazo, "
        "deltoideposterior, deltoidelateral, deltoideanterior, cuadriceps, isq, gluteos, pantorrillas)"
        "values('{\"progress\":[]}','{\"progress\":[]}','{\"progress\":[]}','{\"progress\":[]}','{\"progress\":[]}',"
        "'{\"progress\":[]}','{\"progress\":[]}','{\"progress\":[]}','{\"progress\":[]}','{\"progress\":[]}',"
        "'{\"progress\":[]}','{\"progress\":[]}','{\"progress\":[]}','{\"progress\":[]}','{\"progress\":[]}')")
    cur.execute(query)
    conn.commit()

    update_progress(
        cur.execute(f"select Max(id) from Progreso").fetchone()[0],
        data
    )

    id = cur.execute(f"select Max(id) from Progreso").fetchone()[0]
    conn.close()
    return id

