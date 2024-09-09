def calculate_bmi(weight, height):
    """Calcula el IMC basado en el peso y la estatura."""
    height_in_meters = height / 100
    bmi = weight / (height_in_meters ** 2)
    return round(bmi, 2)

def get_recommendation(bmi):
    """Devuelve la categoría, recomendación y color según el IMC."""
    if bmi < 18.5:
        return "Peso bajo", "Consulta más información sobre cómo ganar peso de forma saludable en este [enlace](https://www.who.int/nutrition).", "yellow"
    elif 18.5 <= bmi < 25:
        return "Peso saludable", "Sigue manteniendo un estilo de vida saludable. Consulta consejos en este [enlace](https://www.health.com/fitness).", "green"
    elif 25 <= bmi < 30:
        return "Sobrepeso", "Te sugerimos leer más sobre cómo perder peso en este [enlace](https://www.cdc.gov/obesity/).", "orange"
    else:
        return "Obesidad", "Consulta información sobre la obesidad en este [enlace](https://www.who.int/topics/obesity).", "red"
