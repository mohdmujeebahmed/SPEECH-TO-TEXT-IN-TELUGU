# 🎙️ Speech to Text in Telugu (తెలుగు) using Python

This project captures your voice using a microphone, saves it as a WAV audio file, and then converts it to **Telugu text (తెలుగు)** using the **Google Speech Recognition API**.

---

## 📌 Features

- 🎧 Records audio through your microphone (5 seconds by default)
- 💾 Saves the audio to `output.wav`
- 🌐 Converts spoken Telugu into text using Google's API
- 🚫 Handles errors like unclear audio or internet issues
- 📜 Telugu language transcription output in terminal

---

## 🧰 Requirements

Install the following Python libraries before running the script:

```bash
pip install sounddevice scipy SpeechRecognition
Speech to Text in Telugu (తెలుగు) using Python
This project captures your voice using a microphone, saves it as a WAV audio file, and then converts it to Telugu text (తెలుగు) using the Google Speech Recognition API.

📌 Features
🎧 Records audio through your microphone (5 seconds by default)

💾 Saves the audio to output.wav

🌐 Converts spoken Telugu into text using Google's API

🚫 Handles errors like unclear audio or internet issues

📜 Telugu language transcription output in terminal

🧰 Requirements
Install the following Python libraries before running the script:

bash
Copy
Edit
pip install sounddevice scipy SpeechRecognition
▶️ How to Run
Clone or download the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/speech-to-text-telugu.git
cd speech-to-text-telugu
Run the script:

bash
Copy
Edit
python filename.py
🔊 Speak into your mic in Telugu, and the recognized text will appear in the terminal.

🌐 Language Setting
Make sure to use the Telugu language code in the recognition part:

python
Copy
Edit
r.recognize_google(audio, language="te-IN")
You can change "te-IN" to other languages like:

"en-IN" for English (India)

"hi-IN" for Hindi

"ur-IN" for Urdu

📸 Example Output
text
Copy
Edit
Recording...
Recording saved.
You said: ఐ యామ్ ఏ జీనియస్
<img width="957" alt="image" src="https://github.com/user-attachments/assets/72aabab4-2f9e-49b2-9883-c8e79ab77646" />

📂 File Structure
bash
Copy
Edit
├── filename.py       # Main Python script  
├── output.wav        # Audio file generated after recording  
└── README.md         # This file  
🙌 Acknowledgements
Google Speech Recognition API

Python sounddevice

Scipy for audio file handling

🧠 Notes
Requires an active internet connection for Google API

Works best in a quiet environment

Telugu pronunciation should be clear for accurate results

📬 Contact
For any suggestions or issues, feel free to open an issue or contact me at [mujeebworks7@gmail.com].
