import sounddevice as sd
import scipy.io.wavfile as wav
import numpy as np
import speech_recognition as sr

print("Recording...")
fs = 44100  
duration = 5 
recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
sd.wait()
print("Recording saved.")

wav.write("output.wav", fs, recording)

r = sr.Recognizer()
with sr.AudioFile("output.wav") as source:
    audio = r.record(source)
    try:
        
        result = r.recognize_google(audio, language="hi-IN", show_all=True)
        if result and "alternative" in result:
            
            text = result["alternative"][0]["transcript"]
            print("you:", text)
        else:
            print("no sound")
    except sr.UnknownValueError:
        print("unknown error")
    except sr.RequestError as e:
        print(f"ఫలితాలను అభ్యర్థించలేకపోయింది: {e}")
