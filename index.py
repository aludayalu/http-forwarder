import flask, requests
from flask import Flask, request

app=Flask(__name__)

url="http://0.tcp.in.ngrok.io:17861"

@app.route("/", methods=["POST", "GET"])
def home():
    res=requests.post(url, files=dict(request.files), headers=dict(request.headers))
    return res.content