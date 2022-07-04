import json
from util import detect_faces
from flask import Flask, request


app = Flask(__name__)


@app.route('/face_detect', methods=['POST', 'GET'])
def face_detect():
    if request.method == 'POST':
        if 'file' in request.files:
            file = request.files.get('file')
            resp = detect_faces(file)

            return json.dumps(resp)

    return '''
    <!doctype html>
    <title>Face Detection</title>
    <head>
    <style>
    * {margin:0; padding:0;}
    body {background:#fff; width:100%; height:100vh;}
    h1 {width:100%; height:20%; display:flex; justify-content:center; align-items:flex-end; color:#000;}
    div {width:100%; height:15%; display:flex; justify-content:center; align-items:center;}
    </style>
    </head>
    <body>
    <h1>Upload Image</h1>
    <div>
    <form method=post enctype=multipart/form-data>
    <input type=file name=file>
    <input class="submit_input" type=submit value=Upload>
    </form>
    </div>
    </body>
    '''


app.run(host='0.0.0.0', port='5001', debug=True)
