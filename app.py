from flask import Flask, request, send_file, render_template
from cartoonify import cartoonify
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files['file']
        input_path = os.path.join(UPLOAD_FOLDER, 'input.jpg')
        output_path = os.path.join(UPLOAD_FOLDER, 'cartoon.jpg')

        file.save(input_path)
        cartoonify(input_path, output_path)
        return send_file(output_path, mimetype='image/jpeg')

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
