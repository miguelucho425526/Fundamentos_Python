# 1. Calcular el puntaje total de un jugador
# Solicitamos los puntos de tres niveles y sumamos para obtener el total.
nivel1 = int(input("Ingrese los puntos del nivel 1: "))
nivel2 = int(input("Ingrese los puntos del nivel 2: "))
nivel3 = int(input("Ingrese los puntos del nivel 3: "))
puntaje_total = nivel1 + nivel2 + nivel3
print("Puntaje total del jugador:", puntaje_total)

# 2. Calcular el tiempo total de juego en segundos
# Solicitamos horas, minutos y segundos, y convertimos todo a segundos.
horas = int(input("Ingrese las horas jugadas: "))
minutos = int(input("Ingrese los minutos jugados: "))
segundos = int(input("Ingrese los segundos jugados: "))
tiempo_total_segundos = horas * 3600 + minutos * 60 + segundos
print("Tiempo total jugado en segundos:", tiempo_total_segundos)

# 3. Calcular el daño total causado por un personaje
# Sumamos el daño de tres ataques.
ataque1 = int(input("Ingrese el daño del primer ataque: "))
ataque2 = int(input("Ingrese el daño del segundo ataque: "))
ataque3 = int(input("Ingrese el daño del tercer ataque: "))
danio_total = ataque1 + ataque2 + ataque3
print("Daño total causado:", danio_total)

# 4. Calcular la experiencia total ganada
# Sumamos la experiencia de tres misiones.
exp1 = int(input("Ingrese la experiencia de la misión 1: "))
exp2 = int(input("Ingrese la experiencia de la misión 2: "))
exp3 = int(input("Ingrese la experiencia de la misión 3: "))
exp_total = exp1 + exp2 + exp3
print("Experiencia total acumulada:", exp_total)

# 5. Calcular el porcentaje de vida restante
# Calculamos el porcentaje de vida actual respecto a la vida máxima.
vida_max = int(input("Ingrese la vida máxima del personaje: "))
vida_actual = int(input("Ingrese la vida actual del personaje: "))
porcentaje_vida = (vida_actual / vida_max) * 100
print("Porcentaje de vida restante:", porcentaje_vida, "%")

# 6. Calcular el oro total recolectado
# Sumamos el oro de tres misiones.
oro1 = int(input("Ingrese el oro recolectado en la misión 1: "))
oro2 = int(input("Ingrese el oro recolectado en la misión 2: "))
oro3 = int(input("Ingrese el oro recolectado en la misión 3: "))
oro_total = oro1 + oro2 + oro3
print("Oro total acumulado:", oro_total)

# 7. Calcular la velocidad promedio de un vehículo
# Dividimos la distancia recorrida entre el tiempo tomado.
distancia = float(input("Ingrese la distancia recorrida (en km): "))
tiempo = float(input("Ingrese el tiempo tomado (en horas): "))
velocidad_promedio = distancia / tiempo
print("Velocidad promedio del vehículo:", velocidad_promedio, "km/h")

# 8. Calcular el costo total de mejoras
# Sumamos el costo de tres mejoras.
mejora1 = float(input("Ingrese el costo de la mejora 1: "))
mejora2 = float(input("Ingrese el costo de la mejora 2: "))
mejora3 = float(input("Ingrese el costo de la mejora 3: "))
costo_total_mejoras = mejora1 + mejora2 + mejora3
print("Costo total de las mejoras:", costo_total_mejoras)

# 9. Calcular el tiempo restante para completar una misión
# Restamos el tiempo transcurrido al tiempo total de la misión.
tiempo_total_mision = int(input("Ingrese el tiempo total de la misión (en minutos): "))
tiempo_transcurrido = int(input("Ingrese el tiempo transcurrido (en minutos): "))
tiempo_restante = tiempo_total_mision - tiempo_transcurrido
print("Tiempo restante para completar la misión:", tiempo_restante, "minutos")

# 10. Calcular el nivel promedio de un equipo de jugadores
# Calculamos el promedio de los niveles de tres jugadores.
nivel_j1 = int(input("Ingrese el nivel del jugador 1: "))
nivel_j2 = int(input("Ingrese el nivel del jugador 2: "))
nivel_j3 = int(input("Ingrese el nivel del jugador 3: "))
nivel_promedio = (nivel_j1 + nivel_j2 + nivel_j3) / 3
print("Nivel promedio del equipo:", nivel_promedio)

# 11. Calcular el daño crítico en un ataque
# Multiplicamos el daño base por el multiplicador crítico.
danio_base = float(input("Ingrese el daño base del ataque: "))
multiplicador_critico = float(input("Ingrese el multiplicador crítico: "))
danio_critico = danio_base * multiplicador_critico
print("Daño crítico del ataque:", danio_critico)

# 12. Calcular el tiempo total de juego en horas y minutos
# Convertimos los minutos jugados a horas y minutos.
minutos_jugados = int(input("Ingrese el tiempo total jugado en minutos: "))
horas_jugadas = minutos_jugados // 60
minutos_restantes = minutos_jugados % 60
print("Tiempo total jugado:", horas_jugadas, "horas y", minutos_restantes, "minutos")

# 13. Calcular el porcentaje de misiones completadas
# Calculamos el porcentaje de misiones completadas respecto al total.
total_misiones = int(input("Ingrese el número total de misiones: "))
misiones_completadas = int(input("Ingrese el número de misiones completadas: "))
porcentaje_misiones = (misiones_completadas / total_misiones) * 100
print("Porcentaje de misiones completadas:", porcentaje_misiones, "%")

# 14. Calcular el costo total de objetos comprados en una tienda
# Sumamos el costo de tres objetos comprados.
objeto1 = float(input("Ingrese el costo del objeto 1: "))
objeto2 = float(input("Ingrese el costo del objeto 2: "))
objeto3 = float(input("Ingrese el costo del objeto 3: "))
costo_total_objetos = objeto1 + objeto2 + objeto3
print("Costo total de los objetos comprados:", costo_total_objetos)

# 15. Calcular el tiempo promedio de una partida
# Calculamos el promedio del tiempo de tres partidas.
partida1 = float(input("Ingrese el tiempo de la partida 1 (en minutos): "))
partida2 = float(input("Ingrese el tiempo de la partida 2 (en minutos): "))
partida3 = float(input("Ingrese el tiempo de la partida 3 (en minutos): "))
tiempo_promedio = (partida1 + partida2 + partida3) / 3
print("Tiempo promedio de las partidas:", tiempo_promedio, "minutos")

# 16. Calcular el porcentaje de enemigos derrotados
# Calculamos el porcentaje de enemigos derrotados respecto al total.
total_enemigos = int(input("Ingrese el número total de enemigos: "))
enemigos_derrotados = int(input("Ingrese el número de enemigos derrotados: "))
porcentaje_enemigos = (enemigos_derrotados / total_enemigos) * 100
print("Porcentaje de enemigos derrotados:", porcentaje_enemigos, "%")