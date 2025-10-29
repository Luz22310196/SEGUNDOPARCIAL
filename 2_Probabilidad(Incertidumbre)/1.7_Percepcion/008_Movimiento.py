import cv2

# Captura de video
cap = cv2.VideoCapture('video.mp4')

# Leer primer frame
ret, frame1 = cap.read()
prev_gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

while True:
    ret, frame2 = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    
    # Diferencia absoluta entre frames
    diff = cv2.absdiff(prev_gray, gray)
    
    # Umbral para resaltar movimiento
    _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
    
    # Mostrar resultado
    cv2.imshow('Movimiento', thresh)
    
    prev_gray = gray
    if cv2.waitKey(30) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
