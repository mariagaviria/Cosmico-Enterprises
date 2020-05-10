import flask 
from flask import Flask, redirect, url_for, request, render_template
import pandas 
import psycopg2 

"""
Se crea la aplicación.
"""

app = flask.Flask(__name__)
app.config["DEBUG"] = True 

"""
Parámetros de conexión.
"""

parametrosDict = {
    "host": "isilo.db.elephantsql.com",
    "database": "eeubnhhz",
    "user": "eeubnhhz",
    "password": "Q3S6Rze1cdcsnnIi3aS9mMekOkQz2r4y"
}

"""
Función que retorna un data_frame dado un query.
"""
def query2DataFrame(sqlQuery):
    DBConnection = None 
    resultDataFrame = None
    try: 
        print("Connecting to database...")
        DBConnection = psycopg2.connect(**parametrosDict)
        resultDataFrame = pandas.read_sql_query(sqlQuery, DBConnection)
        DBConnection.close()
        return resultDataFrame
    except(Exception, psycopg2.DatabaseError) as error:
        print("Error en el query: ",error)
        return None 
    finally:
        if DBConnection is not None:
            DBConnection.close()

"""
Por acá debe ir la creación de los grafos.
Además, una función que reciba origen, destino, atributo a minimizar
y retorne el diccionario con los ids de las estaciones.
"""

"""
Ahora si, rutas de la aplicación
"""

@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")

@app.route("/estaciones", methods=["GET"])
def mostrarEstaciones():
    query = "SELECT * FROM estacion"
    tabla = query2DataFrame(query)
    return tabla.to_html()

@app.route("/mapa", methods=["GET"])
def mostrarMapa():
    return render_template("map.html")

@app.route("/registro", methods=["GET"])
def formulario():
    return app.send_static_file("registroCliente.html")

@app.route("/resultadoRegistro",methods=["POST","GET"])
def registrarse():
    identificacion = str(request.values.get("ID"))
    nombre = str(request.values.get("Nombre"))
    apellido = str(request.values.get("Apellido"))
    email = str(request.values.get("Email"))
    telefono = str(request.values.get("Telefono"))
    DBConnection = None
    try:
        print("Connecting to database...")
        DBConnection = psycopg2.connect(**parametrosDict)
        cursorDB = DBConnection.cursor()
        if telefono == "":
            query = "INSERT INTO cliente(cliente_id, nombre, apellido, email) VALUES("+identificacion+",'"+nombre+"','"+apellido+"','"+email+"')"
        else:
            query = "INSERT INTO cliente(cliente_id, nombre, apellido, email, telefono) VALUES("+identificacion+",'"+nombre+"','"+apellido+"','"+email+"',"+telefono+")"
        cursorDB.execute(query)
        DBConnection.commit()
        DBConnection.close()
        return "Todo en orden!"
    except:
        return "Ocurrió un error... Vuélvalo a intentar."
    finally:
        if DBConnection is not None:
            DBConnection.close()

@app.route("/planearViaje", methods=["GET"])
def ingresoDatos():
    return app.send_static_file("buscarRuta.html")

@app.route("/resultadoRuta",methods=["POST","GET"])
def mostrarRuta():
    return "Aqui iriá algo fancy pero ajá"

app.run()
