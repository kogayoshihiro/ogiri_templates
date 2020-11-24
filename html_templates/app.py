from flask import Flask, redirect, render_template
from flask import request, Markup
import os, time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__' :
    app.run(host='0.0.0.0')
