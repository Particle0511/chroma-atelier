import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARTIFACTS_DIR = os.path.join(BASE_DIR, 'artifacts')
MODEL_PATH = os.path.join(ARTIFACTS_DIR, 'palette_model.pkl')

RANDOM_SEED = 42
TEST_SIZE = 0.1

MODEL_PARAMS = {
    'hidden_layer_sizes': (256, 128, 64),
    'activation': 'relu',
    'solver': 'adam',
    'max_iter': 1500,
    'random_state': RANDOM_SEED
}


THEMES = [
    
    {
        "keywords": ["ocean", "sea", "water", "beach", "blue", "cool", "calm", "sky", "marine", "waves", "deep", "aqua", "turquoise", "pacific", "ice", "winter", "frozen", "pool", "rain"],
        "pool": ['navy', 'blue', 'sky', 'teal', 'cyan', 'azure', 'cerulean', 'ice_blue', 'white']
    },
   
    {
        "keywords": ["forest", "nature", "green", "plants", "organic", "eco", "jungle", "garden", "leaf", "pine", "moss", "fern", "spring", "herbal", "mint", "wild", "hiking", "aloe", "sage"],
        "pool": ['forest', 'green', 'lime', 'emerald', 'moss', 'olive', 'sage', 'brown', 'tan']
    },
    
    {
        "keywords": ["fire", "hot", "red", "passion", "energy", "warm", "sunset", "spicy", "danger", "heat", "flame", "summer", "orange", "burning", "intense", "lava", "volcano"],
        "pool": ['red', 'dark_red', 'orange', 'crimson', 'rust', 'coral', 'yellow', 'black']
    },
    
    {
        "keywords": ["sun", "sunshine", "yellow", "bright", "happy", "morning", "citrus", "lemon", "daisy", "corn", "cheese", "smile", "optimistic", "light", "day", "summer"],
        "pool": ['yellow', 'gold', 'cream', 'orange', 'white', 'lime']
    },
   
    {
        "keywords": ["dark", "black", "night", "midnight", "shadow", "obsidian", "charcoal", "gray", "grey", "slate", "ash", "dim", "gloom", "mystery", "ink", "oil", "batman"],
        "pool": ['black', 'gray', 'charcoal', 'slate', 'navy', 'dark_red']
    },
    
    {
        "keywords": ["contrast", "eclipse", "silhouette", "bold", "impact", "alert", "warning", "bumblebee", "industrial"],
        "pool": ['black', 'yellow', 'gold', 'white', 'charcoal']
    },
    
    {
        "keywords": ["neon", "cyberpunk", "tech", "laser", "hacker", "glitch", "rave", "party", "synthetic", "fluorescent", "vaporwave", "miami", "disco"],
        "pool": ['neon_pink', 'electric_blue', 'magenta', 'acid_green', 'cyan', 'purple']
    },
    
    {
        "keywords": ["coffee", "cafe", "brown", "wood", "earth", "vintage", "chocolate", "rustic", "latte", "espresso", "mocha", "leather", "cardboard", "dirt", "mud", "bear"],
        "pool": ['coffee', 'brown', 'tan', 'beige', 'caramel', 'chocolate', 'sienna', 'cream']
    },
    
    {
        "keywords": ["luxury", "royal", "gold", "expensive", "elegant", "premium", "wealth", "wedding", "jewelry", "vip", "king", "queen", "crown", "silk", "velvet"],
        "pool": ['gold', 'purple', 'black', 'silver', 'champagne', 'burgundy']
    },
    
    {
        "keywords": ["flower", "floral", "pink", "rose", "love", "valentine", "blossom", "petal", "bouquet", "romantic", "sweet", "candy", "baby", "pastel", "soft"],
        "pool": ['pink', 'lavender', 'coral', 'peach', 'cream', 'white', 'magenta']
    },
    
    {
        "keywords": ["minimal", "clean", "white", "simple", "scandinavian", "pure", "airy", "zen", "paper", "blank", "empty", "modern", "hospital"],
        "pool": ['white', 'off_white', 'cloud', 'mist', 'gray', 'silver']
    },
    
    {
        "keywords": ["royal", "majestic", "regal", "imperial", "jewel", "gem", "sapphire", "amethyst", "deep", "magic", "wizard"],
        "pool": ['purple', 'navy', 'gold', 'emerald', 'burgundy']
    }
]

COLORS = {
    
    'red': (255, 0, 0), 'dark_red': (139, 0, 0), 'crimson': (220, 20, 60),
    'pink': (255, 192, 203), 'neon_pink': (255, 20, 147), 'magenta': (255, 0, 255),
    'coral': (255, 127, 80), 'peach': (255, 218, 185), 'burgundy': (128, 0, 32),
    
    
    'orange': (255, 165, 0), 'rust': (183, 65, 14), 'gold': (255, 215, 0),
    'yellow': (255, 255, 0), 'cream': (255, 253, 208), 'champagne': (247, 231, 206),
    'caramel': (198, 142, 23),
    
    
    'green': (0, 128, 0), 'lime': (50, 205, 50), 'acid_green': (176, 255, 20),
    'forest': (34, 139, 34), 'emerald': (80, 200, 120), 'moss': (138, 154, 91),
    'olive': (128, 128, 0), 'sage': (188, 184, 138),
    
    
    'blue': (0, 0, 255), 'navy': (0, 0, 128), 'sky': (135, 206, 235),
    'electric_blue': (125, 249, 255), 'ice_blue': (173, 216, 230),
    'azure': (0, 127, 255), 'cerulean': (0, 123, 167), 'teal': (0, 128, 128),
    'cyan': (0, 255, 255), 'foam': (212, 241, 249),
    
    
    'purple': (128, 0, 128), 'lavender': (230, 230, 250),
    
   
    'white': (255, 255, 255), 'off_white': (250, 250, 245),
    'black': (0, 0, 0), 'gray': (128, 128, 128), 'charcoal': (54, 69, 79),
    'slate': (112, 128, 144), 'silver': (192, 192, 192), 'mist': (224, 224, 224),
    'ash': (178, 190, 181), 'cloud': (236, 240, 241),
    
    
    'brown': (165, 42, 42), 'coffee': (111, 78, 55), 'chocolate': (210, 105, 30),
    'sienna': (160, 82, 45), 'tan': (210, 180, 140), 'beige': (245, 245, 220)
}