from ultralytics import YOLO
import cv2
import requests
import time

# ------------------ Telegram Setup ------------------
BOT_TOKEN = "your BotID"
CHAT_ID = "CHATID"

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    response = requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": text
    })
    print("Message status:", response.status_code)

def send_telegram_photo(photo_path):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    with open(photo_path, "rb") as photo:
        response = requests.post(url, files={"photo": photo}, data={
            "chat_id": CHAT_ID
        })
    print("Photo status:", response.status_code)

# ------------------ YOLO Setup ------------------
model = YOLO("yolov8n.pt")
cap = cv2.VideoCapture(0)

last_alert_time = 0
cooldown = 60   # 🔥 reduce to 60 sec for testing

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)
    human_detected = False

    for r in results:
        for box in r.boxes:
            cls_id = int(box.cls[0])
            confidence = float(box.conf[0])

            if model.names[cls_id] == "person" and confidence > 0.6:
                human_detected = True

                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)
                cv2.putText(frame, f"Human {confidence:.2f}",
                            (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6,
                            (0, 255, 0),
                            2)

    # ------------------ ALERT ------------------
    current_time = time.time()

    if human_detected and (current_time - last_alert_time > cooldown):
        print("🚨 Human detected! Sending alert...")

        image_path = "snapshot.jpg"
        cv2.imwrite(image_path, frame)

        send_telegram_message("🚨 ALERT: Human detected!")
        send_telegram_photo(image_path)

        last_alert_time = current_time

    cv2.imshow("Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()