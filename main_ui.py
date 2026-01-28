import streamlit as st
import app
import os

st.set_page_config(page_title="sahAI Pro", page_icon="🤖", layout="wide")

# PRO UI STYLING
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { border-radius: 10px; height: 3.5em; background-color: #2E7D32; font-weight: bold; }
    .user-card { background: #1e2130; padding: 15px; border-radius: 10px; border-left: 5px solid #00bcd4; margin-bottom: 5px; }
    .ai-card { background: #262730; padding: 15px; border-radius: 0px 0px 10px 10px; border-left: 5px solid #4CAF50; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

if "history" not in st.session_state:
    st.session_state.history = []

st.title("🤖 sahAI Pro")
st.write("### Empathetic Multimodal AI for Rural Empowerment")

# CORE ACTIONS
c1, c2, c3 = st.columns(3)

with c1:
    if st.button("🎤 Start Voice Assistant"):
        with st.spinner("Listening..."):
            res = app.run_sahai_voice()
            st.session_state.history.insert(0, res)
            st.rerun()

with c2:
    if st.button("📸 Scan Physical Document"):
        with st.spinner("Analyzing Document..."):
            analysis = app.capture_and_scan()
            st.session_state.history.insert(0, {"user": "📷 Scan", "ai": analysis})
            st.rerun()

with c3:
    if st.button("🗑️ Clear Chat History"):
        st.session_state.history = []
        if os.path.exists("scan.jpg"): os.remove("scan.jpg")
        st.rerun()

st.divider()

# LAYOUT: TEXT INPUT & HISTORY
left, right = st.columns([1, 1.5])

with left:
    st.subheader("⌨️ Text Entry (Backup)")
    u_input = st.text_input("Type your question here:", key="user_text_box")
    if st.button("Submit Query"):
        if u_input:
            with st.spinner("Thinking..."):
                res = app.process_text_query(u_input)
                st.session_state.history.insert(0, res)
                st.rerun()
    
    if os.path.exists("scan.jpg"):
        st.image("scan.jpg", caption="Last Document Capture")

with right:
    st.subheader("📜 Recent Conversation")
    if not st.session_state.history:
        st.info("Start an interaction using the buttons above.")
    for chat in st.session_state.history:
        st.markdown(f'<div class="user-card">👤 <b>You:</b> {chat["user"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="ai-card">🤖 <b>sahAI:</b> {chat["ai"]}</div>', unsafe_allow_html=True)