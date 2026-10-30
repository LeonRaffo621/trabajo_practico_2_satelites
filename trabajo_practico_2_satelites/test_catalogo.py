import pytest
from satelites import Satelite
import catalogo

def test_resumen_por_orbita():
    sat1 = Satelite("Satelite A", 10001, 10.0, -20.0, 500.0)
    sat2 = Satelite("Satelite B", 10002, 15.0, -25.0, 1500.0)
    sat3 = Satelite("Satelite C", 10003, 0.0, 45.0, 10000.0)
    lista_satelites = [sat1, sat2, sat3]
    
    resultado = catalogo.resumen_por_orbita(lista_satelites)
    assert resultado["LEO"]["cantidad"] == 2
    assert resultado["LEO"]["minimo"] == 500.0
    assert resultado["LEO"]["maximo"] == 1500.0
    assert resultado["LEO"]["promedio"] == 1000.0
    
    assert resultado["MEO"]["cantidad"] == 1
    assert resultado["MEO"]["minimo"] == 10000.0
    assert resultado["MEO"]["maximo"] == 10000.0
    assert resultado["MEO"]["promedio"] == 10000.0


def test_obtener_satelites_en_zona():

    sat_dentro = Satelite("En Zona", 20001, -25.0, -60.0, 400.0)
    sat_fuera = Satelite("Fuera Zona", 20002, 50.0, 10.0, 400.0)
    lista_satelites = [sat_dentro, sat_fuera]
    lon_min, lat_min = -70.0, -40.0
    lon_max, lat_max = -50.0, -10.0
    resultado = catalogo.obtener_satelites_en_zona(lista_satelites, lon_min, lat_min, lon_max, lat_max)
    assert len(resultado) == 1
    assert resultado[0].nombre == "En Zona"


def test_crear_catalogo_con_registros_vacios():
    registros_vacios = []
    resultado = catalogo.crear_catalogo(registros_vacios)
    assert resultado == []


def test_leer_json_archivo_no_encontrado():
    with pytest.raises(FileNotFoundError):
        catalogo.leer_json("este_archivo_no_existe.json")