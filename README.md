Proyecto: Visualización de la Población de Hombres y Mujeres en México a traves del tiempo

Este proyecto tiene como objetivo visualizar la evolución de la población de hombres y mujeres en México a lo largo del tiempo, utilizando datos obtenidos de la API de Indicadores del Instituto Nacional de Estadística y Geografía (INEGI).

Descripción del Proyecto:

    El script realiza las siguientes tareas:

        Obtención de Datos: Utiliza la API de Indicadores del INEGI para descargar la serie histórica de población total de hombres y mujeres en México.

        Procesamiento de Datos: Los datos obtenidos se procesan y se almacenan en DataFrames utilizando la librería pandas para facilitar su manipulación.

        Visualización: Se genera una gráfica que muestra la evolución de la población de hombres y mujeres en un formato adecuado para Instagram. La gráfica incluye:

        Serie histórica de población para hombres y mujeres.
        Anotaciones que destacan los últimos valores registrados para ambas poblaciones.
        Una leyenda que identifica claramente las series de datos.
        Un pie de página que acredita al INEGI como fuente de los datos y al creador del gráfico.
        Exportación: La gráfica se guarda como una imagen PNG de alta resolución, lista para ser compartida en Instagram.

Requisitos
Este proyecto requiere de las siguientes dependencias de Python:

    requests
    pandas
    matplotlib

Detalles Técnicos:
    API del INEGI
    La API utilizada permite obtener datos estadísticos de México de manera programática. En este proyecto, se han utilizado los siguientes identificadores de indicadores:

        1002000002: Población total de hombres.
        1002000003: Población total de mujeres.
        Formato de la Gráfica
        La gráfica se ha diseñado en un formato cuadrado (8x8) y se guarda con una resolución de 150 DPI, lo que asegura una visualización clara y nítida en plataformas de redes sociales.

Autor:

    Francisco Javier García García

Licencia:
    
    Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

Créditos:

    Fuente de datos: INEGI - API 
