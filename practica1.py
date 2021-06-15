from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt

print("CARGANDO EL ARCHIVO......")
print("------------------------------------------------------------------------------------------------")
data = pd.read_csv('tarjetas.csv')
print(data)
print()
print("------------------------------------------------------------------------------------------------")


print("Visualizar los primeros 7 registros del conjunto de datos")
print("------------------------------------------------------------------------------------------------")
print(data.head(7))
print()
print("------------------------------------------------------------------------------------------------")

print("Visualizar los últimos 6 registros del conjunto de datos")
print("------------------------------------------------------------------------------------------------")
print(data.tail(6))
print()
print("------------------------------------------------------------------------------------------------")


print("Generar los estadísticos básicos")
print("------------------------------------------------------------------------------------------------")
print(data.describe())
print()
print("------------------------------------------------------------------------------------------------")

print("Verificando si hay valores vacios")
print("------------------------------------------------------------------------------------------------")
print(data.isnull())
print()
print("------------------------------------------------------------------------------------------------")

print("Completar todos los datos vacíos (na) con ceros (0)")
print("------------------------------------------------------------------------------------------------")
datallena = data.fillna(0)
print(datallena)
print()
print("------------------------------------------------------------------------------------------------")


print("Realizar un gráfico de tipo 'scatter' utilizando para el eje X la variable 'comprador_recurrente'y para el eje Y la variable'reclamaciones'.")
print("------------------------------------------------------------------------------------------------")
v_graficar = datallena.plot(x='comprador_recurrente', y='reclamaciones', kind='scatter', color="blue")
plt.show()
print()
print()
print("------------------------------------------------------------------------------------------------")





