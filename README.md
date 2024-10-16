# Facial Recognition Attendance System using Python

https://github.com/user-attachments/assets/9b3e0ffb-7867-434e-9937-12050a310cf0


This Python script implements a facial recognition attendance system using OpenCV and face_recognition libraries. It captures video input from the webcam, detects faces in real-time, compares them with preloaded images of known individuals, and logs their attendance in a CSV file with the current date.

## Features

- Utilizes OpenCV's `VideoCapture()` function for video input from the webcam.
- Uses face_recognition library to load images of known individuals and encode their facial features.
- Creates a CSV file with the current date to log attendance data.
- Resizes video frames for efficient processing using OpenCV's `cv2.resize()` function.
- Compares detected faces with known faces to recognize individuals.
- Logs attendance data of recognized individuals in the CSV file.

## Getting Started

1. Install the required libraries:
   ```
   pip install opencv-python face-recognition
   
   ```

2. Prepare images of known individuals:
   - Place images of known individuals in the `images` folder.
   - Ensure each image is named appropriately to match the individual's name (e.g., `albert_einstein.jpg`, `isaac_newton.jpg`, etc.).

3. Run the script:
   ```
   python faceDetectionAttendance.py
   
   ```

4. Press the 'q' key to exit the program.

## How it Works

1. The script loads images of known individuals and encodes their facial features using the face_recognition library.
2. It captures video input from the webcam and processes each frame.
3. Faces are detected in each frame and resized for efficient processing.
4. The facial features of detected faces are encoded and compared with the known faces' encodings.
5. If a match is found, the individual's name is displayed on the video feed, and their attendance is logged in the CSV file.
6. The program continues running until the 'q' key is pressed to exit.

## Dependencies

- OpenCV
- face_recognition
