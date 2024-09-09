from flask import Flask
from routes.views import app as views_app

app = Flask(__name__)

# Registrar las rutas desde el módulo 'views'
app.register_blueprint(views_app)

if __name__ == '__main__':
    app.run(debug=True)

