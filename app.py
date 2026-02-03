import os
from flask import Flask, render_template
from config import Config

app = Flask(__name__,
    static_folder='static',
    template_folder='templates')

app.config.from_object(Config)

@app.route("/")
def index():
    # Retorna o ficheiro HTML da pasta /templates
    return render_template("index.html")

@app.route("/healthz")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run()
