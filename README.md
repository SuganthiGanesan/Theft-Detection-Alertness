# 🚨 AI-Based Theft Detection & Alert System

An intelligent real-time theft detection system built using YOLOv8 and OpenCV that detects human presence in restricted areas and sends instant Telegram alerts with image evidence.

---

## 📌 Features

- 🕵️ **Real-time human detection** for theft monitoring
- 📹 **Live video processing** using webcam/CCTV
- 📲 **Instant Telegram alerts** on suspicious activity
- 📸 **Automatic snapshot capture** and sharing
- ⏱️ **Cooldown mechanism** to prevent repeated alerts

---

## 🛠️ Technologies Used

- **Python** - Core programming language
- **YOLOv8 (Ultralytics)** - Object detection model
- **OpenCV** - Computer vision library
- **Telegram Bot API** - Alert notifications
- **Requests** - HTTP library for API calls

---

## 🤖 Telegram Bot Setup

Follow these steps to set up your Telegram bot:

1. Open Telegram and search for **BotFather**
2. Create a new bot using the `/newbot` command
3. Copy your `BOT_TOKEN`
4. Start your bot and send a message (e.g., "hi")
5. Open this URL in your browser:
   ```
   https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates
   ```
6. Copy your `CHAT_ID` from the response

---

## ⚙️ Installation

### Prerequisites

Make sure you have Python 3.8+ installed on your system.

### Install Dependencies

```bash
pip install ultralytics opencv-python requests
```

---

## 🔧 Configuration

Add your Telegram credentials in the code:

```python
BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"
```

---

## ▶️ Usage

Run the project with:

```bash
python app.py
```

The system will start monitoring through your webcam/CCTV feed and send alerts when human presence is detected.

---

## 📸 Output

✅ Detects human presence in real-time  
✅ Sends instant alert message to Telegram  
✅ Sends captured snapshot as evidence

---

## 💡 Use Cases

- 🏠 **Home security systems**
- 🏢 **Office surveillance**
- 🏬 **Shop theft detection**
- 🚫 **Restricted area monitoring**

---

## 🚀 How It Works

1. **Video Capture**: Captures live feed from webcam/CCTV
2. **Detection**: YOLOv8 model detects human presence in frames
3. **Alert Trigger**: When a person is detected, the system triggers an alert
4. **Notification**: Sends image snapshot + alert message via Telegram
5. **Cooldown**: Prevents spam by implementing a cooldown period

---

## 📋 Project Structure

```
theft-detection-system/
│
├── app.py                 # Main application file
├── README.md              # Project documentation
└── requirements.txt       # Python dependencies (optional)
```

---

## 🔒 Security Notes

- Keep your `BOT_TOKEN` and `CHAT_ID` confidential
- Do not commit credentials to public repositories
- Consider using environment variables for sensitive data

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👩‍💻 Author

**Suganthi Ganesan**

---

## 🙏 Acknowledgments

- YOLOv8 by Ultralytics
- OpenCV community
- Telegram Bot API

---

⭐ **If you find this project helpful, please give it a star!** ⭐
