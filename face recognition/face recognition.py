import cv2
import os
import time
import face_recognition
import numpy as np

def compare_encodings(encoding, encodings_folder):
    for filename in os.listdir(encodings_folder):
        try:
            known_encodings = np.load(os.path.join(encodings_folder, filename))
            print(f"Loaded {len(known_encodings)} encodings from {filename}")
            matches = face_recognition.compare_faces(known_encodings, encoding, tolerance=0.6)
            print(f"Matches: {matches}")

            if any(matches):
                return filename[:-4]  # Remove file extension

        except Exception as e:
            print(f"Error loading {filename}: {e}")

    return None

def main():
    encodingsdb_folder = 'encodingsdb'

    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        cv2.imshow('Camera', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        encoding = face_recognition.face_encodings(frame)

        if len(encoding) > 0:
            encoding = encoding[0]
            match = compare_encodings(encoding, encodingsdb_folder)

            if match:
                print(f"Match found: {match}")
                cv2.putText(frame, match, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                cv2.imshow('Camera', frame)
                time.sleep(5)  # Add a 5-second delay
            else:
                print("No matches")

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()