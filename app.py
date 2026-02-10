from flask import Flask, request

app = Flask(__name__)

@app.get("/")
def index():
    return "Hello Flask on Codespaces!"

@app.get("/hello")
def hello():
    name = request.args.get("name", "world")
    return f"Hello, {name}!"
