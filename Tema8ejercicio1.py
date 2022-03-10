#En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt,
# lo abráis y escribáis dentro del archivo. Para ello, tendréis que acceder dos
# veces al archivo creado.

archivo=open("ejercicio8pythonob.txt", "w")
archivo.write("Hola.\n")
archivo.write("¿Cómo vamos?.\n")
archivo.close()