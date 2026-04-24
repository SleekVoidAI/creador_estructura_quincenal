######
# CREADOR DE ESTRUCTURA QUINCENAL
# Objetivo: Crear una carpeta padre organizada por año y quincena, junto con seis subcarpetas internas configurables.
# Fecha modificacion: 24/04/2026
# Autor: Jorge Fernando Ortiz Bravo
######


from __future__ import annotations
from datetime import datetime
from typing import Optional
from pathlib import Path
from dataclasses import dataclass


######
# LISTAS
######

SUBCARPETAS = [
    "Subcarpeta 1",
    "Subcarpeta 2",
    "Subcarpeta 3",
    "Subcarpeta 4",
    "Subcarpeta 5",
    "Subcarpeta 6"
]


######
# CLASES
######

# Calcula la quincena en curso
class Quincena:

    def __init__(self, fecha: Optional[datetime] = None):
        self.fecha = fecha or datetime.today()

    def obtener_quincena(self) -> str:
        dd = self.fecha.day
        mm = self.fecha.month

        base = (mm - 1) * 2
        quincena_num = base + (1 if dd < 16 else 2)

        return f"{quincena_num:02d}"


# Genera una estructura de carpetas basada en año y quincena, incluyendo subcarpetas configurables dentro de un directorio base
@dataclass
class EstructuraCarpetas:

    base_dir: Path
    prefijo: str = "Q" #nombre de carpetas
    subcarpetas: list[str] = None

    def __post_init__(self):
        if self.subcarpetas is None:
            self.subcarpetas = SUBCARPETAS

    def crear(self, anio: int, quincena: str) -> Path:

        carpeta_padre = self.base_dir / f"{self.prefijo}_{anio}_{quincena}"
        carpeta_padre.mkdir(parents=True, exist_ok=True)

        for nombre in self.subcarpetas:
            (carpeta_padre / nombre).mkdir(parents=True, exist_ok=True)

        return carpeta_padre


######
# CONFIGURACIÓN
######

salida = Path(r"C:\Users\Usuario\Documents")
anio = datetime.today().year


######
# EJECUCIÓN
######

estructura = EstructuraCarpetas(base_dir=salida)

carpeta_padre = estructura.crear(
    anio=anio,
    quincena=Quincena().obtener_quincena()
)

print("Carpeta creada en:", carpeta_padre)