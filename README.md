# 🚨 AI-Based Theft Detection & Alert System

An intelligent real-time theft detection system built using YOLOv8 and OpenCV that detects human presence in restricted areas and sends instant Telegram alerts with image evidence.

---

## 📌 Features
- 🕵️ Real-time human detection for theft monitoring  
- 📹 Live video processing using webcam/CCTV  
- 📲 Instant Telegram alerts on suspicious activity  
- 📸 Automatic snapshot capture and sharing  
- ⏱️ Cooldown mechanism to prevent repeated alerts  

---

## 🛠️ Technologies Used
- Python  
- YOLOv8 (Ultralytics)  
- OpenCV  
- Telegram Bot API  
- Requests  

---

##🤖 Telegram Bot Setup
1.Open Telegram and search for BotFather
2.Create a new bot using /newbot
3.Copy your BOT_TOKEN
4.Start your bot and send a message (hi)
5.Open in browser:https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates
6.Copy your CHAT_ID

## ▶️ Usage

1. Add your credentials in the code:

```python
BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

### Run the project:
```bash
python app.py

## 📸 Output
- Detects human presence in real-time  
- Sends instant alert message to Telegram  
- Sends captured snapshot as evidence  

---

## 💡 Use Cases
- 🏠 Home security systems  
- 🏢 Office surveillance  
- 🏬 Shop theft detection  
- 🚫 Restricted area monitoring

## 👩‍💻 Author
**Suganthi Ganesan**

