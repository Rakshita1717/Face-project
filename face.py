from deepface import DeepFace
import cv2

# Demo for face recognition using DeepFace

def face_verification_demo():
    """
    Demo function to verify if two faces are of the same person.
    Uses sample images from URLs.
    """
    # URLs of sample images (you can replace with your own image paths)
    img1_url = r"C:\Users\Dell\OneDrive\Desktop\face_project\facerecognation_img1.jpg"
    img2_url = r"C:\Users\Dell\OneDrive\Desktop\face_project\facerecognation_img2.jpeg"

    print("Verifying faces...")
    try:
        result = DeepFace.verify(img1_path=img1_url, img2_path=img2_url)
        print(f"Verification result: {result['verified']}")
        print(f"Distance: {result['distance']:.4f}")
        print(f"Threshold: {result['threshold']:.4f}")
        print(f"Model: {result['model']}")
    except Exception as e:
        print(f"Error during verification: {e}")

def face_detection_demo():
    """
    Demo function to detect faces in an image.
    """
    img_url = "https://upload.wikimedia.org/wikipedia/commons/5/56/Donald_Trump_official_portrait.jpg"

    print("Detecting faces...")
    try:
        faces = DeepFace.extract_faces(img_path=img_url)
        print(f"Number of faces detected: {len(faces)}")
        for i, face in enumerate(faces):
            print(f"Face {i+1}: {face['facial_area']}")
    except Exception as e:
        print(f"Error during face detection: {e}")

if __name__ == "__main__":
    print("DeepFace Face Recognition Demo")
    print("1. Face Verification")
    print("2. Face Detection")
    choice = input("Choose demo (1 or 2): ").strip()

    if choice == "1":
        face_verification_demo()
    elif choice == "2":
        face_detection_demo()
    else:
        print("Invalid choice.")