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
Ahora si, rutas de la aplicación
"""

@app.route("/", methods=["GET"])
def home():
    return "Buenas buenas!"

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
    except(Exception, psycopg2.DatabaseError) as error:
        return "Error en el query "+error
    finally:
        if DBConnection is not None:
            DBConnection.close()

@app.route("/infoRutas", methods=["GET"])
def informacionRutas():
    return app.send_static_file("busquedaRutas.html")

@app.route("/resultadoRutas",methods=["POST","GET"])
def busquedaRutas():
    if request.method == "POST":
        origen = request.values.get("Ciudad_origen")
        destino = request.values.get("Ciudad_destino")
        return "<h1>" + "Vamos de " + origen + " a" + destino + "</h1>"

app.run()
