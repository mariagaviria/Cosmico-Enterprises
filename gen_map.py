import folium, json, os, pandas

m = folium.Map(location=[48.864716, 2.349014], zoom_start=5)
estaciones = pandas.read_csv("main_stations.csv", sep=";", encoding="latin1").fillna("-")
rutas = pandas.read_csv("routes.csv", sep=";", encoding="latin1").fillna("-")
list = []

"""
¡El orden es súper importante!
"""

faro_porto = os.path.join("data","faro_porto.json")
list.append(faro_porto)
porto_braga = os.path.join("data","porto-braga.json")
list.append(porto_braga)
porto_guimaraes = os.path.join("data","porto-guimaraes.json")
list.append(porto_guimaraes)
cadiz_leon = os.path.join("data","cadiz-leon.json")
list.append(cadiz_leon)
coruña_leon = os.path.join("data","coruña-leon.json")
list.append(coruña_leon)
madrid_castellon = os.path.join("data","madrid-castello.json")
list.append(madrid_castellon)
coimbra_bayonne = os.path.join("data","coimbra-bayonne.json")
list.append(coimbra_bayonne)
madrid_avignon = os.path.join("data","madrid-avignon.json")
list.append(madrid_avignon)
vigo_santiago = os.path.join("data","vigo-santiago.json")
list.append(vigo_santiago)
gijon_leon = os.path.join("data","gijon-leon.json")
list.append(gijon_leon)
santander_leon = os.path.join("data","santander-leon.json")
list.append(santander_leon)
bilbao_burgos = os.path.join("data","bilbao-burgos.json")
list.append(bilbao_burgos)
badajoz_madrid = os.path.join("data","badajoz-madrid.json")
list.append(badajoz_madrid)
cordoba_malaga = os.path.join("data","cordoba-malaga.json")
list.append(cordoba_malaga)
cordoba_almeria = os.path.join("data","cordoba-almeria.json")
list.append(cordoba_almeria)
albacete_murcia = os.path.join("data","albacete-murcia.json")
list.append(albacete_murcia)
albacete_alicante = os.path.join("data","albacete-alicante.json")
list.append(albacete_alicante)
avignon_lille = os.path.join("data","avignon-lille.json")
list.append(avignon_lille)
bayonne_beziers = os.path.join("data","bayonne-beziers.json")
list.append(bayonne_beziers)
brest_paris = os.path.join("data","brest-paris.json")
list.append(brest_paris)
leHavre_paris = os.path.join("data","le_havre-paris.json")
list.append(leHavre_paris)
lille_london = os.path.join("data","lille-london.json")
list.append(lille_london)
paris_liege = os.path.join("data","paris-liege.json")
list.append(paris_liege)
paris_heidelberg = os.path.join("data","paris-heidelberg.json")
list.append(paris_heidelberg)
lyon_zurich = os.path.join("data","lyon-zurich.json")
list.append(lyon_zurich)
avignon_torino = os.path.join("data","avignon-torino.json")
list.append(avignon_torino)
bayonne_limoges = os.path.join("data","bayonne-limoges.json")
list.append(bayonne_limoges)
valence_grenoble = os.path.join("data","valence-grenoble.json")
list.append(valence_grenoble)
stEtienne_lyon = os.path.join("data","stEtienne-lyon.json")
list.append(stEtienne_lyon)
besancon_mulhouse = os.path.join("data","besancon-mulhouse.json")
list.append(besancon_mulhouse)
nantes_tours = os.path.join("data","nantes-tours.json")
list.append(nantes_tours)
caen_rouen = os.path.join("data","caen-rouen.json")
list.append(caen_rouen)
paris_charleville = os.path.join("data","paris-charleville.json")
list.append(paris_charleville)
lille_brussel = os.path.join("data","lille-brussel.json")
list.append(lille_brussel)
metz_nancy = os.path.join("data","metz-nancy.json")
list.append(metz_nancy)
metz_saarsbrucken = os.path.join("data","metz-saarsbrucken.json")
list.append(metz_saarsbrucken)
basel_bern = os.path.join("data","basel-bern.json")
list.append(basel_bern)
zurich_milano = os.path.join("data","zurich-milano.json")
list.append(zurich_milano)
glasgow_london = os.path.join("data","glasgow-london.json")
list.append(glasgow_london)
swansea_birminghan = os.path.join("data","swansea-birminghan.json")
list.append(swansea_birminghan)
liverpool_manchester = os.path.join("data","liverpool-manchester.json")
list.append(liverpool_manchester)
brindisi_milano = os.path.join("data","brindisi-milano.json")
list.append(brindisi_milano)
ancona_foggia = os.path.join("data","ancona-foggia.json")
list.append(ancona_foggia)
firenze_trieste = os.path.join("data","firenze-trieste.json")
list.append(firenze_trieste)
milano_bolzano = os.path.join("data","milano-bolzano.json")
list.append(milano_bolzano)
lugano_milano = os.path.join("data","lugano-milano.json")
list.append(lugano_milano)
verona_padova = os.path.join("data","verona-padova.json")
list.append(verona_padova)
roma_pescara = os.path.join("data","roma-pescara.json")
list.append(roma_pescara)
napoli_salerno = os.path.join("data","napoli-salerno.json")
list.append(napoli_salerno)
bari_taranto = os.path.join("data","bari-taranto.json")
list.append(bari_taranto)
pisa_livorno = os.path.join("data","pisa-livorno.json")
list.append(pisa_livorno)
oostende_rotterdam = os.path.join("data","oostende-rotterdam.json")
list.append(oostende_rotterdam)
amsterdam_bremen = os.path.join("data","amsterdam-bremen.json")
list.append(amsterdam_bremen)
brussel_antwerpen = os.path.join("data","brussel-antwerpen.json")
list.append(brussel_antwerpen)
liege_endhoven = os.path.join("data","liege-endhoven.json")
list.append(liege_endhoven)
rostock_munchen = os.path.join("data","rostock-munchen.json")
list.append(rostock_munchen)
heidelberg_kiel = os.path.join("data","heidelberg-kiel.json")
list.append(heidelberg_kiel)
luxemburgo_munchen = os.path.join("data","luxemburgo-munchen.json")
list.append(luxemburgo_munchen)
osnabruck_potsdam = os.path.join("data","osnabruck-potsdam.json")
list.append(osnabruck_potsdam)
leipzig_zwickau = os.path.join("data","leipzig-zwickau.json")
list.append(leipzig_zwickau)
berlin_cottbus = os.path.join("data","berlin-cottbus.json")
list.append(berlin_cottbus)
braunschweig_rostock = os.path.join("data","braunschweig-rostock.json")
list.append(braunschweig_rostock)
duisburg_bebra = os.path.join("data","duisburg-bebra.json")
list.append(duisburg_bebra)
frankfurt_fulda = os.path.join("data","frankfurt-fulda.json")
list.append(frankfurt_fulda)

for (index, row) in rutas.iterrows():
    geo = folium.GeoJson(list[int(index)], tooltip="<strong>Ruta "+ row["name"] +"</strong>")
    popup = folium.Popup(row["route"])
    popup.add_to(geo)
    geo.add_to(m)

for (index, row) in estaciones.iterrows():
    folium.Marker([row['latitude'],row['longitude']], popup="<strong>"+row.loc['name']+"<\strong>",tooltip='Click para más información').add_to(m)

m.save("map.html")
