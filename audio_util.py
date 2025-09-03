import pyttsx3

def falar(texto):
    try:
        engine = pyttsx3.init()
        engine.say(texto)
        engine.runAndWait()
    except Exception as e:
        print("Erro ao falar com pyttsx3:", e)
