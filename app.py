from flask import Flask, render_template, request
import os
from detector import detect_objects  # your function

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/detect", methods=["POST"])
def detect():
    if "file" not in request.files:
        return "No file uploaded"

    file = request.files["file"]
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    # Run detection
    result_path = detect_objects(filepath)

    return render_template("result.html", image=result_path)

if __name__ == "__main__":
    app.run(debug=True)