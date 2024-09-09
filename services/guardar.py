import openpyxl
from openpyxl import Workbook
import os

def guardar(name, age, weight, height, bmi, category):
    """Guarda los datos en un archivo Excel."""
    file_path = 'data.xlsx'
    
    # Verificar el directorio actual
    print("Directorio actual:", os.getcwd())
    
    # Si el archivo no existe, lo crea y añade los encabezados
    if not os.path.exists(file_path):
        print("El archivo no existe. Se creará uno nuevo.")
        try:
            workbook = Workbook()
            sheet = workbook.active
            sheet.title = "Person Data"
            # Añadir encabezados
            sheet.append(["Nombre", "Edad", "Peso (kg)", "Estatura (cm)", "IMC", "Categoría"])
        except Exception as e:
            print(f"Error al crear el archivo: {e}")
            return
    else:
        print("El archivo existe. Se abrirá y se añadirá la información.")
        try:
            workbook = openpyxl.load_workbook(file_path)
            sheet = workbook.active
        except Exception as e:
            print(f"Error al abrir el archivo: {e}")
            return
    
    # Añadir los datos del usuario al Excel
    try:
        sheet.append([name, age, weight, height, bmi, category])
    except Exception as e:
        print(f"Error al añadir datos: {e}")
        return

    # Guardar el archivo Excel
    try:
        workbook.save(file_path)
        print(f"Datos guardados en {file_path}")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")