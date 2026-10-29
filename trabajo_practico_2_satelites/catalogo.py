import json
from funciones_bases import obtener_posicion
from satelites import Satelite

def leer_json():
    with open("trabajo_practico_2_satelites/datos/satelites.json", "r", encoding="utf-8") as archivo:
        return json.load(archivo)

def crear_catalogo(registros):

    lista_satelites = []
    for reg in registros:
        try:
            nombre = reg.get("OBJECT_NAME")
            num_catalogo = reg.get("NORAD_CAT_ID")
            latitud, longitud, altitud = obtener_posicion(reg)
            satelite = Satelite(nombre, num_catalogo, latitud, longitud, altitud)
            lista_satelites.append(satelite)
        except Exception:
            continue 
    return lista_satelites

def resumir_satelites(satelites):
    sumas_altitud = {}
    resumen = {}

    for s in satelites:
        tipo = s.obtener_tipo_orbita()
        alt = s.altitud

        if tipo not in resumen:
            resumen[tipo] = {"cantidad": 0, "minimo": alt, "maximo": alt}
            sumas_altitud[tipo] = 0.0

        resumen[tipo]["cantidad"] += 1
        sumas_altitud[tipo] += alt

        if alt < resumen[tipo]["minimo"]:
            resumen[tipo]["minimo"] = alt
        if alt > resumen[tipo]["maximo"]:
            resumen[tipo]["maximo"] = alt

    for tipo in resumen:
        cantidad = resumen[tipo]["cantidad"]
        resumen[tipo]["promedio"] = sumas_altitud[tipo] / cantidad, 2

    return resumen

def obtener_satelites_en_zona(satelites, lon_min, lat_min, lon_max, lat_max):
    satelites_filtrados = []
    for s in satelites:
        if s.limite(lon_min, lat_min, lon_max, lat_max):
            satelites_filtrados.append(s)
    return satelites_filtrados
