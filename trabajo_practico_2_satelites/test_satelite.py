import pytest
from satelites import Satelite

def test_satelite_creacion_exitosa():
    sat = Satelite("NOAA 19", 33591, -40.0, 120.0, 850.0)
    assert sat.nombre == "NOAA 19"
    assert sat.n_catalogo == 33591
    assert sat.latitud == -40.0
    assert sat.longitud == 120.0
    assert sat.altitud == 850.0

def test_satelite_nombre_vacio():
    with pytest.raises(ValueError, match="El nombre no debe estar vacío."):
        Satelite("", 12345, 0, 0, 500)

def test_satelite_catalogo_no_entero():
    with pytest.raises(ValueError, match="El número de catálogo debe ser un entero."):
        Satelite("Satelite Test", "no_soy_entero", 0, 0, 500)

def test_satelite_latitud_fuera_rango():
    with pytest.raises(ValueError, match="La latitud debe estar entre -90 y 90."):
        Satelite("Test", 12345, -90.1, 0, 500)
    with pytest.raises(ValueError, match="La latitud debe estar entre -90 y 90."):
        Satelite("Test", 12345, 90.1, 0, 500)

def test_satelite_longitud_fuera_rango():
    with pytest.raises(ValueError, match="La longitud debe estar entre -180 y 180."):
        Satelite("Test", 12345, 0, -180.1, 500)
    with pytest.raises(ValueError, match="La longitud debe estar entre -180 y 180."):
        Satelite("Test", 12345, 0, 180.1, 500)

def test_satelite_altitud_insuficiente():
    with pytest.raises(ValueError, match="La altitud debe ser de al menos 100 km."):
        Satelite("Test", 12345, 0, 0, 99.9)

def test_satelite_tipos_de_orbita():
    sat_leo = Satelite("LEO_Sat", 1, 0, 0, 500)
    assert sat_leo.t_orbita() == "LEO"

    sat_meo = Satelite("MEO_Sat", 2, 0, 0, 10000)
    assert sat_meo.t_orbita() == "MEO"

    sat_geo = Satelite("GEO_Sat", 3, 0, 0, 35000)
    assert sat_geo.t_orbita() == "GEO"

    sat_heo = Satelite("HEO_Sat", 4, 0, 0, 40000)
    assert sat_heo.t_orbita() == "HEO"

def test_satelite_cadena():
    sat = Satelite("ISS", 25544, 51.6, -10.5, 420)
    assert sat.cadena() == "ISS | 25544 | LEO | 420KM"

def test_satelite_limite_geografico():
    sat = Satelite("Zonable", 99999, -20.0, -60.0, 300)
    assert sat.limite(-70, -30, -50, -10) is True
    
    assert sat.limite(-50, -30, -40, -10) is False
    
    assert sat.limite(-70, 0, -50, 10) is False