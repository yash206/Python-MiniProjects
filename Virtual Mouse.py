import cv2
import mediapipe as mp
import pyautogui
cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_height, screen_width = 900, 1500
index_y = 0
pyautogui.FAILSAFE = False
while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for num, landmark in enumerate(landmarks):
                x = int(landmark.x*frame_width)
                y = int(landmark.y*frame_height)
                if num == 8:
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    index_x = screen_width/frame_width*x
                    index_y = screen_height/frame_height*y
                    pyautogui.moveTo(index_x, index_y)
                if num == 4:
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    stop_x = screen_width/frame_width*x
                    stop_y = screen_height/frame_height*y
                if num == 12: # or num == 20:
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    click_x = screen_width / frame_width * x
                    click_y = screen_height / frame_height * y
                    if abs(click_y - stop_y) < 30:
                        pyautogui.click()
                        pyautogui.sleep(1)
    cv2.imshow('Mouse', frame)
    cv2.waitKey(1)
