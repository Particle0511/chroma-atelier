from flask import jsonify, request, render_template
from backend.app.api import bp
from backend.app.core.predictor import PalettePredictor

@bp.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@bp.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    if not data or 'query' not in data:
        return jsonify({'error': 'No query provided'}), 400

    user_input = data['query']
    predictor = PalettePredictor()
    colors = predictor.predict(user_input)

    if not colors:
        return jsonify({'error': 'Model error'}), 500

    return jsonify({'colors': colors})