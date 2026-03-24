<div align="center">

# 🤖 J.A.R.V.I.S
### Just A Rather Very Intelligent System

*A Python-based AI Voice Assistant for Desktop*

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)]()
[![License](https://img.shields.io/badge/License-MIT-green.svg)]()
[![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)]()

</div>

---

## 📌 Overview

**JARVIS** is a Python-based intelligent voice assistant that listens to your voice commands and performs a wide range of tasks — from searching the web and fetching Wikipedia summaries to controlling system apps and telling jokes. Inspired by Tony Stark's AI assistant, JARVIS is built for real productivity on your desktop.

> 🎓 This project was built as part of academic research at [Your Institution], focusing on improving upon existing open-source voice assistant implementations.

---

## ✨ Features

| Category | Commands |
|---|---|
| 🌐 **Web** | Google Search, YouTube, Wikipedia summary, News |
| 💻 **System** | Open apps, Volume control, Battery status, Screenshots |
| 🕐 **Info** | Time, Date, Weather, Jokes, Calculations |
| 📁 **Productivity** | Notes, Reminders, File operations |

### What makes JARVIS different from other Python assistants?

- ✅ **25+ voice commands** (most similar projects support only 5–10)
- ✅ **Robust error handling** — gracefully recovers from mic failures, API errors, ambiguous queries
- ✅ **Time-based greeting** — Good Morning / Afternoon / Evening
- ✅ **Wikipedia summaries** — returns 2-sentence summaries, not full articles
- ✅ **Cross-platform** — works on Windows, macOS, and Linux
- ✅ **No crashes on Wikipedia disambiguation** — handled with spoken feedback

---

## 🖥️ Demo

```
JARVIS: Good Morning! I am Jarvis, Sir. Please tell me how may I help you.

You: "Search Wikipedia for Artificial Intelligence"
JARVIS: "Searching Wikipedia... According to Wikipedia: Artificial Intelligence is
         the simulation of human intelligence processes by computer systems..."

You: "Open YouTube"
JARVIS: "Opening YouTube"

You: "What time is it?"
JARVIS: "Sir, the time is 10:45 AM"

You: "Tell me a joke"
JARVIS: "Why do programmers prefer dark mode? Because light attracts bugs!"
```

---

## 🛠️ Installation

### Prerequisites

- Python 3.8 or higher
- Microphone (built-in or external)
- Internet connection (for speech recognition and web commands)

### Step 1: Clone the Repository

```bash
git clone https://github.com/VedantKudalkar21/JARVIS.git
cd JARVIS
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run JARVIS

```bash
python jarvis.py
```

---

## 📦 Dependencies

```
SpeechRecognition==3.10.0
pyttsx3==2.90
wikipedia==1.4.0
requests==2.28.0
pyjokes==0.6.0
pyaudio==0.2.13
wolframalpha==5.0.0     # optional, for calculations
```

> 💡 **Note for Windows users:** If `pyaudio` fails to install, download the `.whl` from [Unofficial Python Binaries](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) and install manually.

---

## 🗂️ Project Structure

```
JARVIS/
│
├── jarvis.py               # Main entry point
├── requirements.txt        # Python dependencies
├── README.md               # This file
│
├── modules/
│   ├── speak.py            # TTS engine
│   ├── listen.py           # Speech recognition
│   ├── greet.py            # Time-based greeting
│   └── commands/
│       ├── web_commands.py
│       ├── system_commands.py
│       ├── info_commands.py
│       └── utility_commands.py
│
└── assets/
    └── voice_config.json   # TTS settings
```

---

## 💬 Supported Commands

### 🌐 Web
| Say This | Action |
|---|---|
| "Search Google for [topic]" | Opens Google search |
| "Open YouTube" | Opens YouTube |
| "Wikipedia [topic]" | Reads 2-sentence summary |
| "Show me the news" | Opens news site |

### 💻 System
| Say This | Action |
|---|---|
| "Open Notepad / Chrome / VLC" | Launches application |
| "Take a screenshot" | Captures and saves screen |
| "Battery status" | Reports battery percentage |
| "Shutdown / Restart" | System power commands |

### ℹ️ Information
| Say This | Action |
|---|---|
| "What time is it?" | Speaks current time |
| "What's today's date?" | Speaks current date |
| "Tell me a joke" | Random programming joke |

---

## ⚙️ Configuration

You can customize JARVIS in `jarvis.py`:

```python
# Change TTS voice
engine.setProperty('voice', voices[1].id)  # 0 = Male, 1 = Female

# Change speech rate
engine.setProperty('rate', 180)  # Default: 190

# Change recognition language
query = r.recognize_google(audio, language='en-in')  # en-us, hi-in, etc.
```

---

## 🔬 Research & Academic Context

This project was developed as part of academic research comparing Python-based voice assistant implementations. It addresses drawbacks found in 5 prior works including:

- Brittle error handling (crashes on unexpected input)
- Limited command sets (≤10 commands in most prior work)
- Non-summarized Wikipedia responses
- Windows-only compatibility

📄 See [IEEE Research Paper](./IEEE_Research_Paper_JARVIS.md) for full details.
📋 See [Literature Survey](./literature_survey_drawbacks.md) for prior work analysis.

---

## 🚀 Future Enhancements

- [ ] GUI interface using Tkinter or PyQt5
- [ ] Offline speech recognition using Whisper
- [ ] BERT-based NLU for better intent classification
- [ ] Hindi/Marathi language support
- [ ] Smart home / IoT integration
- [ ] Custom wake word ("Hey JARVIS")

---

## 👨‍💻 Author

**Vedant Kudalkar**
- GitHub: [@VedantKudalkar21](https://github.com/VedantKudalkar21)
- Project: [JARVIS](https://github.com/VedantKudalkar21/JARVIS)

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

<div align="center">
⭐ If you found this project useful, please give it a star!
</div>
