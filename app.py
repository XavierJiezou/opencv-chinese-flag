from flask import Flask, jsonify, request, render_template, redirect, url_for
from algorithm import algorithm
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
    algorithm(inp_path, 'img/flag.png', out_path)
    return jsonify({'outdir': url_for('static', filename='img/result/out.png')})


def main():
    webview.create_window('OPENCV-CHINESE-FLAG', app)
    webview.start()


if __name__ == '__main__':
    main()
    