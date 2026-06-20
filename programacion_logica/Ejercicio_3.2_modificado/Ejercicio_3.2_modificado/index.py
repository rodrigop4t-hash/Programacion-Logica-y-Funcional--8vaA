from pyswip import Prolog
from datetime import datetime

# ============================================================
# INICIALIZACIÓN DEL MOTOR PROLOG
# ============================================================

motor = Prolog()
motor.consult("carreras.pl")

# ============================================================
# CATÁLOGO DE PREGUNTAS
# Cada entrada: clave_habilidad -> texto de pregunta
# ============================================================

CATALOGO = {
    "programacion":         "¿Disfrutas escribir código o aprender lenguajes de programación? (s/n): ",
    "matematicas":          "¿Las matemáticas son algo que te resulta natural o interesante? (s/n): ",
    "tecnologia":           "¿Te apasiona todo lo relacionado con la tecnología y los dispositivos? (s/n): ",
    "resolucion_problemas": "¿Te satisface encontrar soluciones a problemas complejos? (s/n): ",
    "logica":               "¿Piensas de forma estructurada y te gusta el razonamiento lógico? (s/n): ",

    "estadistica":          "¿Te llama la atención el mundo de la estadística y los números? (s/n): ",
    "analisis_datos":       "¿Te interesaría trabajar interpretando grandes cantidades de datos? (s/n): ",
    "investigacion":        "¿Te gusta profundizar en temas y llevar a cabo investigaciones? (s/n): ",

    "liderazgo":            "¿Sueles tomar la iniciativa y guiar a otras personas? (s/n): ",
    "organizacion":         "¿Tiendes a planificar y mantener el orden en tus actividades? (s/n): ",
    "negocios":             "¿El mundo de los negocios y el comercio te resulta atractivo? (s/n): ",
    "comunicacion":         "¿Se te facilita expresar ideas y comunicarte con los demás? (s/n): ",
    "gestion":              "¿Te interesa manejar recursos, tiempos y equipos de trabajo? (s/n): ",

    "optimizacion":         "¿Buscas constantemente la manera de hacer las cosas de forma más eficiente? (s/n): ",
    "procesos":             "¿Te llama la atención cómo funcionan los sistemas y los procesos productivos? (s/n): ",
    "analisis":             "¿Disfrutas analizar escenarios y proponer mejoras o soluciones? (s/n): ",

    "quimica":              "¿La química y las reacciones entre sustancias te generan curiosidad? (s/n): ",
    "biologia":             "¿Los seres vivos y los procesos biológicos son de tu interés? (s/n): ",
    "calidad":              "¿Te importa que los productos y servicios cumplan estándares de calidad? (s/n): ",

    "servicio_social":      "¿Sientes vocación por apoyar a comunidades o personas vulnerables? (s/n): ",
    "trabajo_equipo":       "¿Prefieres trabajar colaborativamente con otros hacia un objetivo común? (s/n): ",
    "gestion_social":       "¿Te gustaría impulsar el desarrollo y bienestar de comunidades? (s/n): ",

    "innovacion":           "¿Disfrutas proponer ideas nuevas y creativar soluciones originales? (s/n): ",
    "emprendimiento":       "¿Tienes el sueño o la inquietud de crear tu propia empresa? (s/n): ",
}

# Nombres legibles de cada programa académico
NOMBRES_PROGRAMA = {
    "sistemas":               "Ingeniería en Sistemas Computacionales",
    "ciencia_datos":          "Ingeniería en Ciencia de Datos",
    "administracion":         "Ingeniería en Administración",
    "industrial":             "Ingeniería Industrial",
    "alimentarias":           "Ingeniería en Industrias Alimentarias",
    "desarrollo_comunitario": "Ingeniería en Desarrollo Comunitario",
    "gestion_empresarial":    "Ingeniería en Gestión Empresarial",
}


# ============================================================
# FUNCIONES AUXILIARES (PARADIGMA FUNCIONAL)
# ============================================================

def preguntar(par):
    """Devuelve la clave de habilidad si el usuario responde 's', None si no."""
    clave, pregunta = par
    respuesta = input(pregunta).strip().lower()
    return clave if respuesta == "s" else None


def construir_perfil(catalogo):
    """
    Aplica preguntar a cada par del catálogo (map)
    y filtra las respuestas negativas (filter).
    Retorna una lista inmutable con las habilidades seleccionadas.
    """
    respuestas = map(preguntar, catalogo.items())
    return tuple(filter(lambda x: x is not None, respuestas))


def consultar_motor(perfil):
    """Convierte el perfil a sintaxis Prolog y lanza la evaluación."""
    termino = "[" + ",".join(perfil) + "]"
    query   = f"evaluar({termino}, Programa, Puntos)"
    return list(motor.query(query))


def formatear_resultado(entrada):
    """Transforma un resultado de Prolog en una tupla (nombre_legible, puntos)."""
    clave   = str(entrada["Programa"])
    puntos  = entrada["Puntos"]
    nombre  = NOMBRES_PROGRAMA.get(clave, clave)
    return (nombre, puntos)


# ============================================================
# FLUJO PRINCIPAL
# ============================================================

def main():
    print("    SISTEMA EXPERTO DE ORIENTACION VOCACIONAL")
    print("       Instituto Tecnologico Superior de FCP")
    print("       Motor: Prolog  │  Controlador: Python")
    print()

    nombre = input("Ingresa tu nombre completo: ").strip()
    print(f"\nHola {nombre}, responde el cuestionario con 's' para sí y 'n' para no.\n")

    # Captura y filtrado del perfil (funcional puro)
    perfil = construir_perfil(CATALOGO)

    # Evaluación en Prolog
    resultados_crudos = consultar_motor(perfil)

    if not resultados_crudos:
        print("No fue posible generar una recomendación.")
        return

    # Transformar resultados (map funcional)
    resultados = list(map(formatear_resultado, resultados_crudos))

    # Ordenar de mayor a menor puntaje
    ranking = sorted(resultados, key=lambda x: x[1], reverse=True)
    mejor   = ranking[0]

    # Mostrar resultados
    separador = "=" * 50
    fecha     = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    print(f"\n{separador}")
    print(f"RESULTADOS DE: {nombre.upper()}")
    print(separador)
    print(f"\nFecha y hora de evaluación: {fecha}")
    print(f"\nCarrera recomendada: {mejor[0]}")
    print(f"Puntaje obtenido: {mejor[1]} coincidencias")
    print("\nRanking completo:")

    for nombre_prog, puntos in ranking:
        print(f"  - {nombre_prog}: {puntos} puntos")


if __name__ == "__main__":
    main()
