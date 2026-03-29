# 🩺 MedAI — AI Health Assistant
### Mini Project | Flask + Claude LLM + Healthcare AI

---

## 📋 Project Overview
MedAI is an AI-powered health assistant that analyzes patient symptoms using
the Claude LLM (Large Language Model) and provides:
- Possible medical conditions
- Severity assessment (Mild / Moderate / Severe)
- Home remedies & precautions
- Diet tips
- Doctor consultation advice

---

## 🛠️ Tech Stack
| Layer     | Technology            |
|-----------|-----------------------|
| Backend   | Python + Flask        |
| AI / LLM  | Anthropic Claude API  |
| Frontend  | HTML + CSS + JS       |

---

## ⚙️ Setup & Run

### 1. Install dependencies
```bash
pip install flask anthropic
```

### 2. Set your API key
```bash
# Windows
set ANTHROPIC_API_KEY=your_api_key_here

# Mac/Linux
export ANTHROPIC_API_KEY=your_api_key_here
```
> Get free API key at: https://console.anthropic.com

### 3. Run the app
```bash
python app.py
```

### 4. Open browser
```
http://localhost:5000
```

---

## 📁 Project Structure
```
health_assistant/
│
├── app.py              ← Flask backend + Claude API
├── templates/
│   └── index.html      ← Frontend UI
└── README.md
```

---

## 🎯 How It Works
1. User enters symptoms, age, gender
2. Flask sends data to Claude API with a medical prompt
3. Claude returns structured JSON analysis
4. Frontend renders the results beautifully

---

## ⚠️ Disclaimer
For educational purposes only. Not a substitute for professional medical advice.
