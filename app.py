from flask import Flask, render_template, request
import os
from nlp import OCR
from nlp import ENT
app = Flask(__name__)

BASE_PATH = os.getcwd()
UPLOAD_PATH = os.path.join(
    BASE_PATH, '/Users/sanjaydilii/Desktop/ner/static/upload')


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        upload_file = request.files['image_name']
        filename = upload_file.filename
        path_save = os.path.join(UPLOAD_PATH, filename)
        upload_file.save(path_save)
        string = (path_save)
        table = ENT(string)

        return render_template('index.html', upload=True, upload_image=filename)

    return render_template('index.html', upload=False)


if __name__ == "__main__":
    app.run(debug=True)







