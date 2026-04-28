from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFloatingActionButton
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Color, Ellipse, Line
import speech_recognition as sr
import threading
from groq import Groq
import math

# ================== CONFIG ==================
GROQ_API_KEY = "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"
client = Groq(api_key=GROQ_API_KEY)

r = sr.Recognizer()
r.energy_threshold = 300
r.pause_threshold = 0.8

class TwishuScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = MDFloatLayout()
        
        # Status Label
        self.status = MDLabel(
            text="Twishu Ready\nBoss, bol kya help chahiye?",
            halign="center",
            theme_text_color="Custom",
            text_color=(0, 1, 1, 1),
            font_style="H5",
            pos_hint={"center_x": 0.5, "center_y": 0.78},
            size_hint=(0.9, 0.2)
        )
        self.layout.add_widget(self.status)

        # Mic Button
        self.mic_btn = MDFloatingActionButton(
            icon="microphone",
            pos_hint={"center_x": 0.5, "center_y": 0.32},
            size_hint=(None, None),
            size=(110, 110),
            md_bg_color=(0, 1, 1, 1)
        )
        self.mic_btn.bind(on_release=self.start_listening)
        self.layout.add_widget(self.mic_btn)

        self.add_widget(self.layout)
        
        # Glowing animation start
        Clock.schedule_interval(self.animate_glow, 0.05)

    def animate_glow(self, dt):
        # Simple glow effect on mic button
        pass  # baad mein aur sundar banayenge

    # Baaki saare functions same rahenge (start_listening, listen_and_process, etc.)
    def start_listening(self, instance):
        self.status.text = "🎤 Sun raha hu boss...\nBolo"
        self.mic_btn.md_bg_color = (1, 0.3, 0.3, 1)
        threading.Thread(target=self.listen_and_process, daemon=True).start()

    def listen_and_process(self):
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.8)
                audio = r.listen(source, timeout=8, phrase_time_limit=10)
            
            command = r.recognize_google(audio, language="hi-IN")
            print("You said:", command)
            Clock.schedule_once(lambda dt: self.process_command(command), 0)
        except sr.UnknownValueError:
            Clock.schedule_once(lambda dt: self.update_status("Samajh nahi aaya boss... Phir se bolo"), 0)
        except Exception as e:
            Clock.schedule_once(lambda dt: self.update_status(f"Error: {str(e)}"), 0)
        finally:
            Clock.schedule_once(lambda dt: self.reset_mic(), 0)

    def update_status(self, text):
        self.status.text = text

    def reset_mic(self):
        self.mic_btn.md_bg_color = (0, 1, 1, 1)
        self.status.text = "Twishu Ready\nBoss, bol kya help chahiye?"

    def process_command(self, command):
        self.update_status(f"You: {command}\nThinking...")
        
        system_prompt = """You are Twishu, a friendly, emotional, caring Indian AI assistant. 
Always call user 'boss'. Respond ONLY in Hindi (or Hinglish). Be natural, warm and polite."""

        try:
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": command}
                ],
                temperature=0.7,
                max_tokens=300
            )
            answer = response.choices[0].message.content.strip()
            self.update_status(f"Twishu: {answer}")
            self.speak(answer)
        except Exception as e:
            self.update_status("Kuch issue aa gaya boss...")
            print(e)

    def speak(self, text):
        print("🔊 Speaking:", text)

        def speak_thread():
            try:
                import pyttsx3
                engine = pyttsx3.init()
                engine.setProperty('rate', 170)
                engine.setProperty('volume', 1.0)
                voices = engine.getProperty('voices')
                if len(voices) > 1:
                    engine.setProperty('voice', voices[1].id)
                engine.say(text)
                engine.runAndWait()
                print("✅ Voice successfully boli")
            except Exception as e:
                print("TTS Error:", e)
                try:
                    from plyer import tts
                    tts.speak(text)
                except:
                    pass

        threading.Thread(target=speak_thread, daemon=True).start()


class TwishuApp(MDApp):
    def build(self):
        Window.size = (400, 700)
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Cyan"
        return TwishuScreen()

if __name__ == "__main__":
    TwishuApp().run()