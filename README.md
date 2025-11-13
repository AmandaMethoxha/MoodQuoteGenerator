# 💡 Mood-Based Quote Generator

A fun, creative Python app that reads how you’re feeling and gives you a matching inspirational quote.  
Built with **Tkinter** for the GUI, **TextBlob** for sentiment analysis, and the **ZenQuotes API** for fresh quotes.

---

## ✨ Features
- 🧠 Detects mood (positive / negative / neutral) from what you type  
- 🌈 Background colour changes with your mood  
- 💬 Shows a relevant quote and author  
- 😄 Adds an emoji that matches your emotion  
- 🖥️ Simple, responsive GUI  

---

## 🧰 Tech
| Tool | Purpose |
|------|----------|
| Python 3.11 | Core language |
| Tkinter | GUI framework |
| TextBlob | Sentiment analysis |
| Requests | API calls |
| ZenQuotes API | Quote source |

---

## ⚙️ Setup

```bash
# 1. Clone this repo
git clone https://github.com/amandamethoxha/MoodQuoteGenerator.git
cd MoodQuoteGenerator

# 2. Create & activate venv
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
# venv\Scripts\activate    # Windows

# 3. Install requirements
pip install requests textblob

# 4. (optional) download TextBlob data
python3 -m textblob.download_corpora

# 5. Run
python3 mood_quote_generator.py
```

---

## 🎨 Mood Colours
| Mood | Colour | Emoji |
|------|---------|-------|
| Positive | Deep Green (#2E8B57) | 😄 |
| Neutral | Charcoal Grey (#3A3A3A) | 😐 |
| Negative | Dark Red (#8B0000) | 😔 |

---

## 🚀 Future Ideas
- Smooth fade animation between quotes  
- Dark-mode toggle 🌙  
- Save favourite quotes locally  
- Streamlit web version  

---

## 🧑‍💻 Author
**Amanda Methoxha**  
📍 United Kingdom  
🎓 Embedded Systems & Computer Science enthusiast  

---

## 📜 License
Released under the **MIT License**.  
You’re free to use, modify, and share this project.

---

⭐ If you like it, drop a star on GitHub!
