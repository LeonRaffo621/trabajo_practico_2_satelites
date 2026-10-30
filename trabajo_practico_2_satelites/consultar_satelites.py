import sys
from catalogo import leer_json, crear_catalogo, resumen_por_orbita, obtener_satelites_en_zona

def resumen(satelites):
    resumen = resumen_por_orbita(satelites)
    for tipo, datos in resumen.items():
        print(f"\ntipo de órbita: {tipo}")
        print(f"cantidad de satélites: {datos['cantidad']}")
        if datos["cantidad"] > 0:
            print(f"altitud mínima: {datos['minimo']} km")
            print(f"altitud máxima: {datos['maximo']} km")
            print(f"altitud promedio: {datos['promedio']} km")
        else:
            print("no hay datos disponibles para esta órbita.")

def zona(satelites, args):
    if len(args) != 4:
        print("error: La consulta 'zona' requiere 4 coordenadas.")
        return
    try:
        lon_min = float(args[0])
        lat_min = float(args[1])
        lon_max = float(args[2])
        lat_max = float(args[3])
    except ValueError:
        print("Error: Las coordenadas de la zona deben ser números decimales.")
        return

    if lon_min > lon_max or lat_min > lat_max:
        print("error: verifique el orden de los límites (mínimos deben ser menores o iguales a los máximos).")
        return

    satelites_zona = obtener_satelites_en_zona(satelites, lon_min, lat_min, lon_max, lat_max)

    print(f"Satélites encontrados en la zona especificada: {len(satelites_zona)}")
    for sat in satelites_zona:
        print(sat.cadena())


def main():
    if len(sys.argv) < 3:
        print("Error: Argumentos insuficientes.")
        return

    ruta_json = sys.argv[1]
    consulta = sys.argv[2]

    try:
        registros = leer_json(ruta_json)
        satelites = crear_catalogo(registros)
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo en la ruta '{ruta_json}'.")
        return

    if consulta == "resumen":
        resumen(satelites)
    elif consulta == "zona":
        coordenadas_args = sys.argv[3:]
        zona(satelites, coordenadas_args)
    else:
        print(f"Error: Consulta '{consulta}' no reconocida.")
        return


if __name__ == "__main__":
    main()
