import os
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
from ml_engine.config import ARTIFACTS_DIR, MODEL_PATH
from ml_engine.dataset_generator import generate_synthetic_data

def train_model():
    print("--- Building Search Engine ---")
    
    if not os.path.exists(ARTIFACTS_DIR):
        os.makedirs(ARTIFACTS_DIR)

    # 1. Generate MASSIVE Database (20,000 samples)
    print("1. Generating Palette Database (20,000 samples)...")
    df = generate_synthetic_data(num_samples=20000)
    
    text_data = df['input_text']
    # Grab only the color columns to store as the "Answer Key"
    color_cols = [c for c in df.columns if c.startswith('color_')]
    palette_data = df[color_cols].values

    # 2. Vectorize Text (Convert words to semantic numbers)
    print("2. Vectorizing Descriptions...")
    vectorizer = TfidfVectorizer(ngram_range=(1, 2), stop_words='english')
    text_vectors = vectorizer.fit_transform(text_data)

    # 3. Build Search Engine (Cosine Similarity)
    print("3. Indexing Data...")
    nn_model = NearestNeighbors(
        n_neighbors=1, 
        algorithm='brute', 
        metric='cosine'
    )
    nn_model.fit(text_vectors)

    # 4. Save Everything as a Bundle
    artifact = {
        'vectorizer': vectorizer,
        'model': nn_model,
        'data': palette_data
    }

    print("4. Saving Search Engine...")
    joblib.dump(artifact, MODEL_PATH)
    print(f"Done! Search Engine saved to: {MODEL_PATH}")

if __name__ == "__main__":
    train_model()