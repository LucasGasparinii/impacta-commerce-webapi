from flask import Flask
app = Flask(__name__)
@app.route("/")
def Hello_word():
    return "<p Hello Word</p>"