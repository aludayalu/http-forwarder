import flask, requests
from flask import Flask, request

app=Flask(__name__)

url="http://0.tcp.in.ngrok.io:17861"

@app.route("/", methods=["POST", "GET"])
def home():
    print(request.get_json())
    res=requests.post(url, json={"image":request.get_json()["image"], "route":"/"})
    return res.content

@app.route("/stats", methods=["POST", "GET"])
def stats():
    res=requests.post(url, json={"image":request.get_json()["image"], "route":"/stats"})
    return res.content

@app.route("/stats_increment", methods=["POST", "GET"])
def stats_increment():
    res=requests.post(url, json={"image":request.get_json()["image"], "route":"/stats_increment"})
    return res.content