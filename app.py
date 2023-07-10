from flask import Flask, render_template
import db

app= Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def login():
    error = 'ログインに失敗しました。'
    return render_template('index.html',error=error)