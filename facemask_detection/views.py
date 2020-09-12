from django.shortcuts import render
from urllib.request import urlopen
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from django.http import HttpResponse
# Create your views here.
img_height, img_width = 150, 150
model = load_model('./models/face_mask.h5')
labelInfo = {0:'Mask Detected', 1:'No Mask Detected'}
# Create your views here.
def facemask_detection(request):
    return render(request,'facemask-detection.html',{'is_prediction':False})

def predict(request):
    try:
        url = request.POST['url']
    except:
        return HttpResponse('Error !!!')

    im = Image.open(urlopen(url))
    img = im.resize((img_height, img_width))
    x = image.img_to_array(img)
    x /= 255
    x = x.reshape(1, img_height, img_width, 3)
    predi = model.predict(x)
    final_prediction = labelInfo[np.argmax(predi[0])]
    return render(request,'facemask-detection.html',{'img_url':url, 'prediction':final_prediction.upper(),'accuracy':round(max(predi[0])*100,2),'is_prediction':True})
