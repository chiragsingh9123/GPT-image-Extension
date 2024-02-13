from flask import Flask, request, jsonify
import pyautogui
import PIL.Image
import google.generativeai as genai
from flask_cors import CORS 
import subprocess
import time
import requests
GOOGLE_API_KEY='AIzaSyDtnDYXnzbDRHgc7m1xTt-vjbveF9KRfaU'
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro-vision')
chat = model.start_chat(history=[])

ngul=[]
def get_url():
    response = requests.get('http://localhost:4040/api/tunnels')
    data = response.json()
    ng_url = data['tunnels'][0]['public_url']
    f =  open('token.txt','w')
    f.writelines(ng_url)
    f.close()

try:
    get_url()
    print("1")
except :
    ngrok_process = subprocess.Popen(['ngrok', 'http', '5000'])
    print("2")
finally:
     get_url()
     print("3")


app = Flask(__name__)
CORS(app)

@app.route('/screen_shot', methods=['POST'])
def screen_sho():
    print('Taking Screen Shot')
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save('save.png')
    img = PIL.Image.open('save.png')
    response = model.generate_content(img)
    response_data = {'message': 'Taking Screen Shot'}
    return jsonify(response_data)

@app.route('/gen_response', methods=['POST'])
def screen_seeho():
    data =  request.args.get('q')
    print(data)
    img = PIL.Image.open('save.png')
    response = model.generate_content([data, img], stream=True)
    response.resolve()
    response_data = {'message': f'{response.text}'}
    return jsonify(response_data)



if __name__ == '__main__':
    app.run(port=5000)
