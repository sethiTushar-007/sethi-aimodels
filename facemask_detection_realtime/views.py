from django.shortcuts import render,redirect
from tensorflow.keras.models import load_model
import cv2
import numpy as np
# Create your views here.
model = load_model('./models/face_mask.h5')
results = {0:'without mask', 1:'mask'}
GR_dict = {0:(0,0,255), 1:(0,255,0)}
def facemask_detection_realtime(request):
    rect_size = 4
    cap = cv2.VideoCapture(0)
    haarcascade = cv2.CascadeClassifier('./models/haarcascade_frontalface_default.xml')

    while True:
        (rval, im) = cap.read()
        im = cv2.flip(im, 1, 1)
        rerect_size = cv2.resize(im, (im.shape[1] // rect_size, im.shape[0] // rect_size))
        faces = haarcascade.detectMultiScale(rerect_size)
        for f in faces:
            (x, y, w, h) = [v * rect_size for v in f]
        
            face_img = im[y:y+h, x:x+w]
            rerect_sized = cv2.resize(face_img, (150, 150))
            normalized = rerect_sized / 255.0
            reshaped = np.reshape(normalized, (1,150,150,3))
            reshaped = np.vstack([reshaped])
            result = model.predict(reshaped)
        
            label = np.argmax(result, axis=1)[0]
        
            cv2.rectangle(im, (x,y), (x+w, y+w), GR_dict[label],2)
            cv2.rectangle(im, (x,y-40), (x+w,y), GR_dict[label], -1)
            cv2.putText(im, results[label], (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)
        cv2.imshow('LIVE', im)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    return redirect('../')