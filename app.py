from flask import Flask,request,jsonify
from mtcnn.mtcnn import MTCNN
import cv2
import numpy as np
from PIL import Image,ImageOps

app= Flask(__name__)


def resize_sunglasses(left_eye,right_eye,sunglasses):
    dx = right_eye[0] - left_eye[0]
    dy = right_eye[1] - left_eye[1]
    #angle = np.degrees(np.arctan2(dx,dy))-180
    eye_width = np.sqrt(dx**2 + dy**2)
    scale = eye_width/ sunglasses.width *3
    new_size = (int(sunglasses.width*scale), int(sunglasses.height*scale))
    resized_sunglasses = sunglasses.resize(new_size, Image.LANCZOS)
   # rotated_sunglasses = resized_sunglasses.rotate(angle,expand=True)
    return resized_sunglasses
    

@app.route('/process-image',methods=['POST'])
def process_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400
    file =request.files['image']
    image  = Image.open(file.stream)
    image = np.array(image)
    updated_image  = coolify(image)
    cv2.imwrite('updated_image.jpg',updated_image)
    return jsonify({'message':'Imgage processed successfully'}),200


def coolify(image):
    detector =MTCNN()
    detections =detector.detect_faces(image)
    pil_image =Image.fromarray(image).convert("RGBA")
    sunglasses_path ='sunglasses.png'
    sunglasses = Image.open(sunglasses_path).convert("RGBA")
    if detections:
        for  face in detections:
            print("Face bounding box", face['box'])
            (x,y,h,w)= face['box']
            face_region= image[y:y+h,x:x+h]
            blurred_face =cv2.GaussianBlur(face_region,(15,15),0)
            image[y:y+h,x:x+h] = blurred_face
            pil_image = Image.fromarray(image).convert("RGBA")
            keypoints = face['keypoints']
            left_eye = face['keypoints']['left_eye']
            right_eye = face['keypoints']['right_eye']
            resized_rotated_sunglasses = resize_sunglasses(left_eye,right_eye,sunglasses)
            eye_center = ((left_eye[0]+right_eye[0])//2,(left_eye[1]+right_eye[1])//2)
            sunglasses_position = (eye_center[0]- resized_rotated_sunglasses.width//2,eye_center[1]-resized_rotated_sunglasses.height//2)
            sunglasses_mask = resized_rotated_sunglasses.split()[-1]
            pil_image.paste(resized_rotated_sunglasses,sunglasses_position,sunglasses_mask)
    return np.array(pil_image)



if __name__ == '__main__':
    app.run(debug=True)







