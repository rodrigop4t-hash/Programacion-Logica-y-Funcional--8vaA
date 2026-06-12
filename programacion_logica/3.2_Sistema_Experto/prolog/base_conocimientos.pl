% ================================================================
%  BASE DE CONOCIMIENTOS - SISTEMA EXPERTO ORIENTACION VOCACIONAL
%  Instituto Tecnologico de Felipe Carrillo Puerto
%  Tecnologico Nacional de Mexico
%  Motor de Inferencia: Prolog (Paradigma Logico)
% ================================================================
%
%  DESCRIPCION
%  -----------
%  Este archivo define la base de conocimientos del sistema experto.
%  Contiene hechos (perfiles, habilidades, intereses por carrera) y
%  reglas de inferencia que el motor Prolog usa para calcular la
%  compatibilidad entre un estudiante y cada carrera disponible.
%
%  USO NORMAL (invocado automaticamente por sistema_experto.py)
%  -------------------------------------------------------------
%  No es necesario ejecutar este archivo directamente.
%  El controlador Python lo carga con:
%      swipl -q -s base_conocimientos.pl -g "<consulta>, halt"
%
%  USO DIRECTO DESDE TERMINAL (pruebas y depuracion)
%  ---------------------------------------------------
%  Cargar la base de conocimientos en modo interactivo:
%      swipl base_conocimientos.pl
%
%  Una vez en el interprete de Prolog (?-), ejemplos de consultas:
%
%  -- Listar todas las carreras registradas:
%      ?- carrera(C).
%
%  -- Ver habilidades requeridas para Sistemas:
%      ?- habilidad_requerida(sistemas_computacionales, H).
%
%  -- Calcular puntaje para un perfil especifico:
%      ?- calcular_puntaje(sistemas_computacionales,
%           [analitico, logico],
%           [programacion, matematicas],
%           [tecnologia, automatizacion],
%           Puntaje).
%
%  -- Obtener el ranking completo de carreras para un perfil:
%      ?- evaluar_todas_carreras(
%           [analitico, logico, detallista, creativo],
%           [programacion, matematicas, resolucion_problemas, pensamiento_abstracto],
%           [tecnologia, automatizacion, ciencias_exactas, videojuegos_software],
%           Resultados).
%
%  -- Obtener la carrera recomendada (top 1):
%      ?- recomendar_carrera(
%           [lider, comunicativo],
%           [liderazgo, comunicacion],
%           [negocios, finanzas],
%           Carrera, Puntaje).
%
%  -- Verificar nivel de compatibilidad de una carrera:
%      ?- nivel_compatibilidad(administracion,
%           [lider, organizador],
%           [liderazgo, comunicacion],
%           [negocios, economia],
%           Nivel).
%
%  -- Obtener explicacion detallada de la recomendacion:
%      ?- explicar_recomendacion(sistemas_computacionales,
%           [analitico, logico],
%           [programacion, matematicas],
%           [tecnologia, ciencias_exactas],
%           Explicacion).
%
%  Salir del interprete:
%      ?- halt.
%
%  Verificar que el archivo carga sin errores (sin modo interactivo):
%      swipl -q -t halt -f base_conocimientos.pl
%
%  ESTRUCTURA DE LA BASE DE CONOCIMIENTOS
%  ----------------------------------------
%  Carreras           : 7
%  Hechos por carrera : 4 perfiles + 4 habilidades + 4 intereses = 12
%  Total de hechos    : 84
%  Reglas principales : calcular_puntaje, evaluar_todas_carreras,
%                       recomendar_carrera, nivel_compatibilidad,
%                       explicar_recomendacion
%
%  PONDERACION
%  -----------
%  Perfil personal : 30%  |  Habilidades : 40%  |  Intereses : 30%
%  Alta >= 70%  /  Media >= 40%  /  Baja < 40%
%
% ================================================================

:- discontiguous carrera/1.
:- discontiguous perfil/2.
:- discontiguous habilidad_requerida/2.
:- discontiguous interes_requerido/2.

% ------------------------------------------------------------
%  HECHOS: Definicion de Carreras
% ------------------------------------------------------------
carrera(sistemas_computacionales).
carrera(ciencia_de_datos).
carrera(administracion).
carrera(ingenieria_industrial).
carrera(ingenieria_alimentaria).
carrera(desarrollo_comunitario).
carrera(gestion_empresarial).

% ------------------------------------------------------------
%  HECHOS: Perfiles por Carrera
%  perfil(Carrera, RasgoPersonalidad)
% ------------------------------------------------------------
perfil(sistemas_computacionales, analitico).
perfil(sistemas_computacionales, logico).
perfil(sistemas_computacionales, creativo).
perfil(sistemas_computacionales, detallista).

perfil(ciencia_de_datos, analitico).
perfil(ciencia_de_datos, logico).
perfil(ciencia_de_datos, investigador).
perfil(ciencia_de_datos, detallista).

perfil(administracion, lider).
perfil(administracion, organizador).
perfil(administracion, comunicativo).
perfil(administracion, estrategico).

perfil(ingenieria_industrial, analitico).
perfil(ingenieria_industrial, organizador).
perfil(ingenieria_industrial, practico).
perfil(ingenieria_industrial, estrategico).

perfil(ingenieria_alimentaria, investigador).
perfil(ingenieria_alimentaria, practico).
perfil(ingenieria_alimentaria, detallista).
perfil(ingenieria_alimentaria, creativo).

perfil(desarrollo_comunitario, comunicativo).
perfil(desarrollo_comunitario, lider).
perfil(desarrollo_comunitario, empatico).
perfil(desarrollo_comunitario, creativo).

perfil(gestion_empresarial, lider).
perfil(gestion_empresarial, estrategico).
perfil(gestion_empresarial, comunicativo).
perfil(gestion_empresarial, organizador).

% ------------------------------------------------------------
%  HECHOS: Habilidades Requeridas por Carrera
%  habilidad_requerida(Carrera, Habilidad)
% ------------------------------------------------------------
habilidad_requerida(sistemas_computacionales, programacion).
habilidad_requerida(sistemas_computacionales, matematicas).
habilidad_requerida(sistemas_computacionales, resolucion_problemas).
habilidad_requerida(sistemas_computacionales, pensamiento_abstracto).

habilidad_requerida(ciencia_de_datos, estadistica).
habilidad_requerida(ciencia_de_datos, matematicas).
habilidad_requerida(ciencia_de_datos, programacion).
habilidad_requerida(ciencia_de_datos, resolucion_problemas).

habilidad_requerida(administracion, gestion_recursos).
habilidad_requerida(administracion, toma_decisiones).
habilidad_requerida(administracion, comunicacion).
habilidad_requerida(administracion, liderazgo).

habilidad_requerida(ingenieria_industrial, matematicas).
habilidad_requerida(ingenieria_industrial, gestion_recursos).
habilidad_requerida(ingenieria_industrial, resolucion_problemas).
habilidad_requerida(ingenieria_industrial, toma_decisiones).

habilidad_requerida(ingenieria_alimentaria, ciencias_naturales).
habilidad_requerida(ingenieria_alimentaria, matematicas).
habilidad_requerida(ingenieria_alimentaria, resolucion_problemas).
habilidad_requerida(ingenieria_alimentaria, investigacion).

habilidad_requerida(desarrollo_comunitario, comunicacion).
habilidad_requerida(desarrollo_comunitario, liderazgo).
habilidad_requerida(desarrollo_comunitario, gestion_recursos).
habilidad_requerida(desarrollo_comunitario, investigacion).

habilidad_requerida(gestion_empresarial, comunicacion).
habilidad_requerida(gestion_empresarial, liderazgo).
habilidad_requerida(gestion_empresarial, toma_decisiones).
habilidad_requerida(gestion_empresarial, gestion_recursos).

% ------------------------------------------------------------
%  HECHOS: Intereses por Carrera
%  interes_requerido(Carrera, Interes)
% ------------------------------------------------------------
interes_requerido(sistemas_computacionales, tecnologia).
interes_requerido(sistemas_computacionales, videojuegos_software).
interes_requerido(sistemas_computacionales, automatizacion).
interes_requerido(sistemas_computacionales, ciencias_exactas).

interes_requerido(ciencia_de_datos, tecnologia).
interes_requerido(ciencia_de_datos, investigacion_cientifica).
interes_requerido(ciencia_de_datos, ciencias_exactas).
interes_requerido(ciencia_de_datos, estadistica_analisis).

interes_requerido(administracion, negocios).
interes_requerido(administracion, economia).
interes_requerido(administracion, liderazgo_organizacional).
interes_requerido(administracion, finanzas).

interes_requerido(ingenieria_industrial, manufactura).
interes_requerido(ingenieria_industrial, optimizacion_procesos).
interes_requerido(ingenieria_industrial, ciencias_exactas).
interes_requerido(ingenieria_industrial, negocios).

interes_requerido(ingenieria_alimentaria, ciencias_naturales).
interes_requerido(ingenieria_alimentaria, salud_nutricion).
interes_requerido(ingenieria_alimentaria, investigacion_cientifica).
interes_requerido(ingenieria_alimentaria, manufactura).

interes_requerido(desarrollo_comunitario, trabajo_social).
interes_requerido(desarrollo_comunitario, medio_ambiente).
interes_requerido(desarrollo_comunitario, cultura_arte).
interes_requerido(desarrollo_comunitario, liderazgo_organizacional).

interes_requerido(gestion_empresarial, negocios).
interes_requerido(gestion_empresarial, liderazgo_organizacional).
interes_requerido(gestion_empresarial, finanzas).
interes_requerido(gestion_empresarial, economia).

% ------------------------------------------------------------
%  REGLAS DE INFERENCIA
% ------------------------------------------------------------

% Predicados auxiliares para include/3
carrera_tiene_perfil(Carrera, Rasgo) :-
    perfil(Carrera, Rasgo).

carrera_tiene_habilidad(Carrera, Habilidad) :-
    habilidad_requerida(Carrera, Habilidad).

carrera_tiene_interes(Carrera, Interes) :-
    interes_requerido(Carrera, Interes).

% Cuenta coincidencias de perfil
contar_coincidencias_perfil(Carrera, Rasgos, Cuenta) :-
    include(carrera_tiene_perfil(Carrera), Rasgos, Coincidencias),
    length(Coincidencias, Cuenta).

% Cuenta coincidencias de habilidades
contar_coincidencias_habilidades(Carrera, Habilidades, Cuenta) :-
    include(carrera_tiene_habilidad(Carrera), Habilidades, Coincidencias),
    length(Coincidencias, Cuenta).

% Cuenta coincidencias de intereses
contar_coincidencias_intereses(Carrera, Intereses, Cuenta) :-
    include(carrera_tiene_interes(Carrera), Intereses, Coincidencias),
    length(Coincidencias, Cuenta).

% Calcula el puntaje total ponderado
% Pesos: Perfil=30%, Habilidades=40%, Intereses=30%
calcular_puntaje(Carrera, Rasgos, Habilidades, Intereses, Puntaje) :-
    contar_coincidencias_perfil(Carrera, Rasgos, CP),
    contar_coincidencias_habilidades(Carrera, Habilidades, CH),
    contar_coincidencias_intereses(Carrera, Intereses, CI),
    PuntajePerfil is (CP / 4.0) * 30,
    PuntajeHabilidades is (CH / 4.0) * 40,
    PuntajeIntereses is (CI / 4.0) * 30,
    Puntaje is PuntajePerfil + PuntajeHabilidades + PuntajeIntereses.

% Genera lista ordenada de puntajes para todas las carreras
evaluar_todas_carreras(Rasgos, Habilidades, Intereses, Resultados) :-
    findall(
        Puntaje-Carrera,
        (
            carrera(Carrera),
            calcular_puntaje(Carrera, Rasgos, Habilidades, Intereses, Puntaje)
        ),
        Pares
    ),
    msort(Pares, Ordenados),
    reverse(Ordenados, Resultados).

% Regla principal: recomienda la carrera con mayor puntaje
recomendar_carrera(Rasgos, Habilidades, Intereses, Carrera, Puntaje) :-
    evaluar_todas_carreras(Rasgos, Habilidades, Intereses, [Puntaje-Carrera|_]).

% Regla de compatibilidad alta (>= 70%)
compatibilidad_alta(Carrera, Rasgos, Habilidades, Intereses) :-
    calcular_puntaje(Carrera, Rasgos, Habilidades, Intereses, Puntaje),
    Puntaje >= 70.

% Regla de compatibilidad media (>= 40%)
compatibilidad_media(Carrera, Rasgos, Habilidades, Intereses) :-
    calcular_puntaje(Carrera, Rasgos, Habilidades, Intereses, Puntaje),
    Puntaje >= 40,
    Puntaje < 70.

% Determinar nivel de compatibilidad
nivel_compatibilidad(Carrera, Rasgos, Habilidades, Intereses, alta) :-
    compatibilidad_alta(Carrera, Rasgos, Habilidades, Intereses), !.
nivel_compatibilidad(Carrera, Rasgos, Habilidades, Intereses, media) :-
    compatibilidad_media(Carrera, Rasgos, Habilidades, Intereses), !.
nivel_compatibilidad(_, _, _, _, baja).

% Predicados STEM
es_stem(matematicas).
es_stem(programacion).
es_stem(estadistica).
es_stem(ciencias_naturales).
es_stem(pensamiento_abstracto).
es_stem(resolucion_problemas).

% Contar habilidades STEM
contar_habilidades_stem(Habilidades, Cuenta) :-
    include(es_stem, Habilidades, STEM),
    length(STEM, Cuenta).

% Vocacion social
tiene_vocacion_social(Rasgos, Intereses) :-
    (member(empatico, Rasgos) ; member(comunicativo, Rasgos)),
    (member(trabajo_social, Intereses) ; member(medio_ambiente, Intereses)).

% Explicacion detallada
explicar_recomendacion(Carrera, Rasgos, Habilidades, Intereses, Explicacion) :-
    contar_coincidencias_perfil(Carrera, Rasgos, CP),
    contar_coincidencias_habilidades(Carrera, Habilidades, CH),
    contar_coincidencias_intereses(Carrera, Intereses, CI),
    calcular_puntaje(Carrera, Rasgos, Habilidades, Intereses, Puntaje),
    format(atom(Explicacion),
        'Carrera: ~w | Puntaje: ~2f% | Perfil: ~w/4 | Habilidades: ~w/4 | Intereses: ~w/4',
        [Carrera, Puntaje, CP, CH, CI]).


    