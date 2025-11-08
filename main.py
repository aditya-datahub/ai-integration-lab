from gemini_chat import ask_gemini
from groq_chat import ask_groq

question = "Explain how AI works in simple terms."
print("Gemini Response:", ask_gemini(question))
print("Groq Response:", ask_groq(question))
