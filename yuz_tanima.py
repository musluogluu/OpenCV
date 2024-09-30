import cv2

# Haar cascade yüz tanıma modelini yükleme
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Kamerayı başlat
cap = cv2.VideoCapture(0)

while True:
    # Kameradan görüntü al
    ret, frame = cap.read()
    
    # Gri tonlamalı görüntüye çevir
    gray = cv2.cvtColor(frame(4096, 2304), cv2.COLOR_BGR2GRAY)
    
    # Yüzleri algıla
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    # Algılanan yüzlerin etrafına dikdörtgen çiz
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    
    # Görüntüyü göster
    cv2.imshow('Yuz Tespiti', frame)
    
    # 'q' tuşuna basılınca çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamera ve pencereleri kapat
cap.release()
cv2.destroyAllWindows()
