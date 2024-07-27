import sqlite3
from Controler.Update import update_progress


def create_client(nombre: str, edad: int, rutina: int, foto: str, data_progress: list):
    conn = sqlite3.connect("Clientes.db")
    cur = conn.cursor()

    query = (f'insert into Cliente (Nombre, Edad, Rutina, Progreso, Pesos, Foto) values("{nombre}", {edad}, {rutina}, '
             f'{create_progress(data_progress)}, {create_pesos()}, "{foto}")')

    cur.execute(query)
    conn.commit()


def create_pesos() -> int:
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
            return e
        else:
            e = e + 1
            continue


def create_routine():
    conn = sqlite3.connect("Clientes.db")
    cur = conn.cursor()

    query = ("insert into Rutina (lunes, martes, miercoles, jueves, viernes, sabado, domingo) values('{\"ejers\":[]}',"
             "'{\"ejers\":[]}','{\"ejers\":[]}','{\"ejers\":[]}','{\"ejers\":[]}','{\"ejers\":[]}','{\"ejers\":[]}')")

    cur.execute(query)

    conn.commit()


def create_progress(data: list) -> int:
    conn = sqlite3.connect("Clientes.db")
    cur = conn.cursor()

    query = ("insert into Progreso (pecho, trapecio, romboides, dorsal, espaldabaja, biceps, triceps, antebrazo, deltoideposterior, deltoidelateral, deltoideanterior, cuadriceps, isq, gluteos, pantorrillas) "
             "values('{\"progress\":[]}','{\"progress\":[]}','{\"progress\":[]}','{\"progress\":[]}','{\"progress\":[]}',"
             "'{\"progress\":[]}','{\"progress\":[]}','{\"progress\":[]}','{\"progress\":[]}','{\"progress\":[]}',"
             "'{\"progress\":[]}','{\"progress\":[]}','{\"progress\":[]}','{\"progress\":[]}','{\"progress\":[]}')")
    cur.execute(query)
    conn.commit()

    update_progress(
        cur.execute(f"select Max(id) from Cliente").fetchone()[0],
        data
    )

    return cur.execute(f"select Max(id) from Cliente").fetchone()[0]

