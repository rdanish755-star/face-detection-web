import cv2

# 1. Load the pre-trained face detection model (XML file)
# Make sure this file is in the same folder as your script!
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# 2. Start the Webcam (0 is usually the default camera)
cap = cv2.VideoCapture(0)

print("Press 'q' to exit the program")

while True:
    # 3. Capture frame-by-frame
    ret, frame = cap.read()

    # 4. Convert frame to Grayscale (Computer B&W mein jaldi process karta hai)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 5. Detect faces
    # scaleFactor: Kitna image resize ho (1.1 is standard)
    # minNeighbors: Kitne rectangles pass hon tab face consider ho (5 is good)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    # 6. Draw a rectangle around the faces and count them
    for (x, y, w, h) in faces:
        # Drawing a Green rectangle (BGR format: 0, 255, 0)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
        
        # Display "Face Detected" text
        cv2.putText(frame, 'Face Found', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    # 7. Show the count on screen
    cv2.putText(frame, f'Faces: {len(faces)}', (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # 8. Display the resulting frame
    cv2.imshow('AI Face Detection Project', frame)

    # 9. Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 10. Clean up
cap.release()
cv2.destroyAllWindows()

# 1. Load the pre-trained face detection model (XML file)
# Make sure this file is in the same folder as your script!
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# 2. Start the Webcam (0 is usually the default camera)
cap = cv2.VideoCapture(0)

print("Press 'q' to exit the program")

while True:
    # 3. Capture frame-by-frame
    ret, frame = cap.read()

    # 4. Convert frame to Grayscale (Computer B&W mein jaldi process karta hai)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 5. Detect faces
    # scaleFactor: Kitna image resize ho (1.1 is standard)
    # minNeighbors: Kitne rectangles pass hon tab face consider ho (5 is good)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    # 6. Draw a rectangle around the faces and count them
    for (x, y, w, h) in faces:
        # Drawing a Green rectangle (BGR format: 0, 255, 0)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
        
        # Display "Face Detected" text
        cv2.putText(frame, 'Face Found', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    # 7. Show the count on screen
    cv2.putText(frame, f'Faces: {len(faces)}', (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # 8. Display the resulting frame
    cv2.imshow('AI Face Detection Project', frame)

    # 9. Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 10. Clean up
cap.release()
cv2.destroyAllWindows()
