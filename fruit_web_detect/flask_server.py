from __future__ import division, print_function
import os
import time

import torch
from torchvision import models,transforms
import torch.nn as nn

from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

from PIL import Image


# pull-requests 테스트 주석입니다.

# from dynamikontrol import Module
# module = Module()

# label list
red_tomato_list = []
green_tomato_list = []
rot_list = []


app = Flask(__name__)
# MODEL_PATH = 'C:/Users/user/PycharmProjects/pythonProject1/fruit_detect/fruit_web_detect/pepper_CNN1.pt'
MODEL_PATH = 'C:/Users/user/PycharmProjects/pythonProject1/fruit_detect/fruit_web_detect/fruit_classification.pt'

transforms_test = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

model = models.resnet18()
num_features = model.fc.in_features
# transfer learning: 모델의 출력 뉴런 수를 3개로 교체하여 마지막 레이어 다시 학습시키기
model.fc = nn.Linear(num_features, 3)
model.load_state_dict(torch.load(MODEL_PATH, map_location=torch.device('cpu')))
model.eval()

# labels = ['red tomato', 'green tomato', 'tomato blossom-end rot']
labels = ['green tomato', 'red tomato', 'rot']

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method =='POST':
        f = request.files['file']

        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        img = Image.open(f)
        img = transforms_test(img).unsqueeze(0).to(device='cpu')
        with torch.no_grad():
            outputs = model(img)
            _, preds = torch.max(outputs, 1)

            # if labels[preds[0]] == 'red tomato':
            #     red_tomato_list.append('1')
            #     module.motor.angle(-60)
            #     time.sleep(2)
            #     module.motor.angle(60)
            #     time.sleep(2)
            #
            # elif labels[preds[0]] == 'green tomato':
            #     green_tomato_list.append('2')
            #     module.motor.angle(60)
            #     time.sleep(2)
            #     module.motor.angle(-60)
            #     time.sleep(2)
            #
            # elif labels[preds[0]] == 'rot':
            #     rot_list.append('3')
            #     module.motor.angle(-60)
            #     time.sleep(2)
            #     module.motor.angle(60)
            #     time.sleep(2)

            return labels[preds[0]]


        return 'model predict error'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

