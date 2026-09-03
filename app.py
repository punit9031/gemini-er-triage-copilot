import streamlit as st
from backend import get_triage_assessment

st.set_page_config(
    page_title="ER Triage & First-Aid Copilot",
    page_icon="🚑",
    layout="centered"
)

st.title("🚑 Multimodal ER Triage & First-Aid Copilot")
st.markdown("Upload a photo of an injury or physical condition alongside your symptoms to receive a preliminary triage assessment and safety guidelines.")

# Form layout for user inputs
with st.form("triage_form"):
    symptom_input = st.text_area(
        "Describe your symptoms:",
        placeholder="e.g., 3 days of persistent dry cough, mild fatigue, and low-grade fever..."
    )
    
    uploaded_image = st.file_uploader(
        "Upload an image (optional - e.g., cut, rash, burn):",
        type=["jpg", "jpeg", "png"]
    )
    
    submitted = st.form_submit_button("Analyze Symptoms & Image")

if submitted:
    if not symptom_input and not uploaded_image:
        st.warning("Please provide either a description of your symptoms or upload an image.")
    else:
        with st.spinner("Analyzing clinical data patterns..."):
            # Call backend function
            result = get_triage_assessment(symptom_input, uploaded_image)
            
            if "error" in result:
                st.error(f"An error occurred: {result['error']}")
            else:
                st.subheader("Assessment Summary")
                st.write(result.get("summary", "No summary provided."))
                
                col1, col2 = st.columns(2)
                with col1:
                    st.metric(label="Urgency Level", value=result.get("urgency_level", "Unknown"))
                with col2:
                    st.metric(label="Suggested Department", value=result.get("recommended_department", "Unknown"))
                    
                st.info(f"**Clinical Rationale:** {result.get('rationale', 'N/A')}")
                
                if "first_aid_steps" in result:
                    st.markdown("### Recommended First-Aid Steps")
                    for idx, step in enumerate(result.get("first_aid_steps", []), 1):
                        st.write(f"{idx}. {step}")
                        
                st.warning("⚠️ **Disclaimer:** This tool is an engineering prototype for educational/demonstration purposes and does not replace professional medical diagnosis. If you are experiencing a life-threatening emergency, call local emergency services immediately.")
