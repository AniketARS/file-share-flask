from flask import Flask, render_template, request
import werkzeug
import os


app = Flask(__name__)


@app.route('/upload')
def upload():
    return render_template('upload.html')


@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        return 'file uploaded successfully'
		
if __name__ == '__main__':
    app.config['UPLOAD_FOLDER'] = os.curdir
    app.run(host="0.0.0.0")