import json
import folium

from colorama import Fore, Style, init

with open("anuncios.json", "rb") as f:
    anuncios = json.load(f)

pos = 0

lista_terreno = []
lista_industrial = []
lista_galpao = []

lista_terreno_area1 = []
lista_terreno_area2 = []
lista_terreno_area3 = []
lista_terreno_area4 = []

area1 = 0
area2 = 0
area3 = 0
area4 = 0
area5 = 0
area6 = 0
area7 = 0

valor1 = 0
valor2 = 0
valor3 = 0
valor4 = 0
valor5 = 0
valor6 = 0
valor7 = 0

#Pegando um modelo de dado
for x in anuncios:
    #Tipo imovel
    try:
        if x['tipo_imovel'][0] == "Terreno":
            lista_terreno.append(pos)
        if x['tipo_imovel'][0] == "Galpão":
            lista_galpao.append(pos)
        if x['tipo_imovel'][0] == "Industrial":
            lista_industrial.append(pos)
    except:
        pass  
    pos = pos + 1


for x in lista_terreno:
    #Dadaos area util
    try:
        area_util = anuncios[x]['area_util']
        if area_util < 500:
            area1 += 1
        if 501 < area_util < 1000:
            area2 += 1
            lista_terreno_area1.append([anuncios[x]['latitude'], anuncios[x]['longitude']])
        if 1001 < area_util < 3000:
            area3 += 1
            lista_terreno_area2.append([anuncios[x]['latitude'], anuncios[x]['longitude']])
        if 3001 < area_util < 5000:
            area4 += 1
            lista_terreno_area3.append([anuncios[x]['latitude'], anuncios[x]['longitude']])
        if 5001 < area_util < 10000:
            area5 += 1
            lista_terreno_area4.append([anuncios[x]['latitude'], anuncios[x]['longitude']])
        if 10001 < area_util < 50000:
            area6 += 1
        if area_util > 50001:
            area7 += 1
    except:
        pass
    
    #Dados valores
    try:
        preco = anuncios[x]['valor']
        if preco < 50000:
            valor1 += 1
        if 50001 < preco < 100000:
            valor2 += 1
        if 100001 < preco < 200000:
            valor3 += 1
        if 200001 < preco < 350000:
            valor4 += 1
        if 350001 < preco < 550000:
            valor5 += 1
        if 550001 < preco < 1000000:
            valor6 += 1
        if preco > 1000001:
            valor7 += 1
    except:
        pass
    


print(f"""
INFORMAÇÕES TERRENOS
------------------------------------------------------------------------------
Areas uteis em m2...
0-500: {area1}
500-1000: {area2}
1000-3000: {area3}
3000-5000: {area4}
5000-10000: {area5}
10000-50000: {area6}
50000+: {area7}

Valores
0-50000: {valor1}
50000-100000: {valor2}
100000-200000: {valor3}
200000-350000: {valor4}
350000-500000: {valor5}
550000-1000000: {valor6}
1000000+: {valor7}
------------------------------------------------------------------------------

""")
mapAll = folium.Map(location=[-23.419271802075343, -51.929348288041204], zoom_start=13)

laMap = folium.Map(location=[-23.419271802075343, -51.929348288041204], zoom_start=13)
for x in lista_terreno_area1:
    folium.CircleMarker((x[0], x[1]), radius=3, weight=2, color='blue', fill_color='blue', fill_opacity=1).add_to(mapAll)
    folium.CircleMarker((x[0], x[1]), radius=3, weight=2, color='blue', fill_color='blue', fill_opacity=1).add_to(laMap)
laMap.save('terrenos-500-1000.html')

laMap = folium.Map(location=[-23.419271802075343, -51.929348288041204], zoom_start=13)
for x in lista_terreno_area2:
    folium.CircleMarker((x[0], x[1]), radius=3, weight=2, color='blue', fill_color='blue', fill_opacity=1).add_to(mapAll)
    folium.CircleMarker((x[0], x[1]), radius=3, weight=2, color='blue', fill_color='blue', fill_opacity=1).add_to(laMap)
laMap.save('terrenos-1000-3000.html')

laMap = folium.Map(location=[-23.419271802075343, -51.929348288041204], zoom_start=13)
for x in lista_terreno_area3:
    folium.CircleMarker((x[0], x[1]), radius=3, weight=2, color='blue', fill_color='blue', fill_opacity=1).add_to(mapAll)
    folium.CircleMarker((x[0], x[1]), radius=3, weight=2, color='blue', fill_color='blue', fill_opacity=1).add_to(laMap)
laMap.save('terrenos-3000-5000.html')

laMap = folium.Map(location=[-23.419271802075343, -51.929348288041204], zoom_start=13)
for x in lista_terreno_area4:
    folium.CircleMarker((x[0], x[1]), radius=3, weight=2, color='blue', fill_color='blue', fill_opacity=1).add_to(mapAll)
    folium.CircleMarker((x[0], x[1]), radius=3, weight=2, color='blue', fill_color='blue', fill_opacity=1).add_to(laMap)
laMap.save('terrenos-5000-10000.html')

mapAll.save('todos-terrenos.html')

print("MAPAS GERADOS")

print(lista_terreno_area1)
print("")
print(lista_terreno_area2)
print("")
print(lista_terreno_area3)
print("")
print(lista_terreno_area4)
