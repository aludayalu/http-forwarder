import flask, requests
from flask import Flask, request

app=Flask(__name__)

url="http://0.tcp.in.ngrok.io:17861"

@app.route("/", methods=["POST", "GET"])
def home():
    print(request.get_json())
    res=requests.post(url, json={"image":request.get_json()["image"]})
    return res.content