import cv2
import os
import face_recognition
import numpy as np

def capture_image():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        cv2.imshow('Press "C" to capture image', frame)

        if cv2.waitKey(1) & 0xFF == ord('c'):
            cv2.imwrite('captured_image.jpg', frame)
            break

    cap.release()
    cv2.destroyAllWindows()

def encode_image(image_path):
    image = face_recognition.load_image_file(image_path)
    encodings = face_recognition.face_encodings(image)

    if len(encodings) > 0:
        return encodings[0]
    else:
        return None

def compare_encodings(encoding, encodings_folder):
    for filename in os.listdir(encodings_folder):
        try:
            known_encodings = np.load(os.path.join(encodings_folder, filename))
            matches = face_recognition.compare_faces(known_encodings, encoding)

            if any(matches):
                return filename[:-4]  # Remove file extension

        except Exception as e:
            print(f"Error loading {filename}: {e}")

    return None

def main():
    encodings_folder = 'encodings'
    encodingsbd_folder = 'encodingsdb'

    while True:
        capture_image()
        encoding = encode_image('captured_image.jpg')

        if encoding is not None:
            np.save(os.path.join(encodings_folder, 'current_encoding.npy'), encoding)
            match = compare_encodings(encoding, encodingsbd_folder)

            if match:
                print(f"Match found: {match}")

                # Display the name on the camera window if the 'c' key is pressed
                cap = cv2.VideoCapture(0)
                while True:
                    ret, frame = cap.read()
                    cv2.putText(frame, match, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    cv2.imshow('Match found', frame)

                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                cap.release()
                cv2.destroyAllWindows()
            else:
                print("No matches")

        else:
            print("No face detected in the captured image")

        # Exit the loop if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if __name__ == '__main__':
    main()