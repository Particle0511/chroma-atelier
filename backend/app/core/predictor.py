import joblib
import numpy as np
from flask import current_app

class PalettePredictor:
    def __init__(self):
        self.artifact = None
        self.model_path = current_app.config['MODEL_PATH']
        self._load_model()

    def _load_model(self):
        try:
            self.artifact = joblib.load(self.model_path)
        except FileNotFoundError:
            print(f"Error: Model not found at {self.model_path}")
            self.artifact = None

    def predict(self, text_input):
        if not self.artifact:
            return None

        # Unpack the saved search engine
        vectorizer = self.artifact['vectorizer']
        model = self.artifact['model']
        database_colors = self.artifact['data']

        # 1. Convert user text to numbers
        input_vector = vectorizer.transform([text_input])

        # 2. Find the closest match (Cosine Search)
        distances, indices = model.kneighbors(input_vector)
        
        # 3. Retrieve the actual colors from that row
        best_match_index = indices[0][0]
        prediction = database_colors[best_match_index]
        
        # 4. Format for Frontend
        colors = []
        for i in range(0, 15, 3):
            r = int(prediction[i])
            g = int(prediction[i+1])
            b = int(prediction[i+2])
            hex_code = '#{:02x}{:02x}{:02x}'.format(r, g, b)
            colors.append({
                'rgb': f'rgb({r}, {g}, {b})',
                'hex': hex_code
            })
            
        return colors