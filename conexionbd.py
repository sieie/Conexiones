#comando para instalar la librería de mysql en python:  "pip install mysql-conector-python"

import mysql.connector

# Configura los parámetros de la conexión
config = {
  'user': 'nombre_de_usuario',
  'password': 'contraseña',
  'host': 'nombre_del_servidor',
  'database': 'nombre_de_la_base_de_datos',
  'raise_on_warnings': True
}

try:
    # Crea la conexión
    conect = mysql.connector.connect(**config)
    
    # Realiza alguna operación en la base de datos
    print("Conexión exitosa")
    
    # Cierra la conexión
    conect.close()
except mysql.connector.Error as err:
    print("Error de conexión: {}".format(err))
