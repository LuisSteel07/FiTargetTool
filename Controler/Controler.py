import sqlite3
import json

from Model.Cliente import Cliente
from Model.Peso import Peso
from Model.Rutina import Rutina
from Model.Progreso import Progreso


def get_rutine(id: int) -> Rutina:
    conn = sqlite3.connect("Clientes.db")
    cur = conn.cursor()

    rutine = cur.execute(f"select * from Rutina where id = {id}").fetchone()

    return Rutina(id,
                  rutine[1],
                  json.loads(rutine[2])["ejers"],
                  json.loads(rutine[3])["ejers"],
                  json.loads(rutine[4])["ejers"],
                  json.loads(rutine[5])["ejers"],
                  json.loads(rutine[6])["ejers"],
                  json.loads(rutine[7])["ejers"],
                  json.loads(rutine[8])["ejers"]
                  )


def get_progress(id: int) -> Progreso:
    conn = sqlite3.connect("Clientes.db")
    cur = conn.cursor()

    progress = cur.execute(f"SELECT * from Progreso WHERE ID = {id}").fetchone()
    conn.close()

    return Progreso(id,
                    json.loads(progress[1])["progress"],
                    json.loads(progress[2])["progress"],
                    json.loads(progress[3])["progress"],
                    json.loads(progress[4])["progress"],
                    json.loads(progress[5])["progress"],
                    json.loads(progress[6])["progress"],
                    json.loads(progress[7])["progress"],
                    json.loads(progress[8])["progress"],
                    json.loads(progress[9])["progress"],
                    json.loads(progress[10])["progress"],
                    json.loads(progress[11])["progress"],
                    json.loads(progress[12])["progress"],
                    json.loads(progress[13])["progress"],
                    json.loads(progress[14])["progress"],
                    json.loads(progress[15])["progress"]
                    )


def get_pesos(id: int) -> Peso:
    conn = sqlite3.connect("Clientes.db")
    cur = conn.cursor()

    pesos = cur.execute(f"SELECT * from Pesos WHERE ID = {id}").fetchone()
    conn.close()

    return Peso(id, json.loads(pesos[1])["pesos"])


def get_client(name: str) -> Cliente:
    conn = sqlite3.connect("Clientes.db")
    cur = conn.cursor()

    client = cur.execute(f"SELECT * from Cliente WHERE Nombre = '{name}'").fetchone()

    client_id = client[0]
    name = client[1]
    age = client[2]
    rutine = client[3]
    progress = client[4]
    pesos = client[5]
    photo = client[6]

    conn.close()
    return Cliente(client_id, name, age, get_rutine(rutine), get_progress(progress), get_pesos(pesos), photo)


def get_list_names() -> list[str]:
    conn = sqlite3.connect("Clientes.db")
    cur = conn.cursor()

    names_db = cur.execute("select Nombre from Cliente").fetchall()
    conn.close()

    names = list()
    for name in names_db:
        names.append(name[0])

    return names


def get_all_data() -> list[Cliente]:
    conn = sqlite3.connect("Clientes.db")
    cur = conn.cursor()

    list_clients: list[Cliente] = []

    clients = cur.execute("SELECT * from Cliente").fetchall()

    for client in clients:
        list_clients.append(Cliente(
            client[0],
            client[1],
            client[2],
            client[3],
            client[4],
            client[5],
            client[6]
        ))

    conn.close()
    return list_clients


def get_list_id_rutines() -> list[int]:
    conn = sqlite3.connect("Clientes.db")
    cur = conn.cursor()

    list_id: list[int] = []

    ids = cur.execute("select id from Rutina").fetchall()

    for i in ids:
        list_id.append(i[0])

    conn.close()
    return list_id

get_all_data()