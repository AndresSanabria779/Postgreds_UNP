"""
1.	Cree un base de datos en PostgreSQL llamada “PruebaUNP_<su_nombre>” (elija los puertos, nombre de usuario y contraseña que desee para crear la base).

"""

import psycopg2
from psycopg2 import sql

# Configuración de la conexión

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
)


conn.autocommit = True
cursor = conn.cursor()
"""
2.	Cree una tabla llamada “Usuarios” que contenga las siguientes columnas:
-	id: Es de tipo Entero, autoincremental y es la Primary Key de la tabla.
-	nombreUsuario: Es de tipo VarChar, no se puede repetir en la tabla.
-	contraseña: Es de tipo VarChar. 

"""
# Crear el usuario
cursor.execute("CREATE USER tu_usuario WITH PASSWORD '1234';")

# Crear la base de datos
cursor.execute("CREATE DATABASE PruebaUNP_JairoAndresSanabriaTorres;")

# Otorgar todos los privilegios al usuario sobre la base de datos
cursor.execute("GRANT ALL PRIVILEGES ON DATABASE PruebaUNP_JairoAndresSanabriaTorres TO UNP;")

# Cerrar la conexión
cursor.close()
conn.close()

"""
3.	Cree una tabla llamada “Beneficiarios” que contenga las siguientes columnas:
-	cedula: Es de tipo Entero y es la primary key de la tabla, no se puede repetir.
-	nombre: Es de tipo VarChar.
-	direccion: Es de tipo VarChar.
-	poblacion: Es de tipo VarChar.

"""
# Crear la tabla Beneficiarios
cursor.execute("""
    CREATE TABLE Beneficiarios (
        cedula INTEGER PRIMARY KEY,
        nombre VARCHAR(255),
        direccion VARCHAR(255),
        poblacion VARCHAR(255)
    );
""")
"""
4.	Cree una tabla llamada “Chalecos” con las siguientes columnas:
-	serial: Es de tipo Entero y es la Primary Key de la tabla.
-	beneficiario_cedula: Es de tipo Entero, y es la Foreign Key de la columna “cedula” de la tabla “Beneficiarios”, debe tener eliminación por cascada.
"""
# Crear la tabla Chalecos
cursor.execute("""
    CREATE TABLE Chalecos (
        serial INTEGER PRIMARY KEY,
        beneficiario_cedula INTEGER,
        FOREIGN KEY (beneficiario_cedula) REFERENCES Beneficiarios(cedula) ON DELETE CASCADE
    );
""")

# Cerrar la conexión
cursor.close()
conn.close()
