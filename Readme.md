# Spiritual Intent Classifier (Krishna Persona)

## Tech Stack & Choices
- **Frontend:** Streamlit + ElevenLabs Web SDK (WebRTC). Chosen for high-performance audio handling.
- **Brain (LLM):** Gemini 1.5 Flash (via ElevenLabs). Chosen for <350ms reasoning latency.
- **Mouth (TTS):** Eleven Flash v2.5. Chosen for its record-breaking 75ms generation time.

## Latency Breakdown (< 1s Total)
- **STT (Ear):** ~150ms (Internal ElevenLabs transcription).
- **LLM (Brain):** ~300ms (Gemini Flash Time-to-First-Token).
- **TTS (Mouth):** ~100ms (Eleven Flash v2.5 streaming).
- **Network/VAD:** ~200ms.
- **Total:** ~750ms (Meets <1s requirement).

## Dashboard Setup
1. **System Prompt:** Define Krishna's role and the 5 intent categories.
2. **Language:** Set to "Multilingual" for Hinglish support.
3. **Voice:** Selected 'Krishna – Spiritual Books Voice' (ID: F4AXgTwG8nWPB9dcXaTh).