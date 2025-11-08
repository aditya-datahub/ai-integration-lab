import google.generativeai as genai

# Replace with your API key
genai.configure(api_key="YOUR_GEMINI_API_KEY")

def ask_gemini(question):
    try:
        model = genai.GenerativeModel("gemini-2.0-flash") 
        response = model.generate_content(question)
        return response.text
    except Exception as e:
        return f"⚠️ Error: {e}"

# Test it
question = "Explain how AI works in simple terms."
print("Gemini Response:\n", ask_gemini(question))
