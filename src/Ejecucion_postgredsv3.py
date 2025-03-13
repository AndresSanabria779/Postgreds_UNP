import psycopg2
from psycopg2 import sql




# 1. Configuración de la conexión inicial a la base de datos "postgres" para crear usuario y base de datos
conn = psycopg2.connect(
    dbname="postgres",  # Conexión a la base de datos "postgres"
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
)

conn.autocommit = True
cursor = conn.cursor()

print("Conexión exitosa"+"."*50)



# 2. Crear el usuario
cursor.execute("CREATE USER ANDRES WITH PASSWORD '1234';")
print("Usuario creado"+"."*50)

# 3. Crear la base de datos
cursor.execute("CREATE DATABASE PruebaUNP_JairoAndresSanabriaTorres;")
print("Base de datos creada"+"."*50)
# 4. Otorgar todos los privilegios al usuario sobre la base de datos
cursor.execute("GRANT ALL PRIVILEGES ON DATABASE PruebaUNP_JairoAndresSanabriaTorres TO ANDRES;")
print("Privilegios otorgados"+"."*50)
# Cerrar la conexión con la base de datos "postgres"
cursor.close()
conn.close()






# 5. Conectarse a la nueva base de datos "PruebaUNP_JairoAndresSanabriaTorres"
conn = psycopg2.connect(
    dbname="pruebaunp_jairoandressanabriatorres",  # Conexión a la base de datos recién creada
    user="postgres",  # O el usuario que hayas creado
    password="1234",
    host="localhost",
    port="5432"
)

conn.autocommit = True
cursor = conn.cursor()

# 6. Crear la tabla "Beneficiarios"
cursor.execute("""
    CREATE TABLE Beneficiarios (
        cedula INTEGER PRIMARY KEY,
        nombre VARCHAR(255),
        direccion VARCHAR(255),
        poblacion VARCHAR(255)
    );
""")

# 7. Crear la tabla "Chalecos"
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
