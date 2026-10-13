import cv2
import dlib
import keyboard
import time



# Load the pre-trained model for facial landmark detectionq
predictor_path = "shape_predictor_68_face_landmarks.dat"
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_path)

# Open the webcamqq
cap = cv2.VideoCapture(0)
counter = 0

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = detector(gray)

    # Loop over each detected face
    for face in faces:
        # Get the facial landmarks for the face
        landmarks = predictor(gray, face)

        # Loop over each landmark and draw it on the frame
        for n in range(0, 68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            cv2.circle(frame, (x, y), 2, (255, 0, 0), -1)

    # Show the frame with facial landmarks
    cv2.imshow("Facial Landmarks", frame)
    
    if keyboard.is_pressed('w'):
        # Save the photo
        
        cv2.imwrite("FacialLandmarks" + str(counter) + ".png", frame)
        counter = counter + 1
        time.sleep(1)

    # Exit if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()