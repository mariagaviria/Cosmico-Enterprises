import pandas
import networkx as nx 
import matplotlib.pyplot as plt


rutas = pandas.read_csv("rutas.csv", sep=";", encoding="latin1").fillna("-")

G = nx.DiGraph()

for index,row in rutas.iterrows():
    origen = row["origen_id"]
    destino = row["destino_id"]
    peso = row["duracion"]
    G.add_edge(origen,destino,weight = peso)
    G.add_edge(destino,origen,weight = peso)

trayecto = nx.shortest_path(G, source=1, target = 6)
print(trayecto)

for i in range(len(trayecto)-1):
    print("Tiene que ir de",trayecto[i],"a",trayecto[i+1])

nx.draw(G, with_labels = True)
plt.show()