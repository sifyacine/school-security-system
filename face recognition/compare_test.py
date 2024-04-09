import face_recognition
import numpy as np

# Load the face encodings from two files
encoding_file_1 = "encodingsdb/yacine sif.npy"
encoding_file_2 = "encodingsdb/captured_encoding.npy"

encoding_1 = np.load(encoding_file_1)
encoding_2 = np.load(encoding_file_2)

# Compare the two face encodings with a tolerance of 0.4
matches = face_recognition.compare_faces([encoding_1], encoding_2, tolerance=0.3)

if np.any(matches):
    print("The two face encodings match.")
else:
    print("The two face encodings do not match.")