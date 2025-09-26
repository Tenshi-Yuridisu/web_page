from flask import Flask, request, jsonify
from matematicas import suma, resta, multiplicacion, division

# CORS nos permite recibir peticiones desde nuestro archivo HTML
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Habilitamos CORS para toda la aplicación

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()

    operation = data.get('operation')
    x = data.get('x')
    y = data.get('y')

    if x is None or y is None or operation is None:
        return jsonify({'error': 'Faltan parámetros (operation, x, y)'}), 400

    result = None
    if operation == 'suma':
        result = suma(x, y)
    elif operation == 'resta':
        result = resta(x, y)
    elif operation == 'multiplicacion':
        result = multiplicacion(x, y)
    elif operation == 'division':
        result = division(x, y)
    else:
        return jsonify({'error': 'Operación no válida'}), 400

    return jsonify({'result': result})

if __name__ == '__main__':
    # El servidor se ejecutará en http://127.0.0.1:5000
    app.run(debug=True)