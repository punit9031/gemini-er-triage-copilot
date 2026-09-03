# gemini-er-triage-copilot# 🚑 Multimodal ER Triage & Visual First-Aid Copilot

A lightweight emergency room pre-triage and health-tech prototype built using **Python**, **Streamlit**, and the **Gemini API** (`gemini-2.5-flash`). Designed for high school hackathons and Hack Club workshops to demonstrate safe, multimodal clinical AI applications.

---

## 🚀 Features
* **Multimodal Analysis:** Ingests user-submitted images (e.g., cuts, burns, rashes) alongside natural language symptom descriptions.
* **Structured Clinical Outputs:** Forces the Gemini model to return strict JSON mapping out urgency levels, suggested medical departments, and first-aid instructions.
* **Built-in Safety Guardrails:** Programmed with system instructions and low temperature settings to prevent definitive medical diagnoses and safely guide users toward professional medical care.

---

## 🛠️ Tech Stack
* **Frontend/UI:** Streamlit
* **AI Engine:** Google GenAI SDK (`google-generativeai`)
* **Data Interchange:** Native Python `json` parsing

---

## ⚙️ Quick Start (Local Setup)

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/gemini-er-triage-copilot.git](https://github.com/your-username/gemini-er-triage-copilot.git)
   cd gemini-er-triage-copilot
