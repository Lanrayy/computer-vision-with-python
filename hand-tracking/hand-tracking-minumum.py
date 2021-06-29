# this file contains the bare minimum code required to run hand tracking
import cv2
import mediapipe as mp
import time  # for frame rate

# check frame rate
cap = cv2.VideoCapture(0)

# formality before you can start using the module
mpHands = mp.solutions.hands
# The hands function- false indicates tracking should only take place above a certain confidence
# 2 is the maximum number of hands and the 0.5's are the minimum detection confidence and minimum tracking confidence
hands = mpHands.Hands(False, 2, 0.5, 0.5)

# the provided method that allows us to draw the points on the hand
mpDraw = mp.solutions.drawing_utils

# Running a webcam
while True:
    success, img = cap.read()
    # covert out image into RGB
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    # check if we have something in the results
    # We need to know if something is detected or not
    print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        # For each hand extract the information of each hand
        for handLandMarks in results.multi_hand_landmarks:
            # Draw the points on the hand
            mpDraw.draw_landmarks(img, handLandMarks)



    # check if we have multiple hands

    cv2.imshow("Image", img)
    cv2.waitKey(1)