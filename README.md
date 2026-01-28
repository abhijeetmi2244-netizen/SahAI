#SahAI: Your Local AI Friend 🤖🌾
Breaking Literacy and Language Barriers in Rural Gujarat.
SahAI is a Multimodal Generative AI Agent built by Team Algó Riderz. It is designed specifically for rural populations who face difficulties navigating complex digital documents or educational resources due to language and literacy barriers.
🌟 Core Mission
Traditional technology often acts as a wall for rural users. sahAI turns a smartphone into a bridge by offering a Voice-First, Vision-Guided experience that understands regional dialects (Kathiyawadi) and uses cultural metaphors to explain complex concepts.
🚀 Key Capabilities
Zero-Typing Voice Interface: Built for accessibility; users interact through natural speech in Gujarati/Kathiyawadi.
Multimodal Vision Scanner: Users can point their camera at any document (bank forms, electricity bills, prescriptions), and the AI explains the contents via voice.
Livelihood & Economic Assistant: Simplifies access to government schemes (like PM-Kisan) and provides micro-guides for vocational skills in local languages.
Interactive Subject Tutor: Democratizes STEM education by explaining subjects like HTML or Physics using metaphors grounded in village life.
Real-Time Awareness: Unlike static models, sahAI is aware of the current date and time to provide contextually accurate assistance.
🛠️ Tech Stack
Core AI: Google Gemini 1.5 Flash (optimized for multimodal latency).
UI Framework: Streamlit (customized with CSS for a professional dark-themed dashboard).
Vision: OpenCV & PIL for real-time camera capture and image processing.
Audio:
STT: SpeechRecognition library for Gujarati audio processing.
TTS: gTTS (Google Text-to-Speech) for natural Gujarati voice output.
Audio Management: pygame for seamless background audio playback.
📋 Features & Implementation Highlights
Natural Speech Layer: Implemented a custom NLP cleaning layer to remove symbols (like asterisks or bullet points) from AI responses, ensuring the voice output sounds human and empathetic.
Resilience Logic: Integrated automatic retry logic to handle API rate limits (429 Quota errors) during high-demand periods.
Persistent Session State: Utilizes Streamlit session state to manage chat history and vision feedback across interactions.
