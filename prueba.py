import pandas as pd
import matplotlib.pyplot as plt

estudiantes= pd.read_csv("datos/estudiantes.csv", sep=';')

rutas_conteo = estudiantes['ruta'].value_counts()
print(rutas_conteo)
ordenado = rutas_conteo.sort_values(ascending=False)
print(ordenado)
