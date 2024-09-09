from flask import Blueprint, render_template, request
from services.calculator import calculate_bmi, get_recommendation
from services.guardar import guardar  # Asegúrate de importar la función

app = Blueprint('views', __name__)

@app.route('/')
def home():
    return render_template('formulario.html')

@app.route('/result', methods=['POST'])
def result():
    name = request.form['name']
    age = int (request.form['age'])
    weight = float(request.form['weight'])
    height = float(request.form['height'])

    # Calcular el IMC
    bmi = calculate_bmi(weight, height)
    category, recommendation, color = get_recommendation(bmi)

    # Guardar los datos en el archivo Excel
    guardar (name, age, weight, height, bmi, category)

    return render_template('resultados.html', name=name, age=age, weight=weight, height=height, bmi=bmi, category=category, recommendation=recommendation, color=color)
