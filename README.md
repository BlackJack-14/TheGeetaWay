# 🪔 TheGeetaWay

**Your Path to Ancient Wisdom** — AI-powered Bhagavad Gita guidance portal.

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)

## Features

- 🔍 Semantic search for relevant Gita verses
- 🤖 AI-powered personalized guidance (Groq LLM)
- 🎧 Sanskrit audio recitation
- 🌌 Beautiful cosmic UI

## Tech Stack

| Component | Technology     |
| --------- | -------------- |
| Frontend  | Streamlit      |
| Backend   | FastAPI        |
| Vector DB | FAISS          |
| LLM       | Groq (Llama 3) |

## Quick Start

```bash
# Clone repo
git clone https://github.com/YOUR_USERNAME/TheGeetaWay.git
cd TheGeetaWay

# Install
pip install -r requirements.txt

# Configure
python generate_api_key.py --update-env
# Add GROQ_API_KEY to .env

# Run
uvicorn api:app --reload
streamlit run app.py
```

## License

MIT License - see [LICENSE](LICENSE)

## Acknowledgments

- [Gita Supersite, IIT Kanpur](https://gitasupersite.iitk.ac.in/) for audio
- Groq for fast LLM inference

---

<p align="center"><i>श्रीमद्भगवद्गीता — The Song of the Divine</i></p>
