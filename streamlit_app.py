import streamlit as st
import joblib
import os
import time

# --- CONFIGURATION ---
st.set_page_config(
    page_title="Chroma | Digital Atelier",
    page_icon="🎨",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- CUSTOM CSS (The "Chroma" Vibe) ---
# We inject your specific fonts and colors to override Streamlit's default look
st.markdown("""
    <style>
        /* Import Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600&family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,400;1,600&family=Outfit:wght@200..600&display=swap');

        /* Background */
        .stApp {
            background: linear-gradient(135deg, #f0ebe0 0%, #dcd3c9 100%);
        }

        /* Typography */
        h1 {
            font-family: 'Cinzel', serif !important;
            font-size: 4rem !important;
            text-align: center;
            color: #1a1a1a;
            margin-bottom: 0px !important;
            text-shadow: 2px 2px 0px rgba(0,0,0,0.05);
        }
        
        .subtitle {
            font-family: 'Cormorant Garamond', serif;
            font-size: 1.8rem;
            text-align: center;
            font-style: italic;
            color: #66605b;
            margin-bottom: 3rem;
        }

        /* Input Field Styling */
        .stTextInput input {
            font-family: 'Cormorant Garamond', serif !important;
            font-size: 1.5rem !important;
            text-align: center;
            background-color: transparent !important;
            border: none !important;
            border-bottom: 2px solid #1a1a1a !important;
            color: #1a1a1a !important;
        }
        .stTextInput input:focus {
            box-shadow: none !important;
            border-bottom: 2px solid #c5a059 !important;
        }
        
        /* Hide default Streamlit elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Palette Display */
        .color-card {
            height: 250px;
            border-radius: 4px;
            display: flex;
            align-items: flex-end;
            justify-content: center;
            padding-bottom: 20px;
            transition: transform 0.3s ease;
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        }
        .color-card:hover {
            transform: translateY(-10px) scale(1.02);
            z-index: 10;
        }
        .hex-text {
            background: rgba(255,255,255,0.9);
            padding: 5px 10px;
            border-radius: 20px;
            font-family: 'Outfit', sans-serif;
            font-size: 0.8rem;
            color: #1a1a1a;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# --- MODEL LOADING ---
@st.cache_resource
def load_model():
    # Path to your artifacts
    model_path = os.path.join('ml_engine', 'artifacts', 'palette_model.pkl')
    
    if not os.path.exists(model_path):
        # If model doesn't exist, we might need to train it on the fly (for cloud deployment)
        # But ideally, you push the trained model or run training in build
        return None
        
    try:
        return joblib.load(model_path)
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

def predict_palette(model_artifact, text_input):
    if not model_artifact:
        return []
    
    vectorizer = model_artifact['vectorizer']
    nn_model = model_artifact['model']
    database_colors = model_artifact['data']

    input_vector = vectorizer.transform([text_input])
    distances, indices = nn_model.kneighbors(input_vector)
    
    best_match_index = indices[0][0]
    prediction = database_colors[best_match_index]
    
    colors = []
    for i in range(0, 15, 3):
        r = int(prediction[i])
        g = int(prediction[i+1])
        b = int(prediction[i+2])
        hex_code = '#{:02x}{:02x}{:02x}'.format(r, g, b)
        colors.append(hex_code)
    return colors

# --- MAIN APP LOGIC ---

# 1. Header
st.markdown("<h1>CHROMA STUDIO</h1>", unsafe_allow_html=True)
st.markdown('<p class="subtitle">The Muse</p>', unsafe_allow_html=True)

# 2. Load Brain
model = load_model()

# 3. Input
query = st.text_input("", placeholder="Describe your dream...")

# 4. Button & Action
if st.button("Ignite Imagination", type="primary", use_container_width=True):
    if not query:
        st.warning("Please whisper a vision to the Muse first...")
    elif not model:
        st.error("The Muse is sleeping (Model file not found). Please train the model first!")
    else:
        # Cinematic Loader
        with st.spinner("Mixing colors..."):
            time.sleep(1.0) # Aesthetic delay
            colors = predict_palette(model, query)
        
        # Display Palette
        st.markdown("---")
        cols = st.columns(5)
        
        for i, color in enumerate(colors):
            with cols[i]:
                # We use HTML/CSS to render the colored blocks because Streamlit's native tools are limited
                st.markdown(f"""
                    <div class="color-card" style="background-color: {color};">
                        <div class="hex-text">{color}</div>
                    </div>
                """, unsafe_allow_html=True)