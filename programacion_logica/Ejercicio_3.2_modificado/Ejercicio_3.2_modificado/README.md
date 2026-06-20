# Sistema Experto de Orientación Vocacional — TecNM
### Motor de Inferencia: Prolog · Controlador: Python (Funcional)

---

## Descripción

Sistema experto que recomienda la carrera más adecuada para estudiantes de nuevo ingreso del Tecnológico Nacional de México Campus Felipe Carrillo Puerto.

El sistema combina dos paradigmas de programación:

- **Paradigma lógico** (SWI-Prolog): actúa como motor de inferencia. Contiene la base de conocimientos con los perfiles de cada carrera y la regla `evaluar/3` que calcula coincidencias.
- **Paradigma funcional** (Python): actúa como controlador. Usa `map` y `filter` para capturar y procesar las respuestas del usuario antes de consultarle al motor Prolog.

### Carreras evaluadas

| # | Carrera |
|---|---------|
| 1 | Ingeniería en Sistemas Computacionales |
| 2 | Ingeniería en Ciencia de Datos |
| 3 | Ingeniería en Administración |
| 4 | Ingeniería Industrial |
| 5 | Ingeniería en Industrias Alimentarias |
| 6 | Ingeniería en Desarrollo Comunitario |
| 7 | Ingeniería en Gestión Empresarial |

---

## Estructura del proyecto

```
Ejercicio_3.2/
├── carreras.pl       # Base de conocimientos + motor de inferencia (Prolog)
├── index.py          # Controlador interactivo (Python funcional)
├── requirements.txt  # Dependencias Python
└── README.md         # Este archivo
```

---

## Requisitos previos

### 1. SWI-Prolog 9.0 o superior

Descarga desde: https://www.swi-prolog.org/Download.html

Verifica la instalación:
```bash
swipl --version
```

### 2. Python 3.10 o superior

Descarga desde: https://www.python.org/downloads/

Verifica la instalación:
```bash
python --version
```

### 3. Librería `pyswip`

Permite que Python se comunique con SWI-Prolog:
```bash
pip install pyswip
```

---

## Instalación

1. Descarga o clona el repositorio y accede a la carpeta del ejercicio:

```bash
git clone <url-del-repo>
cd Ejercicio_3.2
```

2. (Opcional) Crea un entorno virtual para aislar las dependencias:

```bash
python -m venv venv

# En Windows:
venv\Scripts\activate

# En macOS/Linux:
source venv/bin/activate
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

4. Asegúrate de que `carreras.pl` e `index.py` estén en el **mismo directorio** antes de ejecutar.

---

## Ejecución

Desde la carpeta del proyecto, ejecuta:

```bash
python index.py
```

El sistema presentará un cuestionario de 24 preguntas. Responde cada una con:
- `s` → sí
- `n` → no

Al finalizar, mostrará la carrera recomendada y un ranking completo ordenado por puntaje.

### Ejemplo de salida

```
    SISTEMA EXPERTO DE ORIENTACION VOCACIONAL
       Instituto Tecnologico Superior de FCP
       Motor: Prolog  │  Controlador: Python

Ingresa tu nombre completo: Ana López

Hola Ana López, responde el cuestionario con 's' para sí y 'n' para no.

¿Disfrutas escribir código o aprender lenguajes de programación? (s/n): s
¿Las matemáticas son algo que te resulta natural o interesante? (s/n): s
...

==================================================
RESULTADOS DE: ANA LÓPEZ
==================================================

Fecha y hora de evaluación: 19/06/2026 10:35:22

Carrera recomendada: Ingeniería en Sistemas Computacionales
Puntaje obtenido: 5 coincidencias

Ranking completo:
  - Ingeniería en Sistemas Computacionales: 5 puntos
  - Ingeniería en Ciencia de Datos: 3 puntos
  - Ingeniería Industrial: 2 puntos
  ...
```

---

## Arquitectura del sistema

```
┌──────────────────────────────────────────────┐
│                  index.py                    │
│            (Controlador Python)              │
│                                              │
│  construir_perfil()  →  map + filter         │
│  consultar_motor()   →  pyswip query         │
│  formatear_resultado() → map funcional       │
└────────────────────┬─────────────────────────┘
                     │  pyswip
                     ▼
┌──────────────────────────────────────────────┐
│               carreras.pl                    │
│          (Motor de Inferencia Prolog)        │
│                                              │
│  programa/2       →  base de conocimientos   │
│  contar_matches/3 →  cuenta coincidencias    │
│  evaluar/3        →  punto de entrada        │
└──────────────────────────────────────────────┘
```

---

## Solución de problemas

**`ModuleNotFoundError: No module named 'pyswip'`**
Instala la dependencia: `pip install pyswip`

**`SWI-Prolog not found` o error al consultar `carreras.pl`**
Asegúrate de que SWI-Prolog esté instalado y en el PATH del sistema. En Windows puede ser necesario reiniciar la terminal después de instalarlo.

**`FileNotFoundError: carreras.pl`**
Ejecuta el script siempre desde la carpeta donde están ambos archivos, o ajusta la ruta en `motor.consult(...)` dentro de `index.py`.

---

## Tecnologías

- **SWI-Prolog** 9.x — https://www.swi-prolog.org
- **Python** 3.10+ — https://www.python.org
- **pyswip** — https://pypi.org/project/pyswip/

---


