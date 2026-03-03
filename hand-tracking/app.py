import cv2
import mediapipe as mp

# inicializar MediaPipe
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# webcam
cap = cv2.VideoCapture(0)

print("Programa iniciado. Coloque a/s mão/s na frente da webcam.")
print("Pressione ESC para sair")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    # espelha imagem
    frame = cv2.flip(frame, 1)

    # converte para RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(frame_rgb)

    # processa deteccao
    if results.multi_hand_landmarks:
        for hand_landmarks, handedness in zip(
            results.multi_hand_landmarks,
            results.multi_handedness
        ):

            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            dedos = []
            landmarks = hand_landmarks.landmark

            # identifica se é mão direita ou esquerda
            label = handedness.classification[0].label

            # POLEGAR 
            if label == "Right":
                dedos.append(landmarks[4].x < landmarks[3].x)
            else:  # Left
                dedos.append(landmarks[4].x > landmarks[3].x)

            # outros dedos
            dedos.append(landmarks[8].y < landmarks[6].y)
            dedos.append(landmarks[12].y < landmarks[10].y)
            dedos.append(landmarks[16].y < landmarks[14].y)
            dedos.append(landmarks[20].y < landmarks[18].y)

            total_dedos = sum(dedos)

            cv2.putText(
                frame,
                f"Dedos levantados: {total_dedos}",
                (10, 70),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

    cv2.imshow("Gestos", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()