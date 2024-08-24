import requests
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import creds  # Importar el archivo creds.py donde se almacena el token

# URL de la API del INEGI para obtener la población de hombres y mujeres
url = f"https://www.inegi.org.mx/app/api/indicadores/desarrolladores/jsonxml/INDICATOR/1002000002,1002000003/es/0700/false/BISE/2.0/{creds.token}?type=json"

# Realizar la solicitud a la API
response = requests.get(url)
data = response.json()

# Extraer los datos para hombres y mujeres
hombres_data = data['Series'][0]['OBSERVATIONS']
mujeres_data = data['Series'][1]['OBSERVATIONS']

# Convertir los datos en DataFrames
hombres_df = pd.DataFrame(hombres_data)
mujeres_df = pd.DataFrame(mujeres_data)

# Convertir el periodo a formato datetime
hombres_df['TIME_PERIOD'] = pd.to_datetime(hombres_df['TIME_PERIOD'])
mujeres_df['TIME_PERIOD'] = pd.to_datetime(mujeres_df['TIME_PERIOD'])

# Convertir los valores a números
hombres_df['OBS_VALUE'] = pd.to_numeric(hombres_df['OBS_VALUE'])
mujeres_df['OBS_VALUE'] = pd.to_numeric(mujeres_df['OBS_VALUE'])

# Renombrar las columnas para claridad
hombres_df.rename(columns={'TIME_PERIOD': 'Fecha', 'OBS_VALUE': 'Población Hombres'}, inplace=True)
mujeres_df.rename(columns={'TIME_PERIOD': 'Fecha', 'OBS_VALUE': 'Población Mujeres'}, inplace=True)

# Unir los DataFrames en uno solo para facilitar la graficación
df = pd.merge(hombres_df[['Fecha', 'Población Hombres']], mujeres_df[['Fecha', 'Población Mujeres']], on='Fecha')

# Crear la gráfica con formato cuadrado
plt.figure(figsize=(8, 8))  # Ajustar el tamaño a un formato cuadrado

# Graficar los datos
plt.plot(df['Fecha'], df['Población Hombres'], label='Población Hombres', color='blue')
plt.plot(df['Fecha'], df['Población Mujeres'], label='Población Mujeres', color='red')

# Añadir título y etiquetas
plt.title('Población Total de Hombres y Mujeres en México (1910 - 2020)')
plt.xlabel('Fecha')
plt.ylabel('Población (Millones)')

# Formatear el eje Y para mostrar los números en millones
plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{x*1e-6:.1f}M'))

# Añadir la leyenda para identificar las series
plt.legend(loc="upper left")

# Añadir la fuente de datos y el creador en el pie de la figura
plt.figtext(0.5, 0.02, "Fuente de datos: INEGI - API REST\nCreado por: Francisco Javier García García", 
            ha="center", fontsize=10, bbox={"facecolor": "lightgrey", "alpha": 0.5, "pad": 5})

# Obtener el último valor para hombres y mujeres
last_hombres = df.iloc[-1]
last_mujeres = df.iloc[-1]

# Añadir anotaciones para el último valor de hombres
plt.annotate(f'{last_hombres["Población Hombres"]*1e-6:.1f}M',
             xy=(last_hombres['Fecha'], last_hombres['Población Hombres']),
             xytext=(5, 5),  # Mover un poco el texto para que no se superponga
             textcoords="offset points",
             arrowprops=dict(facecolor='blue', arrowstyle="->"),
             fontsize=10, color='blue')

# Añadir anotaciones para el último valor de mujeres
plt.annotate(f'{last_mujeres["Población Mujeres"]*1e-6:.1f}M',
             xy=(last_mujeres['Fecha'], last_mujeres['Población Mujeres']),
             xytext=(5, 5),
             textcoords="offset points",
             arrowprops=dict(facecolor='red', arrowstyle="->"),
             fontsize=10, color='red')

# Guardar la gráfica en un archivo con DPI ajustado
plt.savefig('grafica_instagram.png', dpi=150, bbox_inches='tight')  # DPI ajustado para evitar problemas de tamaño

# Mostrar la gráfica
plt.show()
