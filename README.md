# 🪔 TheGeetaWay

<div align="center">

**Your Path to Ancient Wisdom** — AI-powered Bhagavad Gita guidance portal

[![Live Demo](https://img.shields.io/badge/🌐_Live_Demo-thegeetaway.streamlit.app-FF4B4B?style=for-the-badge)](https://thegeetaway.streamlit.app)

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat-square&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-009688?style=flat-square&logo=fastapi&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-LLM-orange?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

<img src="https://img.shields.io/badge/🕉️_Bhagavad_Gita-Ancient_Wisdom_Meets_AI-gold?style=for-the-badge" alt="Bhagavad Gita"/>

</div>

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🔍 **Semantic Search** | Find relevant verses using natural language queries |
| 🤖 **AI Guidance** | Personalized wisdom powered by Groq LLM (Llama 3) |
| 🎧 **Sanskrit Audio** | Listen to authentic verse recitations from IIT Kanpur |
| 🌌 **Cosmic UI** | Immersive starfield interface with smooth animations |
| 📖 **700 Verses** | Complete Bhagavad Gita with translations & meanings |
| 🎨 **Theme Selection** | Choose between Spiritual, Philosophical, or Practical guidance |

---

## 🚀 Live Demo

👉 **[https://thegeetaway.streamlit.app](https://thegeetaway.streamlit.app)**

<div align="center">
<i>Ask your life questions and receive wisdom from the Bhagavad Gita</i>
</div>

---

## 🛠️ Tech Stack

```
┌─────────────────────────────────────────────────────────┐
│                    TheGeetaWay                          │
├─────────────────────────────────────────────────────────┤
│  Frontend     │  Streamlit (Cosmic Theme UI)            │
│  Backend      │  FastAPI (REST API)                     │
│  Vector DB    │  FAISS (Semantic Search)                │
│  Embeddings   │  Sentence-Transformers (MiniLM-L6)      │
│  LLM          │  Groq (Llama 3 - 70B)                   │
│  Hosting      │  Streamlit Cloud + Railway              │
└─────────────────────────────────────────────────────────┘
```

---

## 📦 Installation

### Prerequisites
- Python 3.9+
- [Groq API Key](https://console.groq.com/)

### Local Setup

```bash
# Clone the repository
git clone https://github.com/BlackJack-14/TheGeetaWay.git
cd TheGeetaWay

# Install dependencies
pip install -r requirements.txt

# Configure environment
python generate_api_key.py --update-env
# Add your GROQ_API_KEY to .env file

# Start the backend
uvicorn api:app --reload --port 8000

# In another terminal, start the frontend
streamlit run app.py
```

---

## 🔧 Environment Variables

| Variable | Description |
|----------|-------------|
| `GROQ_API_KEY` | Your Groq API key for LLM |
| `API_KEY` | Generated API key for backend auth |
| `API_BASE_URL` | Backend URL (default: `http://localhost:8000`) |

---

## 📁 Project Structure

```
TheGeetaWay/
├── app.py                 # Streamlit frontend
├── api.py                 # FastAPI backend
├── embeddings/
│   ├── buildFaissIndex.py # Build FAISS index
│   └── query_faiss.py     # Semantic search
├── reasoning/
│   └── llm_reasoning.py   # Groq LLM integration
├── faiss_index/
│   ├── gita.index         # FAISS vector index
│   └── metadata.json      # Verse metadata
├── data/
│   └── gita_clean.json    # Cleaned Gita dataset
└── .streamlit/
    └── config.toml        # Streamlit theme config
```

---

## 🙏 Acknowledgments

- [**Gita Supersite, IIT Kanpur**](https://gitasupersite.iitk.ac.in/) — Sanskrit audio recitations
- [**Groq**](https://groq.com/) — Lightning-fast LLM inference
- [**Sentence-Transformers**](https://www.sbert.net/) — Semantic embeddings

---

## 📄 License

This project is licensed under the **MIT License** — see [LICENSE](LICENSE) for details.

---

<div align="center">

### 🙏 श्रीमद्भगवद्गीता

*"Whenever there is a decline in righteousness and an increase in unrighteousness,*  
*O Arjuna, at that time I manifest Myself on earth."*  
— **Bhagavad Gita 4.7**

<br>

**[⭐ Star this repo](https://github.com/BlackJack-14/TheGeetaWay)** if you found it helpful!

</div>
