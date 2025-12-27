import streamlit as st
import os
from dotenv import load_dotenv

# Load credentials
load_dotenv()
AGENT_ID = os.getenv("AGENT_ID")

# --- UI STYLING ---
st.set_page_config(page_title="Krishna: Spiritual Companion", page_icon="🪔")
st.title("🪔 Speak to Krishna")
st.subheader("Your Voice-First Spiritual Guide")

st.markdown("""
    **Mission:** Share your thoughts. Krishna will classify your intent and guide you.
    * **Intents:** Career, Relationships, Inner Conflict, Life Transitions, Daily Struggles.
    * **Languages:** English, Hindi, or Hinglish.
""")

if not AGENT_ID:
    st.error("Error: AGENT_ID not found. Please check your .env file.")
else:

    widget_html = f"""
    <div style="display: flex; justify-content: center; padding: 20px;">
        <elevenlabs-convai agent-id="{AGENT_ID}"></elevenlabs-convai>
    </div>
    <script src="https://elevenlabs.io/convai-widget/index.js" async type="text/javascript"></script>
    """
    st.components.v1.html(widget_html, height=500)

st.divider()
st.caption("Built for AI Engineering Case Study. Powered by ElevenLabs & Streamlit.")