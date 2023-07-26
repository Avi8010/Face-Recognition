import cv2
import face_recognition
from simple_facerec import SimpleFacerec

#Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("Test/")
# img = cv2.imread("Messi.jpg")
# rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
# img_encoding = face_recognition.face_encodings(rgb_img)[0]

img2 = cv2.imread(r"C:\Users\dell\Desktop\face detector\new.jpg")
half = cv2.resize(img2, (0,0), fx = 0.5, fy = 0.5) 
rgb_img2 = cv2.cvtColor(half, cv2.COLOR_BGR2RGB) 
img_encoding2 = face_recognition.face_encodings(rgb_img2)[0]

result = face_recognition.compare_faces([img_encoding2], img_encoding2)
print("Result: ", result)

# cv2.imshow("Img", img)
cv2.imshow("Img 2", half)
# cv2.waitKey(0)