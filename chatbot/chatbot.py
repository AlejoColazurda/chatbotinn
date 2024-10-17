import chainlit as cl

@cl.on_message
async def message(message):
    # Extrae el contenido del mensaje
    input_text = message.content  # Usa message.content para obtener el texto del mensaje

    # Intenciones
    if "limpieza de datos" in input_text.lower():
        response = """Para limpiar un dataset en Python, puedes usar la biblioteca Pandas. Por ejemplo:
        ```python
        df.dropna()
        ```
        Esto eliminará los valores nulos. Más información en la [documentación de Pandas](https://pandas.pydata.org/)."""
    
    elif "visualización" in input_text.lower():
        response = """Para visualizar datos en Python, puedes usar Matplotlib. Aquí tienes un ejemplo para un histograma:
        ```python
        import matplotlib.pyplot as plt
        df['columna'].hist()
        plt.show()
        ```
        Visita la [documentación de Matplotlib](https://matplotlib.org/) para más ejemplos."""
    
    elif "modelo predictivo" in input_text.lower():
        response = """Un modelo de regresión es una técnica usada para predecir un valor continuo. Puedes usar scikit-learn:
        ```python
        from sklearn.linear_model import LinearRegression
        model = LinearRegression()
        model.fit(X_train, y_train)
        ```
        Aprende más sobre modelos en [scikit-learn](https://scikit-learn.org/)."""
    
    elif "sql" in input_text.lower():
        response = """Puedes realizar consultas SQL con `SELECT`. Por ejemplo:
        ```sql
        SELECT * FROM tabla WHERE columna = 'valor';
        ```
        Consulta esta [guía de SQL](https://www.w3schools.com/sql/) para más información."""

    elif "herramientas" in input_text.lower():
        response = """Algunas herramientas populares para el análisis de datos incluyen Python, R, SQL para bases de datos, y herramientas de visualización como Tableau y Power BI."""
    
    else:
        response = "Lo siento, no tengo una respuesta para esa consulta. ¿Podrías reformular tu pregunta?"
    
    # Enviar la respuesta como mensaje de texto
    await cl.Message(content=response).send()

if __name__ == "__main__":
    cl.run()
