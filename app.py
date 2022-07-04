#import pyautogui
from flask import Flask, render_template, request, jsonify
import time
import json
import os

import waitress
from waitress import serve
from chat import get_response
#import webbrowser,pyautogui
from threading import Timer 

app = Flask(__name__)


@app.route("/",methods=["GET"])
def index_get():
    #pyautogui.hotkey('ctrl', 'w')
    return render_template("base.html")

@app.route("/predict",methods=["POST"])
def predict():
    text = request.get_json().get("message") 
    #TODO: check if text is valid  
    response = get_response(text)  
    message = {"answer":response}
    return jsonify(message)

#def open_browser():
    #print(request.remote_addr)
    #webbrowser.open_new("http://127.0.0.1:5000/")

if __name__ == "__main__":
    #open_browser()
    #app.run(debug=True)
    #serve(app, host='0.0.0.0', port=5000)
    app.debug = False
    port = int(os.environ.get('PORT', 33507))
    serve(app, host='0.0.0.0', port=port)
    
    


