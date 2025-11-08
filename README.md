# 🧠 AI Integration Lab
**Integration of Google Gemini and Groq (Llama) models for AI text generation and comparison using Python.**

---

## 🚀 Overview
This project demonstrates how to connect and interact with two powerful AI models — **Google Gemini** and **Groq (Llama-3)** — using Python.  
It’s designed as a simple lab to explore **multi-model integration**, **prompt testing**, and **AI response comparison** for learning or analytical purposes.

---

## 🧰 Tech Stack
- 🐍 **Python 3.10+**
- 🤖 **Google Generative AI SDK** (`google-generativeai`)
- ⚡ **Groq SDK** (`groq`)
  
---

## ⚙️ Features
- 🧩 Connects with **Gemini API** using `google-generativeai`  
- ⚡ Interacts with **Groq API** using the `groq` SDK  
- 💬 Handles question–answer prompts and text generation  
- 🧠 Helps compare output style, speed, and quality between models  

---

## 📁 Project Structure
```
ai-integration-lab/
│
├── gemini_chat.py      # Script to interact with Google Gemini
├── groq_chat.py        # Script to interact with Groq (Llama)
├── main.py             # Runs both models for comparison
└── README.md           # Project overview and usage guide
```
---

## 🧰 Installation
1. **Clone this repo**
   ```bash
   git clone https://github.com/yourusername/ai-integration-lab.git
   cd ai-integration-lab

2. Install dependencies
   ```
   pip install google-generativeai groq
   
3. Add your API keys
Replace inside code:
```
genai.configure(api_key="YOUR_GEMINI_API_KEY")
client = Groq(api_key="YOUR_GROQ_API_KEY")
```
---

## 💡 Usage Example

```bash
from gemini_chat import ask_gemini
from groq_chat import ask_groq

question = "Explain how AI works in simple terms."
print("Gemini Response:", ask_gemini(question))
print("Groq Response:", ask_groq(question))
```
---

## 🧩 Sample Output
Gemini Response: AI works by analyzing data and recognizing patterns to make predictions or generate text.
Groq Response: Artificial Intelligence processes information and learns from examples to solve problems automatically.

---

## 🎯 Purpose
This project was created as a hands-on experiment to explore how different AI models — Google Gemini and Groq (Llama) — respond to the same prompt.  
It helps compare response quality, reasoning, and performance between models, making it a great mini-project for learning **AI model integration**, **API handling**, and **text generation**.

---
