# 🎙️ Sound Recording & Speech Recognition

A Python audio processing pipeline that records sound, applies a 
band-pass filter for noise reduction, and converts speech to text.

---

## ⚙️ How It Works

1. **Record** — Captures 5 seconds of audio via microphone (16kHz, mono)
2. **Filter** — Applies a Butterworth band-pass filter to reduce noise
3. **Visualize** — Plots original vs filtered audio signal
4. **Transcribe** — Converts filtered audio to text using Google Speech API

---

## ✨ Features
- Real-time audio recording
- Band-pass filtering (Butterworth, order 4)
- Signal visualization with Matplotlib
- Speech-to-text transcription (English)

---

## 🛠️ Technologies Used
- Python
- PyAudio
- SciPy
- NumPy
- Matplotlib
- SpeechRecognition (Google API)

---

## ⚙️ Installation

```bash
git clone https://github.com/rana-alaa-abdelaziz/sound-recording.git
cd sound-recording
pip install pyaudio numpy scipy matplotlib SpeechRecognition
python main.py
```

---

##  Author
**Rana Alaa Abdelaziz**
[GitHub](https://github.com/rana-alaa-abdelaziz)
