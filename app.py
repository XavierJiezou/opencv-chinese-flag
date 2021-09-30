from flask import Flask, jsonify, request, render_template, redirect, url_for
from main import main
import sys
import os
import webview


if getattr(sys, 'frozen', False):
    template_folder = os.path.join(sys._MEIPASS, 'templates')
    static_folder = os.path.join(sys._MEIPASS, 'static')
    app = Flask(
        __name__,
        template_folder=template_folder,
        static_folder=static_folder
    )
else:
    app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/upload', methods=['POST'])
def upload():
    inp_path = './static/img/upload/inp.png'
    out_path = './static/img/result/out.png'
    request.files.get('file').save(inp_path)
    main(inp_path, 'flag.png', out_path)
    return jsonify({'outdir': url_for('static', filename='img/result/out.png')})


if __name__ == '__main__':
    webview.create_window('OPENCV-CHINESE-FLAG', app)
    webview.start()