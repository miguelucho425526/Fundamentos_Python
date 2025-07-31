# Definimos la variable 'kilometers' y le asignamos el valor 12.25 (kilómetros)
kilometers = 12.25

# Definimos la variable 'miles' y le asignamos el valor 7.38 (millas)
miles = 7.38

# Convertimos millas a kilómetros multiplicando por 1.61 (1 milla ≈ 1.61 km)
miles_to_kilometers = miles * 1.61

# Convertimos kilómetros a millas dividiendo por 1.61 (1 km ≈ 0.62 millas)
kilometers_to_miles = kilometers / 1.61

# Imprimimos el resultado de la conversión de millas a kilómetros, redondeando a 2 decimales
print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")

# Imprimimos el resultado de la conversión de kilómetros a millas, redondeando a 2 decimales
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")