import random
import pandas as pd
from ml_engine.config import COLORS, THEMES

def generate_synthetic_data(num_samples=6000):
    data = []

    for _ in range(num_samples):
        theme = random.choice(THEMES)
        
        # 1. Generate varied descriptions
        desc_len = random.randint(2, 4)
        # Sort keywords to ensure consistency (e.g., "ocean blue" == "blue ocean")
        keywords = sorted(random.sample(theme["keywords"], desc_len))
        description = " ".join(keywords)
        
        # 2. Deterministic RNG
        rng = random.Random(description)
        
        # 3. Pick colors
        if len(theme["pool"]) >= 5:
            palette_keys = rng.sample(theme["pool"], 5)
        else:
            palette_keys = rng.choices(theme["pool"], k=5)
        
        # 4. Sort by Brightness (Luminance)
        # Ensures [Darkest ... Lightest] order
        def get_brightness(key):
            r, g, b = COLORS[key]
            return (r * 299 + g * 587 + b * 114) / 1000

        palette_keys.sort(key=get_brightness)

        flat_palette = []
        for key in palette_keys:
            r, g, b = COLORS[key]
            flat_palette.extend([r, g, b])
            
        row = {'input_text': description}
        for i, val in enumerate(flat_palette):
            row[f'color_{i}'] = val
            
        data.append(row)

    return pd.DataFrame(data)