import pandas
import networkx as nx
import matplotlib.pyplot as plt

def maximizacion(tipo):
    if tipo == 0:
        objetivo = "duracion(min)"
    elif tipo == 1:
        objetivo = "monto_vip"
    elif tipo == 2:
        objetivo = "monto_economico"
    else:
        objetivo = "monto_ejecutivo"

    for index,row in rutas.iterrows():
        origen = row["origen_id"]
        destino = row["destino_id"]
        peso = row[objetivo]
        G.add_edge(origen,destino,weight = peso)
        G.add_edge(destino,origen,weight = peso)

rutas = pandas.read_csv('rutas2.csv', sep=';', encoding='latin1').fillna('-')
G = nx.DiGraph()
maximizacion(2)
trayecto = nx.shortest_path(G, source=1, target = 5)
print(trayecto)

for i in range(len(trayecto)-1):
    print("Tiene que ir de",trayecto[i],"a",trayecto[i+1])
print("De puta madre")
nx.draw_random(G, with_labels = True)
print("Puta vida :v")

plt.show()

# Cualquiera de los temas de la clase
# 4 paginas 2 hojas maximo
# es un ensayo
# mi correo es andrese.cruz@urosario.edu.co
# al 19 de mayo
# No solo un resña sino que tienen que dar su opinion
