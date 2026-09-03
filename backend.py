import os
import json
from PIL import Image
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables (supports local .env and Streamlit secrets)
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if api_key:
    genai.configure(api_key=api_key)

def get_triage_assessment(symptom_text, uploaded_image=None):
    """
    Sends symptom text and an optional uploaded image to the Gemini API 
    and returns a structured JSON triage assessment.
    """
    system_instruction = (
        "You are a supportive, clinical decision-support AI assistant. "
        "Analyze the user's symptoms and optional uploaded injury/condition image conservatively. "
        "Return ONLY a valid JSON object with the following exact keys: "
        "'summary' (string), "
        "'urgency_level' (Low, Medium, High, Emergency), "
        "'recommended_department' (string), "
        "'rationale' (string), and "
        "'first_aid_steps' (a list of strings). "
        "Never give a definitive diagnosis; frame findings as possibilities and prioritize user safety."
    )
    
    generation_config = {
        "temperature": 0.2, # Low temperature for analytical consistency
        "response_mime_type": "application/json",
    }

    model = genai.GenerativeModel(
        model_name="gemini-2.5-flash",
        system_instruction=system_instruction,
        generation_config=generation_config
    )

    # Build the multi-modal content payload
    contents = []
    
    if symptom_text:
        contents.append(f"Patient symptom details: {symptom_text}")
    else:
        contents.append("Patient symptom details: No text provided, analyze the attached image.")

    if uploaded_image is not None:
        try:
            img = Image.open(uploaded_image)
            contents.append(img)
        except Exception as img_error:
            return {"error": f"Failed to process uploaded image: {str(img_error)}"}

    try:
        response = model.generate_content(contents)
        return json.loads(response.text)
    except Exception as e:
        return {"error": str(e)}
