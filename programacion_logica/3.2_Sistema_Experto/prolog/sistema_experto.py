#!/usr/bin/env python3
"""
================================================================
  SISTEMA EXPERTO - ORIENTACION VOCACIONAL
  Instituto Tecnologico de Felipe Carrillo Puerto
  Tecnologico Nacional de Mexico
================================================================
  Paradigma Logico   : Prolog  (motor de inferencia)
  Paradigma Funcional: Python  (controlador - map, filter,
                                inmutabilidad, NamedTuple)
================================================================

REQUISITOS PREVIOS
------------------
  Sistema operativo : Linux / macOS / Windows (WSL recomendado)
  Python            : 3.9 o superior
  SWI-Prolog        : 8.x o superior

INSTALACION DE DEPENDENCIAS
-----------------------------
  Ubuntu / Debian:
      sudo apt update && sudo apt install -y swi-prolog

  macOS (Homebrew):
      brew install swi-prolog

  Windows:
      Descargar instalador desde https://www.swi-prolog.org/download/stable
      Asegurarse de agregar 'swipl' al PATH del sistema.

  Verificar instalacion de Prolog:
      swipl --version

ESTRUCTURA DEL PROYECTO
-------------------------
  sistema_experto/
  |-- base_conocimientos.pl   <- Base de hechos y reglas Prolog
  |-- sistema_experto.py      <- Controlador Python (este archivo)
  |-- demo_perfiles.py        <- Demo automatico con perfiles de ejemplo

  IMPORTANTE: Los tres archivos deben estar en el MISMO directorio.

EJECUCION
----------
  Modo interactivo (cuestionario completo para un estudiante):
      python3 sistema_experto.py

  Demo automatico (4 perfiles preconstruidos, sin entrada del usuario):
      python3 demo_perfiles.py

  Consulta directa al motor Prolog (desde terminal):
      swipl -q -s base_conocimientos.pl -g "
        recomendar_carrera([analitico,logico],[programacion,matematicas],
          [tecnologia,ciencias_exactas],Carrera,Puntaje),
        format('~w: ~2f%~n',[Carrera,Puntaje]),halt"

FLUJO DEL SISTEMA
------------------
  1. Python muestra el cuestionario (9 preguntas en 3 categorias).
  2. Las respuestas se transforman en terminos Prolog (frozenset).
  3. Python invoca SWI-Prolog via subprocess con la base de conocimientos.
  4. Prolog aplica reglas de inferencia y devuelve el ranking ponderado.
  5. Python formatea y presenta los resultados al usuario.

PONDERACION DEL MOTOR DE INFERENCIA
--------------------------------------
  Perfil personal : 30%   |  Habilidades : 40%   |  Intereses : 30%
  Niveles: ALTA >= 70%  /  MEDIA >= 40%  /  BAJA < 40%

CARRERAS DISPONIBLES (7)
--------------------------
  1. Ingenieria en Sistemas Computacionales
  2. Licenciatura en Ciencia de Datos
  3. Licenciatura en Administracion
  4. Ingenieria Industrial
  5. Ingenieria en Industrias Alimentarias
  6. Licenciatura en Desarrollo Comunitario
  7. Licenciatura en Gestion Empresarial

ERRORES FRECUENTES
--------------------
  "ERROR: SWI-Prolog no encontrado"
      -> Instalar SWI-Prolog y verificar que 'swipl' este en el PATH.

  "No se pudo obtener resultado del motor"
      -> Verificar que base_conocimientos.pl este en el mismo directorio.

  Timeout en consulta Prolog
      -> Comprobar sintaxis con: swipl -q -t halt -f base_conocimientos.pl

================================================================
"""

import subprocess
import os
import sys
from functools import reduce
from typing import NamedTuple, FrozenSet, Tuple, List

# ─────────────────────────────────────────────────────────────
#  ESTRUCTURAS INMUTABLES (Paradigma Funcional - Inmutabilidad)
# ─────────────────────────────────────────────────────────────

class Pregunta(NamedTuple):
    """Estructura inmutable para representar una pregunta del cuestionario."""
    id: str
    categoria: str
    texto: str
    opciones: Tuple[Tuple[str, str], ...]   # (clave_prolog, etiqueta_display)

class PerfilUsuario(NamedTuple):
    """Estructura inmutable que representa el perfil completo del usuario."""
    rasgos:     FrozenSet[str]
    habilidades: FrozenSet[str]
    intereses:  FrozenSet[str]

class ResultadoCarrera(NamedTuple):
    """Estructura inmutable para un resultado de recomendación."""
    carrera:  str
    puntaje:  float
    nivel:    str


# ─────────────────────────────────────────────────────────────
#  BANCO DE PREGUNTAS (datos inmutables)
# ─────────────────────────────────────────────────────────────

PREGUNTAS_PERFIL: Tuple[Pregunta, ...] = (
    Pregunta(
        id="p1",
        categoria="perfil",
        texto="¿Cómo describirías mejor tu forma de pensar?",
        opciones=(
            ("analitico",    "Analítico — descompongo problemas en partes"),
            ("creativo",     "Creativo — genero ideas y soluciones originales"),
            ("logico",       "Lógico — sigo razonamientos paso a paso"),
            ("investigador", "Investigador — me gusta explorar y descubrir"),
        )
    ),
    Pregunta(
        id="p2",
        categoria="perfil",
        texto="¿Cuál es tu rol más natural en un equipo?",
        opciones=(
            ("lider",       "Líder — me gusta dirigir y motivar"),
            ("organizador", "Organizador — me encargo de coordinar y planear"),
            ("practico",    "Práctico — prefiero ejecutar y hacer las cosas"),
            ("detallista",  "Detallista — cuido la precisión y calidad"),
        )
    ),
    Pregunta(
        id="p3",
        categoria="perfil",
        texto="¿Qué característica te define mejor al relacionarte con otros?",
        opciones=(
            ("comunicativo", "Comunicativo — expreso ideas con facilidad"),
            ("empático",     "Empático — entiendo bien los sentimientos ajenos"),
            ("estrategico",  "Estratégico — planifico a largo plazo"),
            ("analitico",    "Reflexivo — analizo antes de actuar"),
        )
    ),
)

PREGUNTAS_HABILIDADES: Tuple[Pregunta, ...] = (
    Pregunta(
        id="h1",
        categoria="habilidades",
        texto="¿En qué área académica te destacas o tienes más facilidad?",
        opciones=(
            ("matematicas",          "Matemáticas y cálculo"),
            ("programacion",         "Programación y tecnología"),
            ("comunicacion",         "Comunicación y redacción"),
            ("ciencias_naturales",   "Ciencias naturales (biología, química)"),
        )
    ),
    Pregunta(
        id="h2",
        categoria="habilidades",
        texto="¿Qué tipo de problemas disfrutas resolver?",
        opciones=(
            ("resolucion_problemas", "Problemas técnicos o matemáticos"),
            ("toma_decisiones",      "Decisiones estratégicas o de negocio"),
            ("gestion_recursos",     "Organización de recursos y procesos"),
            ("investigacion",        "Investigación y análisis de información"),
        )
    ),
    Pregunta(
        id="h3",
        categoria="habilidades",
        texto="¿Qué habilidad consideras tu punto más fuerte?",
        opciones=(
            ("liderazgo",            "Liderazgo y trabajo en equipo"),
            ("estadistica",          "Estadística y análisis de datos"),
            ("pensamiento_abstracto","Pensamiento abstracto y lógica"),
            ("comunicacion",         "Comunicación y relaciones interpersonales"),
        )
    ),
)

PREGUNTAS_INTERESES: Tuple[Pregunta, ...] = (
    Pregunta(
        id="i1",
        categoria="intereses",
        texto="¿Qué área del conocimiento te apasiona más?",
        opciones=(
            ("tecnologia",           "Tecnología e innovación digital"),
            ("negocios",             "Negocios y emprendimiento"),
            ("ciencias_naturales",   "Ciencias naturales y medio ambiente"),
            ("trabajo_social",       "Trabajo social y comunidad"),
        )
    ),
    Pregunta(
        id="i2",
        categoria="intereses",
        texto="¿Qué tipo de impacto quieres tener en tu trabajo?",
        opciones=(
            ("automatizacion",         "Crear soluciones tecnológicas automatizadas"),
            ("optimizacion_procesos",  "Optimizar procesos industriales o empresariales"),
            ("salud_nutricion",        "Mejorar la salud y alimentación de las personas"),
            ("liderazgo_organizacional","Liderar organizaciones o equipos de trabajo"),
        )
    ),
    Pregunta(
        id="i3",
        categoria="intereses",
        texto="¿Con cuál de estos campos te identificas más?",
        opciones=(
            ("investigacion_cientifica","Investigación científica y laboratorio"),
            ("finanzas",               "Finanzas, economía y mercados"),
            ("estadistica_analisis",   "Estadística y análisis de grandes datos"),
            ("cultura_arte",           "Cultura, arte y expresión social"),
        )
    ),
)

# Agrupación funcional de todas las preguntas
TODAS_PREGUNTAS: Tuple[Pregunta, ...] = (
    PREGUNTAS_PERFIL + PREGUNTAS_HABILIDADES + PREGUNTAS_INTERESES
)

# Mapeo de nombres de carreras para display
NOMBRES_CARRERAS = {
    "sistemas_computacionales":  "Ingeniería en Sistemas Computacionales",
    "ciencia_de_datos":          "Licenciatura en Ciencia de Datos",
    "administracion":            "Licenciatura en Administración",
    "ingenieria_industrial":     "Ingeniería Industrial",
    "ingenieria_alimentaria":    "Ingeniería en Industrias Alimentarias",
    "desarrollo_comunitario":    "Licenciatura en Desarrollo Comunitario",
    "gestion_empresarial":       "Licenciatura en Gestión Empresarial",
}

EMOJIS_CARRERA = {
    "sistemas_computacionales": "💻",
    "ciencia_de_datos":         "📊",
    "administracion":           "📋",
    "ingenieria_industrial":    "⚙️",
    "ingenieria_alimentaria":   "🍃",
    "desarrollo_comunitario":   "🤝",
    "gestion_empresarial":      "🏢",
}

COLORES_NIVEL = {
    "alta":  "\033[92m",   # verde
    "media": "\033[93m",   # amarillo
    "baja":  "\033[91m",   # rojo
}
RESET  = "\033[0m"
BOLD   = "\033[1m"
CYAN   = "\033[96m"
MAGENTA= "\033[95m"
YELLOW = "\033[93m"
BLUE   = "\033[94m"


# ─────────────────────────────────────────────────────────────
#  MOTOR PROLOG (puente Python ↔ Prolog)
# ─────────────────────────────────────────────────────────────

PROLOG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "base_conocimientos.pl")

def lista_prolog(items: FrozenSet[str]) -> str:
    """Convierte un conjunto Python en lista Prolog. Función pura."""
    return "[" + ",".join(sorted(items)) + "]"

def consultar_prolog(query: str) -> str:
    """
    Ejecuta una consulta Prolog y retorna el resultado.
    Funcion pura: misma entrada -> misma salida.
    Usa -s para cargar el archivo y -g para ejecutar la meta.
    """
    goal = f"{query}, halt ; halt(1)"
    try:
        resultado = subprocess.run(
            ["swipl", "-q", "-s", PROLOG_FILE, "-g", goal],
            capture_output=True,
            text=True,
            timeout=15
        )
        return resultado.stdout.strip()
    except subprocess.TimeoutExpired:
        return "ERROR: Tiempo de espera agotado"
    except FileNotFoundError:
        return "ERROR: SWI-Prolog no encontrado"

def consultar_top_carreras(perfil: PerfilUsuario) -> List[dict]:
    """
    Consulta Prolog para obtener el ranking de todas las carreras.
    Retorna lista de dicts con carrera, puntaje y nivel.
    Función pura (no modifica estado).
    """
    rasgos_pl      = lista_prolog(perfil.rasgos)
    habilidades_pl = lista_prolog(perfil.habilidades)
    intereses_pl   = lista_prolog(perfil.intereses)

    query = (
        f"evaluar_todas_carreras({rasgos_pl}, {habilidades_pl}, {intereses_pl}, Resultados),"
        f"forall(member(P-C, Resultados), "
        f"(nivel_compatibilidad(C, {rasgos_pl}, {habilidades_pl}, {intereses_pl}, N),"
        f"format('~w|~2f|~w~n', [C, P, N])))"
    )

    salida = consultar_prolog(query)

    if not salida or salida.startswith("ERROR"):
        return []

    # Parsear salida (paradigma funcional: map sobre líneas)
    def parsear_linea(linea: str) -> dict | None:
        partes = linea.strip().split("|")
        if len(partes) == 3:
            try:
                return {
                    "carrera": partes[0],
                    "puntaje": float(partes[1]),
                    "nivel":   partes[2]
                }
            except ValueError:
                return None
        return None

    lineas   = salida.strip().split("\n")
    parsed   = list(map(parsear_linea, lineas))
    filtrado = list(filter(lambda x: x is not None, parsed))
    return filtrado

def obtener_explicacion(carrera: str, perfil: PerfilUsuario) -> str:
    """Obtiene la explicación detallada de Prolog para una carrera."""
    rasgos_pl      = lista_prolog(perfil.rasgos)
    habilidades_pl = lista_prolog(perfil.habilidades)
    intereses_pl   = lista_prolog(perfil.intereses)

    query = (
        f"explicar_recomendacion({carrera}, {rasgos_pl}, {habilidades_pl}, "
        f"{intereses_pl}, Exp), write(Exp)"
    )
    return consultar_prolog(query)


# ─────────────────────────────────────────────────────────────
#  FUNCIONES FUNCIONALES PURAS (Paradigma Funcional)
# ─────────────────────────────────────────────────────────────

def filtrar_preguntas_por_categoria(categoria: str) -> Tuple[Pregunta, ...]:
    """
    filter: filtra preguntas por categoría. Función pura.
    """
    return tuple(filter(lambda p: p.categoria == categoria, TODAS_PREGUNTAS))

def extraer_respuesta(pregunta: Pregunta, indice: int) -> str:
    """
    Extrae la clave Prolog de una respuesta dado su índice. Función pura.
    """
    clave, _ = pregunta.opciones[indice]
    return clave

def construir_perfil(respuestas: dict) -> PerfilUsuario:
    """
    Construye el PerfilUsuario inmutable a partir de las respuestas.
    Usa map para transformar respuestas en conjuntos por categoría.
    Función pura.
    """
    def obtener_categoria(cat: str) -> FrozenSet[str]:
        preguntas_cat = filtrar_preguntas_por_categoria(cat)
        # map: transforma preguntas → respuestas Prolog
        claves = map(
            lambda p: extraer_respuesta(p, respuestas.get(p.id, 0)),
            preguntas_cat
        )
        return frozenset(claves)

    return PerfilUsuario(
        rasgos      = obtener_categoria("perfil"),
        habilidades = obtener_categoria("habilidades"),
        intereses   = obtener_categoria("intereses"),
    )

def calcular_estadisticas(resultados: List[dict]) -> dict:
    """
    Calcula estadísticas del ranking usando funciones de orden superior.
    Función pura.
    """
    if not resultados:
        return {}

    puntajes = list(map(lambda r: r["puntaje"], resultados))

    promedio = reduce(lambda acc, p: acc + p, puntajes, 0.0) / len(puntajes)
    maximo   = reduce(lambda a, b: a if a > b else b, puntajes)
    minimo   = reduce(lambda a, b: a if a < b else b, puntajes)

    alta  = len(list(filter(lambda r: r["nivel"] == "alta",  resultados)))
    media = len(list(filter(lambda r: r["nivel"] == "media", resultados)))
    baja  = len(list(filter(lambda r: r["nivel"] == "baja",  resultados)))

    return {
        "promedio": promedio,
        "maximo":   maximo,
        "minimo":   minimo,
        "alta":     alta,
        "media":    media,
        "baja":     baja,
    }

def formatear_barra(puntaje: float, ancho: int = 30) -> str:
    """Genera una barra visual de progreso. Función pura."""
    llenos  = int((puntaje / 100) * ancho)
    vacios  = ancho - llenos
    return "█" * llenos + "░" * vacios

def formatear_nombre_carrera(clave: str) -> str:
    """Obtiene el nombre display de una carrera. Función pura."""
    return NOMBRES_CARRERAS.get(clave, clave.replace("_", " ").title())

def formatear_resultado(resultado: dict, posicion: int) -> str:
    """
    Formatea un resultado para display. Función pura (sin side-effects).
    """
    carrera  = resultado["carrera"]
    puntaje  = resultado["puntaje"]
    nivel    = resultado["nivel"]
    nombre   = formatear_nombre_carrera(carrera)
    emoji    = EMOJIS_CARRERA.get(carrera, "🎓")
    barra    = formatear_barra(puntaje)
    color    = COLORES_NIVEL.get(nivel, "")
    medalla  = {1: "🥇", 2: "🥈", 3: "🥉"}.get(posicion, f" {posicion}.")

    return (
        f"  {medalla} {emoji} {BOLD}{nombre}{RESET}\n"
        f"     {color}{barra}{RESET} {BOLD}{puntaje:.1f}%{RESET}  "
        f"[{color}{nivel.upper()}{RESET}]"
    )


# ─────────────────────────────────────────────────────────────
#  INTERFAZ DE USUARIO (controlador)
# ─────────────────────────────────────────────────────────────

def limpiar_pantalla():
    os.system("clear" if os.name == "posix" else "cls")

def imprimir_encabezado():
    print(f"\n{CYAN}{'═'*62}{RESET}")
    print(f"{BOLD}{CYAN}   🎓  SISTEMA EXPERTO DE ORIENTACIÓN VOCACIONAL{RESET}")
    print(f"{CYAN}   Instituto Tecnológico de Felipe Carrillo Puerto{RESET}")
    print(f"{CYAN}        Tecnológico Nacional de México{RESET}")
    print(f"{CYAN}{'═'*62}{RESET}")
    print(f"  {YELLOW}Motor de Inferencia:{RESET} Prolog (Paradigma Lógico)")
    print(f"  {YELLOW}Controlador:{RESET}        Python (Paradigma Funcional)")
    print(f"{CYAN}{'─'*62}{RESET}\n")

def imprimir_seccion(titulo: str):
    print(f"\n{MAGENTA}{'─'*62}{RESET}")
    print(f"{BOLD}{MAGENTA}  {titulo}{RESET}")
    print(f"{MAGENTA}{'─'*62}{RESET}\n")

def solicitar_nombre() -> str:
    """Solicita el nombre del estudiante."""
    print(f"  {BLUE}¿Cuál es tu nombre?{RESET} ", end="")
    nombre = input().strip()
    return nombre if nombre else "Estudiante"

def mostrar_pregunta(pregunta: Pregunta, numero: int, total: int) -> int:
    """
    Muestra una pregunta y retorna el índice de la respuesta elegida.
    Gestiona la interacción con el usuario.
    """
    cat_labels = {
        "perfil":      f"{YELLOW}[PERFIL PERSONAL]{RESET}",
        "habilidades": f"{BLUE}[HABILIDADES]{RESET}",
        "intereses":   f"{MAGENTA}[INTERESES]{RESET}",
    }
    print(f"  Pregunta {numero}/{total}  {cat_labels.get(pregunta.categoria,'')}")
    print(f"\n  {BOLD}{pregunta.texto}{RESET}\n")

    for i, (_, etiqueta) in enumerate(pregunta.opciones, 1):
        print(f"    {CYAN}{i}.{RESET} {etiqueta}")

    while True:
        print(f"\n  Tu elección (1-{len(pregunta.opciones)}): ", end="")
        try:
            eleccion = int(input().strip())
            if 1 <= eleccion <= len(pregunta.opciones):
                return eleccion - 1          # índice base 0
            print(f"  {YELLOW}⚠  Por favor elige un número entre 1 y {len(pregunta.opciones)}{RESET}")
        except ValueError:
            print(f"  {YELLOW}⚠  Ingresa solo el número de tu respuesta{RESET}")

def ejecutar_cuestionario() -> dict:
    """
    Ejecuta el cuestionario completo y retorna el mapa de respuestas.
    Aplica principio funcional: retorna estructura inmutable de respuestas.
    """
    respuestas = {}
    total = len(TODAS_PREGUNTAS)

    secciones = [
        ("perfil",      "SECCIÓN 1: PERFIL PERSONAL",     PREGUNTAS_PERFIL),
        ("habilidades", "SECCIÓN 2: HABILIDADES",          PREGUNTAS_HABILIDADES),
        ("intereses",   "SECCIÓN 3: INTERESES Y VOCACIÓN", PREGUNTAS_INTERESES),
    ]

    numero_global = 1
    for _, titulo_sec, preguntas_sec in secciones:
        imprimir_seccion(titulo_sec)
        for pregunta in preguntas_sec:
            indice = mostrar_pregunta(pregunta, numero_global, total)
            # Inmutabilidad: creamos nuevo dict en cada iteración
            respuestas = {**respuestas, pregunta.id: indice}
            numero_global += 1
            print()

    return respuestas   # dict inmutable de resultados

def mostrar_resumen_perfil(perfil: PerfilUsuario):
    """Muestra el perfil del usuario de forma legible."""
    imprimir_seccion("📋 TU PERFIL CAPTURADO")

    def formatear_set(s: FrozenSet[str]) -> str:
        return ", ".join(sorted(s)).replace("_", " ")

    print(f"  {YELLOW}Rasgos personales:{RESET}  {formatear_set(perfil.rasgos)}")
    print(f"  {BLUE}Habilidades:{RESET}        {formatear_set(perfil.habilidades)}")
    print(f"  {MAGENTA}Intereses:{RESET}          {formatear_set(perfil.intereses)}")

def mostrar_resultados(nombre: str, resultados: List[dict], perfil: PerfilUsuario):
    """Muestra los resultados del sistema experto."""
    if not resultados:
        print(f"\n  {YELLOW}⚠  No se pudieron obtener resultados. Verifica la instalación de SWI-Prolog.{RESET}")
        return

    imprimir_seccion(f"🏆 RESULTADOS PARA {nombre.upper()}")

    print(f"  {BOLD}Ranking completo de compatibilidad:{RESET}\n")

    # map: transformar resultados en strings formateados con sus posiciones
    lineas_formateadas = list(map(
        lambda par: formatear_resultado(par[1], par[0] + 1),
        enumerate(resultados)
    ))

    for linea in lineas_formateadas:
        print(linea)
        print()

    # Estadísticas con funciones de orden superior
    stats = calcular_estadisticas(resultados)

    print(f"\n{CYAN}{'─'*62}{RESET}")
    print(f"  {BOLD}📈 Estadísticas del análisis:{RESET}")
    print(f"     Puntaje promedio: {stats['promedio']:.1f}%")
    print(f"     Compatibilidad {COLORES_NIVEL['alta']}ALTA{RESET}:  {stats['alta']} carrera(s)")
    print(f"     Compatibilidad {COLORES_NIVEL['media']}MEDIA{RESET}: {stats['media']} carrera(s)")
    print(f"     Compatibilidad {COLORES_NIVEL['baja']}BAJA{RESET}:  {stats['baja']} carrera(s)")

    # Mostrar explicación detallada de la carrera top
    top = resultados[0]
    print(f"\n{CYAN}{'─'*62}{RESET}")
    print(f"  {BOLD}🔍 Análisis detallado de tu mejor opción:{RESET}")
    explicacion = obtener_explicacion(top["carrera"], perfil)
    if explicacion and not explicacion.startswith("ERROR"):
        # Parsear la explicación de Prolog
        partes = dict(
            item.split(": ", 1)
            for item in explicacion.split(" | ")
            if ": " in item
        )
        carrera_key = top["carrera"]
        print(f"\n  {EMOJIS_CARRERA.get(carrera_key,'🎓')} {BOLD}{formatear_nombre_carrera(carrera_key)}{RESET}")
        print(f"  {'─'*45}")
        for k, v in partes.items():
            if k != "Carrera":
                print(f"  • {YELLOW}{k}:{RESET} {v}")

def mostrar_recomendacion_final(nombre: str, resultados: List[dict]):
    """Muestra el mensaje final con la recomendación principal."""
    if not resultados:
        return

    top = resultados[0]
    carrera_key  = top["carrera"]
    nombre_carr  = formatear_nombre_carrera(carrera_key)
    emoji        = EMOJIS_CARRERA.get(carrera_key, "🎓")
    puntaje      = top["puntaje"]

    print(f"\n{CYAN}{'═'*62}{RESET}")
    print(f"{BOLD}{CYAN}  ✨ RECOMENDACIÓN PRINCIPAL PARA {nombre.upper()}{RESET}")
    print(f"{CYAN}{'═'*62}{RESET}\n")
    print(f"  {emoji}  {BOLD}{nombre_carr}{RESET}")
    print(f"\n  Compatibilidad: {BOLD}{puntaje:.1f}%{RESET}  {formatear_barra(puntaje, 25)}")
    print(f"\n  {YELLOW}Esta carrera fue seleccionada por el motor de")
    print(f"  inferencia Prolog como la que mejor se alinea")
    print(f"  con tu perfil, habilidades e intereses.{RESET}")
    print(f"\n{CYAN}{'═'*62}{RESET}\n")

def confirmar_continuar(mensaje: str = "Presiona ENTER para continuar...") -> None:
    input(f"\n  {YELLOW}{mensaje}{RESET}")


# ─────────────────────────────────────────────────────────────
#  FLUJO PRINCIPAL
# ─────────────────────────────────────────────────────────────

def verificar_prolog() -> bool:
    """Verifica que SWI-Prolog esté disponible y la base de conocimientos cargue."""
    resultado = consultar_prolog("carrera(sistemas_computacionales), write(ok)")
    return "ok" in resultado

def ejecutar_sistema():
    """
    Función principal que orquesta todo el sistema experto.
    Aplica composición funcional de módulos independientes.
    """
    limpiar_pantalla()
    imprimir_encabezado()

    # ── Verificación del motor ──────────────────────────────
    print(f"  {YELLOW}🔧 Iniciando motor de inferencia Prolog...{RESET}")
    if not verificar_prolog():
        print(f"\n  {COLORES_NIVEL['baja']}✗ Error: No se pudo iniciar el motor Prolog.{RESET}")
        print(f"  Asegúrate de que SWI-Prolog esté instalado.")
        sys.exit(1)
    print(f"  {COLORES_NIVEL['alta']}✓ Motor de inferencia Prolog activo{RESET}")
    print(f"  {COLORES_NIVEL['alta']}✓ Base de conocimientos cargada (7 carreras){RESET}")

    confirmar_continuar("Presiona ENTER para iniciar el cuestionario...")
    limpiar_pantalla()
    imprimir_encabezado()

    # ── Bienvenida personalizada ────────────────────────────
    imprimir_seccion("👋 BIENVENIDO/A")
    nombre = solicitar_nombre()

    print(f"\n  Hola, {BOLD}{nombre}{RESET}! A continuación responderás")
    print(f"  {len(TODAS_PREGUNTAS)} preguntas sobre tu perfil, habilidades e intereses.")
    print(f"\n  {YELLOW}Instrucción:{RESET} Elige la opción que MEJOR te describe.")
    print(f"  No hay respuestas correctas o incorrectas.\n")

    confirmar_continuar()
    limpiar_pantalla()
    imprimir_encabezado()

    # ── Cuestionario ────────────────────────────────────────
    # Paradigma funcional: el cuestionario devuelve estructura inmutable
    respuestas = ejecutar_cuestionario()

    # ── Construcción del perfil (función pura) ──────────────
    perfil = construir_perfil(respuestas)

    limpiar_pantalla()
    imprimir_encabezado()
    mostrar_resumen_perfil(perfil)

    print(f"\n  {YELLOW}🧠 Consultando motor de inferencia Prolog...{RESET}")

    # ── Inferencia Prolog ───────────────────────────────────
    resultados = consultar_top_carreras(perfil)

    confirmar_continuar()
    limpiar_pantalla()
    imprimir_encabezado()

    # ── Resultados ──────────────────────────────────────────
    mostrar_resultados(nombre, resultados, perfil)
    mostrar_recomendacion_final(nombre, resultados)

    print(f"  {CYAN}¡Éxito en tu trayectoria académica, {nombre}! 🎓{RESET}\n")


# ─────────────────────────────────────────────────────────────
#  PUNTO DE ENTRADA
# ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    try:
        ejecutar_sistema()
    except KeyboardInterrupt:
        print(f"\n\n  {YELLOW}Sistema terminado por el usuario. ¡Hasta pronto!{RESET}\n")
        sys.exit(0)


        