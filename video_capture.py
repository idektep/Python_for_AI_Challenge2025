import cv2
import os

# Create a video capture to read frames from the webcam (use 0 for the default camera)
cap = cv2.VideoCapture(__)

# Specify the number of images to capture
num_images = 5

# Create the CaptureImages folder if it doesn't exist
if not os.path.exists('CaptureImages'):
    os.makedirs('CaptureImages')

# Capture and save the specified number of images
for i in range(___):
    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()

        # Display the frame
        cv2.imshow('Camera', ____)

        # Check if the user pressed the 'c' key (ord('__') for the letter 'c')
        if cv2.waitKey(1) == ord('__'):
            # Save the captured image with the index number
            cv2.imwrite(f'CaptureImages/image{i}.jpg', frame)
            print(f"Image {i} saved!")
            break  # Exit the loop after capturing the image

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
