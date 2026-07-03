import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000"

st.title("📄 RAG Q&A App")

# ----------------- १. फाईल अपलोड सेक्शन -----------------
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    if st.button("Upload to Backend"):
        files = {"file": (uploaded_file.name, uploaded_file.getvalue(), "application/pdf")}
        try:
            response = requests.post(f"{BACKEND_URL}/upload", files=files)
            if response.status_code == 200:
                st.success("फाईल यशस्वीरित्या अपलोड झाली आहे! 👍")
                st.json(response.json())
            else:
                st.error(f"सर््हर एरर: {response.status_code}")
        except requests.exceptions.ConnectionError:
            st.error("आधी FastAPI चा सर्व्हर सुरू करा!")

# --- येथे एक लाईन (Divider) टाकूया जेणेकरून दोन सेक्शन वेगळे दिसतील ---
st.markdown("---")

# ----------------- २. प्रश्न विचारण्याचा सेक्शन -----------------
# 💡 लक्षात ठेव: हा कोड फाईल अपलोडच्या 'if' कंडिशनच्या बाहेर (स्वतंत्र) असायला हवा
st.subheader("🤖 डॉक्युमेंटला प्रश्न विचारा")
question = st.text_input("तुमचा प्रश्न इथे टाईप करा:")

if st.button("Submit"):
    if question.strip() == "":
        st.warning("कृपया आधी काहीतरी प्रश्न टाईप करा!")
    else:
        with st.spinner("उत्तर शोधत आहे..."):
            try:
                # बॅकएंडच्या /ask एंडपॉईंटला रिक्वेस्ट पाठवा
                response = requests.post(f"{BACKEND_URL}/ask", json={"question": question})
                
                if response.status_code == 200:
                    answer = response.json().get("answer", "उत्तर मिळाले नाही.")
                    st.write("### 📝 उत्तर:")
                    st.info(answer)
                else:
                    st.error(f"बॅकएंड एरर: {response.status_code}")
            except requests.exceptions.ConnectionError:
                st.error("FastAPI सर्व्हरशी संपर्क होऊ शकला नाही!")