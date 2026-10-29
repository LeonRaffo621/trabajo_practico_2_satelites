class Satelite:
    def __init__(self,nombre,n_catalogo,latitud,longitud,altitud):
        if nombre==(""):
            raise ValueError("El nombre no debe estar vacío.")
        self.nombre=nombre
        if type(n_catalogo)!=int:
            raise ValueError("El número de catálogo debe ser un entero.")
        self.n_catalogo=n_catalogo
        if not -90<=latitud<=90:
            raise ValueError("La latitud debe estar entre -90 y 90.")
        self.latitud=latitud
        if not -180<=longitud<=180:
            raise ValueError("La longitud debe estar entre -180 y 180.")
        self.longitud=longitud
        if not altitud>=100:
            raise ValueError("La altitud debe ser de al menos 100 km.")
        self.altitud=altitud

    def t_orbita(self):
        if self.altitud<2000:
            return("LEO")
        elif 2000<=self.altitud<34000:
            return("MEO")
        elif 34000<=self.altitud<=37000:
            return("GEO")
        elif 37000<self.altitud:
            return("HEO")

    def cadena(self):
        return(f"{self.nombre} | {self.n_catalogo} | {self.t_orbita()} | {self.altitud}KM")

    def limite(self,lon_min,lat_min,lon_max,lat_max):
        if lon_min<=self.longitud<=lon_max:
            if lat_min<=self.latitud<=lat_max:
                return True
            else:
                return False
        else:
            return False
