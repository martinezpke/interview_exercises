""" 
    Pregunta 5: Bases de Datos y Consultas SQL
    Dada una tabla "Clientes" con columnas "ID", "Nombre" y "Edad", 
    escribe una consulta SQL para seleccionar todos los clientes mayores de 18 años.

"""

import sqlite3

# ------------------- Creacion de base de datos 
conexion = sqlite3.connect("base_de_datos.db")
cursor = conexion.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Clientes (
        ID INTEGER PRIMARY KEY,
        Nombre TEXT NOT NULL,
        Edad INTEGER NOT NULL
    )
""")

data = [
    ("Kevin", 20),
    ("Kemapa", 20),
    ("Carlos", 16),
    ("Maria", 19)
]

cursor.executemany("INSERT INTO Clientes (Nombre, Edad) VALUES (?, ?)", data)

conexion.close()

print("Base de datos y tabla creadas con éxito.")

#------------------- Consulta de personas mayores de 18

conexion = sqlite3.connect("base_de_datos.db")
cursor = conexion.cursor()


consulta = "SELECT Nombre FROM Clientes WHERE Edad > 18"
cursor.execute(consulta)
clientes_mayores = cursor.fetchall()

print("Clientes mayores de 18 años:")
for cliente in clientes_mayores:
    print(cliente[0])

conexion.close()
