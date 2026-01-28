import os
import cv2
import re
import time
import pygame
from datetime import datetime
import google.generativeai as genai
from dotenv import load_dotenv
import speech_recognition as sr
from gtts import gTTS
from PIL import Image

# INITIALIZATION
load_dotenv()
# Ensure your .env has GEMINI_API_KEY=your_key_here
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-2.5-flash') 

SAHAI_IDENTITY = """
You are sahAI, a local friend for rural Gujarat. 
RULES: 
- Use simple Gujarati or Kathiyawadi. 
- DO NOT use or pronounce symbols like *, #, or bullets. 
- Use short sentences.
- Use farming or village metaphors for tech/education topics.
"""

def clean_text_for_speech(text):
    """Removes special characters for natural voice output."""
    clean = re.sub(r'[*#_~-]', '', text)
    clean = clean.replace("•", ". ")
    return clean

def call_gemini_with_retry(content_list, max_retries=3):
    """Handles temporary quota errors with a simple retry."""
    for i in range(max_retries):
        try:
            response = model.generate_content(content_list)
            return response.text if response.text else "No response."
        except Exception as e:
            if "429" in str(e):
                time.sleep(3) # Wait for quota to breathe
                continue
            return f"Error: {str(e)}"
    return "Limit reached. Please wait a minute or check your key."

def speak(text):
    """Clean Voice Output."""
    try:
        if not text: return
        speech_ready_text = clean_text_for_speech(text)
        tts = gTTS(text=speech_ready_text, lang='gu')
        filename = f"s_{int(time.time())}.mp3"
        tts.save(filename)
        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()
    except Exception as e: 
        print(f"Audio Error: {e}")

def capture_and_scan():
    """Vision Logic."""
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    if ret:
        img_path = "scan.jpg"
        cv2.imwrite(img_path, frame)
        cam.release()
        img = Image.open(img_path)
        res_text = call_gemini_with_retry([SAHAI_IDENTITY, "Explain this in Gujarati.", img])
        speak(res_text)
        return res_text
    cam.release()
    return "Camera error."

def process_text_query(user_text):
    """Injects Real-Time awareness (Date/Time)."""
    now = datetime.now().strftime("%A, %B %d, %I:%M %p")
    full_prompt = f"{SAHAI_IDENTITY}\nReal-time context: {now}\nUser: {user_text}"
    res_text = call_gemini_with_retry([full_prompt])
    speak(res_text)
    return {"user": user_text, "ai": res_text}

def run_sahai_voice():
    """Voice-to-Text Logic."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.4)
        try:
            audio = recognizer.listen(source, timeout=5)
            user_input = recognizer.recognize_google(audio, language='gu-IN')
            return process_text_query(user_input)
        except: 
            return {"user": "Error", "ai": "Please speak again clearly."}