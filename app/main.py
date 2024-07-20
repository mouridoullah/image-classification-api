from flask import Flask, request, jsonify
import torch
import torchvision.transforms as transforms
from torchvision import models
from PIL import Image
import io
import json
import requests

app = Flask(__name__)

# Charger le modèle pré-entraîné ResNet18
model = models.resnet18(pretrained=True)
model.eval()

# Charger les étiquettes de classe
with open('imagenet-simple-labels.json') as f:
    labels = json.load(f)

def transform_image(image_bytes):
    my_transforms = transforms.Compose([
        transforms.Resize(255),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(
            [0.485, 0.456, 0.406],
            [0.229, 0.224, 0.225])
    ])
    image = Image.open(io.BytesIO(image_bytes))
    return my_transforms(image).unsqueeze(0)

def get_prediction(image_bytes):
    tensor = transform_image(image_bytes)
    outputs = model(tensor)
    _, predicted = outputs.max(1)
    return predicted.item()

def download_image(image_url):
    response = requests.get(image_url)
    if response.status_code == 200:
        return response.content
    else:
        raise ValueError(f"Unable to download image from URL. Status code: {response.status_code}")

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' in request.files:
        file = request.files['file']
        img_bytes = file.read()
    elif 'url' in request.form:
        image_url = request.form['url']
        img_bytes = download_image(image_url)
    else:
        return jsonify({'error': 'No file or URL provided'}), 400
    
    class_id = get_prediction(img_bytes)
    class_name = labels[class_id] 
    return jsonify({'class_id': class_id, 'class_name': class_name})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
