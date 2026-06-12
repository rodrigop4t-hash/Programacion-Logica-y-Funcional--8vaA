#!/usr/bin/env python3
"""
================================================================
  DEMO AUTOMATIZADO - SISTEMA co
================================================================

DESCRIPCION
-----------
  Ejecuta el sistema experto sobre 4 perfiles de estudiantes
  preconstruidos y muestra el ranking de carreras recomendadas
  para cada uno. No requiere entrada del usuario.
EXPERTO ORIENTACION VOCACIONAL
  Instituto Tecnologico de Felipe Carrillo Puerto
  Tecnologico Nacional de Mexi
REQUISITOS
----------
  - Python 3.9 o superior
  - SWI-Prolog instalado y en el PATH
  - Los archivos base_conocimientos.pl y sistema_experto.py
    deben estar en el MISMO directorio que este script.

EJECUCION
----------
  python3 demo_perfiles.py

  Para el cuestionario interactivo completo:
  python3 sistema_experto.py

PERFILES INCLUIDOS EN EL DEMO
-------------------------------
  1. Ana Garcia    -> STEM / Tecnologia
  2. Carlos Mendoza -> Liderazgo / Negocios
  3. Maria Lopez   -> Ciencias / Investigacion
  4. Jose Ruiz     -> Social / Comunitario

================================================================
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from sistema_experto import (
    PerfilUsuario, consultar_top_carreras, calcular_estadisticas,
    formatear_nombre_carrera, formatear_barra, EMOJIS_CARRERA,
    COLORES_NIVEL, RESET, BOLD, CYAN, MAGENTA, YELLOW, BLUE,
    obtener_explicacion
)
from functools import reduce

# ─────────────────────────────────────────────────────────────
#  PERFILES DE EJEMPLO (estructuras inmutables)
# ─────────────────────────────────────────────────────────────

PERFILES_DEMO = (
    (
        "Ana Garcia",
        "Perfil: Tecnologia / STEM fuerte",
        PerfilUsuario(
            rasgos      = frozenset(["analitico", "logico", "detallista", "creativo"]),
            habilidades = frozenset(["programacion", "matematicas",
                                     "resolucion_problemas", "pensamiento_abstracto"]),
            intereses   = frozenset(["tecnologia", "automatizacion",
                                     "ciencias_exactas", "videojuegos_software"]),
        )
    ),
    (
        "Carlos Mendoza",
        "Perfil: Liderazgo / Negocios",
        PerfilUsuario(
            rasgos      = frozenset(["lider", "estrategico", "comunicativo", "organizador"]),
            habilidades = frozenset(["liderazgo", "toma_decisiones",
                                     "comunicacion", "gestion_recursos"]),
            intereses   = frozenset(["negocios", "liderazgo_organizacional",
                                     "finanzas", "economia"]),
        )
    ),
    (
        "Maria Lopez",
        "Perfil: Ciencias / Investigacion",
        PerfilUsuario(
            rasgos      = frozenset(["investigador", "detallista", "analitico", "practico"]),
            habilidades = frozenset(["ciencias_naturales", "investigacion",
                                     "matematicas", "resolucion_problemas"]),
            intereses   = frozenset(["salud_nutricion", "ciencias_naturales",
                                     "investigacion_cientifica", "manufactura"]),
        )
    ),
    (
        "Jose Ruiz",
        "Perfil: Social / Comunitario",
        PerfilUsuario(
            rasgos      = frozenset(["empatico", "comunicativo", "lider", "creativo"]),
            habilidades = frozenset(["comunicacion", "liderazgo",
                                     "investigacion", "gestion_recursos"]),
            intereses   = frozenset(["trabajo_social", "medio_ambiente",
                                     "cultura_arte", "liderazgo_organizacional"]),
        )
    ),
)


# ─────────────────────────────────────────────────────────────
#  FUNCIONES DE DISPLAY (funcionales - sin side effects globales)
# ─────────────────────────────────────────────────────────────

def separador(char: str = "=", ancho: int = 62) -> str:
    return char * ancho

def imprimir_encabezado_demo():
    print(f"\n{CYAN}{separador()}{RESET}")
    print(f"{BOLD}{CYAN}   DEMO: SISTEMA EXPERTO ORIENTACION VOCACIONAL{RESET}")
    print(f"{CYAN}   Instituto Tecnologico de Felipe Carrillo Puerto{RESET}")
    print(f"{CYAN}   Tecnologico Nacional de Mexico{RESET}")
    print(f"{CYAN}{separador()}{RESET}")
    print(f"  {YELLOW}Motor Logico:{RESET}      Prolog (SWI-Prolog)")
    print(f"  {YELLOW}Controlador:{RESET}       Python - Paradigma Funcional")
    print(f"  {YELLOW}Paradigmas:{RESET}        map | filter | NamedTuple | frozenset")
    print(f"  {YELLOW}Carreras en BD:{RESET}    7 opciones del TecNM")
    print(f"{CYAN}{separador()}{RESET}\n")

def mostrar_perfil_demo(nombre: str, descripcion: str, perfil: PerfilUsuario):
    """Muestra el perfil de un estudiante demo."""
    def fmt_set(s):
        return ", ".join(sorted(s)).replace("_", " ")

    print(f"\n{MAGENTA}{separador('-')}{RESET}")
    print(f"{BOLD}{MAGENTA}  Estudiante: {nombre}{RESET}")
    print(f"  {YELLOW}{descripcion}{RESET}")
    print(f"{MAGENTA}{separador('-')}{RESET}")
    print(f"  {BLUE}Rasgos:{RESET}      {fmt_set(perfil.rasgos)}")
    print(f"  {BLUE}Habilidades:{RESET} {fmt_set(perfil.habilidades)}")
    print(f"  {BLUE}Intereses:{RESET}   {fmt_set(perfil.intereses)}")

def mostrar_ranking_demo(resultados: list, top_n: int = 4):
    """Muestra el ranking de carreras para un perfil."""
    print(f"\n  {BOLD}Ranking de compatibilidad (motor Prolog):{RESET}\n")

    # map: transformar resultado en linea formateada
    def formatear(par):
        pos, r = par
        carrera = r["carrera"]
        puntaje = r["puntaje"]
        nivel   = r["nivel"]
        nombre  = formatear_nombre_carrera(carrera)
        emoji   = EMOJIS_CARRERA.get(carrera, "🎓")
        barra   = formatear_barra(puntaje, 25)
        color   = COLORES_NIVEL.get(nivel, "")
        medalla = {0: "🥇", 1: "🥈", 2: "🥉"}.get(pos, f"  {pos+1}.")
        return (
            f"  {medalla} {emoji} {BOLD}{nombre}{RESET}\n"
            f"     {color}{barra}{RESET} {puntaje:.1f}%  [{color}{nivel.upper()}{RESET}]"
        )

    top = resultados[:top_n]
    lineas = list(map(formatear, enumerate(top)))
    for linea in lineas:
        print(linea)
        print()

    # Estadisticas con reduce
    puntajes = list(map(lambda r: r["puntaje"], resultados))
    promedio = reduce(lambda a, b: a + b, puntajes) / len(puntajes)
    alta  = len(list(filter(lambda r: r["nivel"] == "alta",  resultados)))
    media = len(list(filter(lambda r: r["nivel"] == "media", resultados)))

    print(f"  {YELLOW}Promedio general:{RESET} {promedio:.1f}%  "
          f"| Alta: {alta}  Media: {media}  "
          f"Baja: {len(resultados)-alta-media}")


def ejecutar_demo():
    imprimir_encabezado_demo()
    print(f"  Ejecutando inferencia Prolog para {len(PERFILES_DEMO)} perfiles...\n")

    # map sobre todos los perfiles demo
    def procesar_perfil(datos):
        nombre, desc, perfil = datos
        mostrar_perfil_demo(nombre, desc, perfil)
        resultados = consultar_top_carreras(perfil)
        if resultados:
            mostrar_ranking_demo(resultados)
            # Explicacion de la carrera top
            top = resultados[0]
            exp = obtener_explicacion(top["carrera"], perfil)
            if exp and not exp.startswith("ERROR"):
                partes = {k: v for item in exp.split(" | ")
                          if ": " in item
                          for k, v in [item.split(": ", 1)]}
                print(f"  {BOLD}Analisis Prolog:{RESET}")
                for k, v in partes.items():
                    if k != "Carrera":
                        print(f"    • {k}: {v}")
        else:
            print(f"  {YELLOW}No se pudo obtener resultado del motor.{RESET}")
        return nombre, resultados

    todos = list(map(procesar_perfil, PERFILES_DEMO))

    # Resumen final con filter y map
    print(f"\n{CYAN}{separador()}{RESET}")
    print(f"{BOLD}{CYAN}  RESUMEN EJECUTIVO{RESET}")
    print(f"{CYAN}{separador()}{RESET}\n")

    recomendaciones_top = list(map(
        lambda par: (par[0], formatear_nombre_carrera(par[1][0]["carrera"]),
                     par[1][0]["puntaje"]) if par[1] else (par[0], "N/A", 0),
        todos
    ))

    for nombre, carrera, puntaje in recomendaciones_top:
        print(f"  {BOLD}{nombre:<20}{RESET}  {EMOJIS_CARRERA.get(next((k for k,v in __import__('sistema_experto').NOMBRES_CARRERAS.items() if v == carrera), ''), '🎓')}  "
              f"{carrera}  ({puntaje:.1f}%)")

    print(f"\n{CYAN}{separador()}{RESET}")
    print(f"\n  {YELLOW}Fin del demo. Para modo interactivo: python3 sistema_experto.py{RESET}\n")


if __name__ == "__main__":
    ejecutar_demo()

