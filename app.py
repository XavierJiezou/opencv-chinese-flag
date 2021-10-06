from flask import Flask, jsonify, request, render_template, redirect, url_for
from algorithm import algorithm


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/upload', methods=['POST'])
def upload():
    inp_path = './static/img/upload/inp.png'
    out_path = './static/img/result/out.png'
    flag_path = './static/img/flag.png'
    request.files.get('file').save(inp_path)
    algorithm(inp_path, flag_path, out_path)
    return jsonify({'outdir': url_for('static', filename='img/result/out.png')})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
