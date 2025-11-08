from groq import Groq

# Replace with your Groq API key
client = Groq(api_key="YOUR_GROQ_API_KEY")

def ask_groq(question):
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": question}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"⚠️ Error: {e}"

# Test it
question = "Explain how open-source and proprietary APIs differ in simple terms."
print("Groq Response:\n", ask_groq(question))
