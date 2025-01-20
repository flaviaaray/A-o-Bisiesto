#Tarea año bisiesto

def contar_bisiestos_sin_ciclo(año):

    # Calculamos la cantidad de años bisiestos tomando en cuenta los 4 años
    bisiestos_4 = (año - 1900) // 4

    # Restamos los años que son divisibles entre 100 pero no entre 400
    bisiestos_100 = (año - 1900) // 100
    bisiestos_400 = (año - 1900) // 400
    return bisiestos_4 - bisiestos_100 + bisiestos_400

# Obtenemos el año de entrada
año_ingresado = int(input("Ingrese un año entre 1900 y 2199: "))

# Calculamos y mostramos el resultado
resultado = contar_bisiestos_sin_ciclo(año_ingresado)
print(f"El número de años bisiestos hasta {año_ingresado} es: {resultado}")
