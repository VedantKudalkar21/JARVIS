import google.generativeai as genai

# Configure Gemini API (Replace with your actual API key)
API_KEY = "AIzaSyBLF0LzV86rienyeGoQBzHyKN_RhvzEwJk"
genai.configure(api_key=API_KEY)

# AI Processing Function
def aiProcess(command):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")  # Use latest fast model
        response = model.generate_content(command)
        return response.text  # Return generated text

    except Exception as e:
        return f"Error: {str(e)}"

# Example usage in JARVIS
command = "Tell me a joke about AI."
response = aiProcess(command)
print(response)  # JARVIS can use this output for speech
