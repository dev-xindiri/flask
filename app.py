from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello from Wolke!"

@app.route("/healthz")
def health():
    return {"status": "healthy"}, 200
