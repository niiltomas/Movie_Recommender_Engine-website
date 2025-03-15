from flask import Flask, jsonify, send_from_directory
import os
from flask_cors import CORS  # Permet les peticions CORS (Cross-Origin Resource Sharing)

app = Flask(__name__)

# Permetre totes les peticions CORS
CORS(app)


@app.route('/api/movies')
def get_movies():
    json_file_path = 'movies_weighted.json'

    if os.path.exists(json_file_path):
        return send_from_directory('.', json_file_path)
    else:
        return jsonify({'error': 'No se pudo encontrar el archivo JSON'}), 404


# Ruta per servir arxius estàtics (si tens altres fitxers com imatges, CSS, JS)
@app.route('/static/<path:filename>')
def serve_static_file(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    app.run(debug=True)
