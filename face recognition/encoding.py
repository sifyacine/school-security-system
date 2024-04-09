import face_recognition
import numpy as np
import os
import tkinter as tk
from tkinter import filedialog, simpledialog
import cv2


# Define a function to capture an image from the webcam
def capture_image():
    # Open the webcam
    cap = cv2.VideoCapture(0)

    # Initialize variables
    face_detected = False
    image_path = "image.jpg"

    while not face_detected:
        # Capture a single frame from the webcam
        ret, frame = cap.read()

        # Find the face locations
        face_locations = face_recognition.face_locations(frame)

        # Check if a face was detected
        if len(face_locations) > 0:
            # Save the image to a file
            cv2.imwrite(image_path, frame)

            # Set the flag to exit the loop
            face_detected = True

    # Release the webcam
    cap.release()

    # Get the name of the person in the image
    name = simpledialog.askstring("Name", "Enter the name of the person in the image:")

    # Encode the image
    encode_image(image_path, name)
# Define a function to select an image file using a file dialog
def select_image():
    # Show the file dialog
    file_path = filedialog.askopenfilename()

    # Get the name of the person in the image
    name = simpledialog.askstring("Name", "Enter the name of the person in the image:")

    # Encode the image
    encode_image(file_path, name)

# Define a function to encode a single image
def encode_image(image_path, name):
    # Load the image
    image = face_recognition.load_image_file(image_path)

    # Find the face locations
    face_locations = face_recognition.face_locations(image)

    # Encode the faces
    face_encodings = face_recognition.face_encodings(image, face_locations)

    # Check if any faces were found
    if len(face_encodings) == 0:
        print("No faces found in image for {}".format(name))
        return

    # Add the face encodings and name to the lists
    known_face_encodings.append(face_encodings[0])
    known_face_names.append(name)

    # Save the encodings and names to files
    np.save("encodingsdb/{}.npy".format(name), face_encodings)
    with open("names/names.txt", "a") as f:
        f.write(name + "\n")

    print("Encoded image for {}".format(name))

# Create a list to store the face encodings and names
known_face_encodings = []
known_face_names = []

# Create a Tkinter window
window = tk.Tk()
window.title("Face Encoding")

# Create a button to capture an image from the webcam
capture_button = tk.Button(window, text="Capture Image", command=capture_image)
capture_button.pack()

# Create a button to select an image file
select_button = tk.Button(window, text="Select Image", command=select_image)
select_button.pack()

# Start the main loop
window.mainloop()

# Save the face encodings and names to files
np.save("encodingsdb/encodings.npy", known_face_encodings)
with open("names/names.txt", "w") as f:
    for name in known_face_names:
        f.write(name + "\n")

print("Finished encoding images.")