import os
import cv2
import numpy as np
import base64
from matplotlib import pyplot as plt
from flask import Flask, escape, request, jsonify

#image = cv2.imread("4.jpg", cv2.IMREAD_COLOR)

#bilateral = cv2.bilateralFilter(image, 35, 75, 75)

#cv2.imshow("original", image)
#cv2.imshow("last", bilateral)

#retval, buffer = cv2.imencode('.jpg', bilateral)
#jpg_as_text = base64.b64encode(buffer)
#print(jpg_as_text[:100])
#print(str(jpg_as_text[:100]))
#cv2.waitKey(0)
#cv2.destroyAllWindows()

app = Flask(__name__)

#input img mat
def blurr(img):
    res = cv2.bilateralFilter(img, 35, 75, 75)
    retval, buffer = cv2.imencode('.jpg', res)
    jpg_as_text = base64.b64encode(buffer)
    return jpg_as_text

def black_white(img):
    #res = cv2.bilateralFilter(img, 35, 75, 75)
    res = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    retval, buffer = cv2.imencode('.jpg', res)
    jpg_as_text = base64.b64encode(buffer)
    return jpg_as_text

#input img mat
def efecto3(img):
    res = cv2.bilateralFilter(img, 35, 75, 75)
    retval, buffer = cv2.imencode('.jpg', res)
    jpg_as_text = base64.b64encode(buffer)
    return jpg_as_text

def efecto4(img):
    #res = cv2.bilateralFilter(img, 35, 75, 75)
    res = cv2.cvtColor(img, cv2.arrowedLine)
    retval, buffer = cv2.imencode('.jpg', res)
    jpg_as_text = base64.b64encode(buffer)
    return jpg_as_text


@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route('/api/upload',methods=['GET', 'POST'])
def upload():
    value = request.get_json()
    string = value['img']
    string = string.replace('data:image/jpeg;base64', '')
    string = string.replace('data:image/png;base64', '')
    #print(value)
    jpg_original = base64.b64decode(string)
    jpg_as_np = np.frombuffer(jpg_original, dtype=np.uint8)
    img = cv2.imdecode(jpg_as_np, flags=1)
    bilateral = cv2.bilateralFilter(img, 35, 75, 75)
    #encode para enviar
    #retval, buffer = cv2.imencode('.jpg', bilateral)
    #jpg_as_text = base64.b64encode(buffer)
    return jsonify([{'data':blurr(img)},{'data':black_white(img) }])
