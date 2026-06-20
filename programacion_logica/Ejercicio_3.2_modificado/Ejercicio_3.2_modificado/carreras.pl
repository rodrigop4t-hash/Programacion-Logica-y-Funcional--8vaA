
% ============================================================
% BASE DE CONOCIMIENTOS — ORIENTACION VOCACIONAL
% ============================================================

% Cada programa academico se define con sus habilidades clave.

programa(sistemas,
    [programacion, matematicas, tecnologia, resolucion_problemas, logica]).

programa(ciencia_datos,
    [matematicas, estadistica, analisis_datos, investigacion, programacion]).

programa(administracion,
    [liderazgo, organizacion, negocios, comunicacion, gestion]).

programa(industrial,
    [matematicas, optimizacion, procesos, liderazgo, analisis]).

programa(alimentarias,
    [quimica, biologia, investigacion, calidad, procesos]).

programa(desarrollo_comunitario,
    [servicio_social, liderazgo, comunicacion, trabajo_equipo, gestion_social]).

programa(gestion_empresarial,
    [negocios, liderazgo, innovacion, emprendimiento, gestion]).


% ============================================================
% MOTOR DE INFERENCIA
% ============================================================

% Calcula cuantas habilidades del perfil del usuario
% coinciden con las requeridas por el programa.

contar_matches([], _, 0).

contar_matches([Hab|Resto], Perfil, Total) :-
    member(Hab, Perfil),
    !,
    contar_matches(Resto, Perfil, Parcial),
    Total is Parcial + 1.

contar_matches([_|Resto], Perfil, Total) :-
    contar_matches(Resto, Perfil, Total).

% Punto de entrada: evalua un perfil contra todos los programas.
evaluar(Perfil, Programa, Puntos) :-
    programa(Programa, Habilidades),
    contar_matches(Habilidades, Perfil, Puntos).
