import sqlite3
from Model.Cliente import Cliente


def delete_client(client: Cliente):
    conn = sqlite3.connect("Clientes.db")
    cur = conn.cursor()

    cur.execute(f"DELETE from Cliente where id = {client.id}")
    cur.execute(f"DELETE FROM Progreso WHERE id = {client.progreso.id}")
    cur.execute(f"DELETE FROM Pesos WHERE id = {client.pesos.id}")

    conn.commit()


def delete_routine(id: int):
    conn = sqlite3.connect("Clientes.db")
    cur = conn.cursor()

    cur.execute(f"DELETE from Rutina where id = {id}")
    conn.commit()


def delete_peso(id: int):
    conn = sqlite3.connect("Clientes.db")
    cur = conn.cursor()

    cur.execute(f"DELETE from Pesos where id = {id}")
    conn.commit()


def delete_progress(id: int):
    conn = sqlite3.connect("Clientes.db")
    cur = conn.cursor()

    cur.execute(f"DELETE from Progreso where id = {id}")
    conn.commit()
