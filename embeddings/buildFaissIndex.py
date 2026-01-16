import json
import os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

DATA_PATH = "../data/bhagavad_gita_clean_final.json"
INDEX_DIR = "../faiss_index"
INDEX_PATH = os.path.join(INDEX_DIR, "gita.index")
META_PATH = os.path.join(INDEX_DIR, "metadata.json")

os.makedirs(INDEX_DIR, exist_ok=True)

print("🔹 Loading embedding model...")
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

print("🔹 Loading cleaned dataset...")
with open(DATA_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

def get_verse_themes(english_text):
    """Extract semantic themes from verse content"""
    text_lower = english_text.lower()
    themes = []
    
    # Fear and anxiety
    if any(word in text_lower for word in ['fear', 'afraid', 'anxiety', 'worry', 'dread', 'terror']):
        themes.append("overcoming fear and anxiety")
    
    # Confusion and clarity
    if any(word in text_lower for word in ['confus', 'doubt', 'uncertain', 'perplex', 'bewilder']):
        themes.append("finding clarity in confusion")
    
    # Action and duty
    if any(word in text_lower for word in ['duty', 'action', 'work', 'perform', 'karma', 'deed']):
        themes.append("understanding duty and action")
    
    # Mind control
    if any(word in text_lower for word in ['mind', 'thought', 'control', 'focus', 'concentrate']):
        themes.append("mastering the mind")
    
    # Peace and calm
    if any(word in text_lower for word in ['peace', 'calm', 'tranquil', 'serene', 'equanim']):
        themes.append("achieving inner peace")
    
    # Detachment
    if any(word in text_lower for word in ['detach', 'renounce', 'abandon', 'relinquish', 'let go']):
        themes.append("practicing detachment")
    
    # Desire and attachment
    if any(word in text_lower for word in ['desire', 'attach', 'crav', 'long for', 'passion']):
        themes.append("managing desires and attachments")
    
    # Wisdom and knowledge
    if any(word in text_lower for word in ['wisdom', 'knowledge', 'understand', 'realize', 'enlighten']):
        themes.append("gaining wisdom and understanding")
    
    # Strength and courage
    if any(word in text_lower for word in ['strength', 'courage', 'brave', 'valor', 'fortitude']):
        themes.append("building strength and courage")
    
    # Future and destiny
    if any(word in text_lower for word in ['future', 'destiny', 'fate', 'path', 'journey']):
        themes.append("navigating life's path")
    
    # Death and impermanence
    if any(word in text_lower for word in ['death', 'die', 'mortal', 'imperien', 'transitory']):
        themes.append("accepting impermanence")
    
    # Self and identity
    if any(word in text_lower for word in ['self', 'soul', 'atman', 'true nature', 'essence']):
        themes.append("understanding true self")
    
    return themes

def is_practical_verse(english_text):
    """Check if verse gives practical life guidance vs mythological/cosmic context"""
    text_lower = english_text.lower()
    
    # Avoid overly cosmic/mythological verses
    cosmic_keywords = [
        'cosmic form', 'divine form', 'universes', 'celestial', 
        'thousand arms', 'blazing', 'effulgence', 'deity',
        'creation and dissolution', 'brahma', 'vishnu'
    ]
    
    if any(keyword in text_lower for keyword in cosmic_keywords):
        return False
    
    # Prefer actionable guidance
    practical_keywords = [
        'should', 'must', 'one who', 'therefore', 'thus',
        'perform', 'control', 'practice', 'abandon', 'cultivate'
    ]
    
    return any(keyword in text_lower for keyword in practical_keywords)

texts = []
metadata_list = []

print("🔹 Creating enhanced embeddings...")

for v in data:
    # Get themes for this verse
    themes = get_verse_themes(v['english'])
    theme_text = " ".join(themes) if themes else "spiritual wisdom and guidance"
    
    # Check if verse is practical
    practicality_boost = ""
    if is_practical_verse(v['english']):
        practicality_boost = "Practical life advice. Real-world application. "
    
    # Create enriched text for embedding
    # The key is to add context that matches user queries
    enriched_text = f"""
    {practicality_boost}
    Life guidance about: {theme_text}.
    Verse teaching: {v['english']}
    Keywords: confusion, fear, anxiety, clarity, action, duty, peace, strength, future, path
    """.strip()
    
    texts.append(enriched_text)
    metadata_list.append({
        "id": v["id"],
        "chapter": v["chapter"],
        "verse": v["verse"],
        "sanskrit": v["sanskrit"],
        "english": v["english"],
        "themes": themes,  # Store themes in metadata
        "is_practical": is_practical_verse(v['english'])
    })

print(f"🔹 Encoding {len(texts)} verses...")
embeddings = model.encode(
    texts,
    convert_to_numpy=True,
    normalize_embeddings=True,
    show_progress_bar=True
)

dimension = embeddings.shape[1]

print("🔹 Building FAISS index (cosine similarity)...")
index = faiss.IndexFlatIP(dimension)  # Inner Product for cosine similarity
index.add(embeddings)

print("🔹 Saving FAISS index...")
faiss.write_index(index, INDEX_PATH)

print("🔹 Saving enhanced metadata...")
with open(META_PATH, "w", encoding="utf-8") as f:
    json.dump(metadata_list, f, ensure_ascii=False, indent=2)

print(f"✅ Enhanced FAISS index built with {index.ntotal} vectors")
print("✅ Metadata now includes themes and practicality flags")