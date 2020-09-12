from django.shortcuts import render
from urllib.request import urlopen
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import json
import numpy as np
from django.http import HttpResponse
# Create your views here.
img_height, img_width = 224, 224
model = load_model('./models/img_class.h5')
with open('./models/imagenet_classes.json','r') as f:
    labelInfo = f.read()

labelInfo = json.loads(labelInfo)

def imgclass(request):
    return render(request,'imgclass.html',{'is_prediction':False})

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
    final_prediction = labelInfo[str(np.argmax(predi[0]))][1]
    return render(request,'imgclass.html',{'img_url':url, 'prediction':final_prediction.upper(),'accuracy':round(max(predi[0])*100,2),'is_prediction':True})
