from flask import Flask, redirect, url_for, render_template, request, send_from_directory
from werkzeug.utils import secure_filename
import subprocess
import os

app = Flask(__name__)
app.static_folder = 'static'

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'

@app.route('/render', methods = ['GET', 'POST'])
def render():
    if request.method == "POST":
        bp = request.form["bp"]
        file = request.form["fn"]
        output = request.form["out"]
        frame = request.form["frame_n1"]
        subprocess.Popen(f"{bp} -b {file} -o {output} -f {frame}", shell=True)

    return render_template("renderimage.html")

@app.route('/renderanim', methods = ['GET', 'POST'])
def render_anim():
    if request.method == "POST":
        bp = request.form["bp"]
        file = request.form["fn"]
        output = request.form["out"]
        start_frame = request.form["s_frame"]
        end_frame = request.form["e_frame"]
        subprocess.Popen(f"{bp} -b {file} -o {output} -s {start_frame} -e {end_frame} -P script.py -a", shell=True)

    return render_template("renderanimation.html")

@app.route('/rsync', methods = ['GET', 'POST'])
def rsync_data():
    if request.method == "POST":
        localdir = request.form["bp"]
        user = request.form["fn"]
        hostname = request.form["out"]
        nasdir = request.form["s_frame"]
        subprocess.Popen(f"rsync -a --progress {localdir} {user}@{hostname}:{nasdir}", shell=True)

    return render_template("rsync.html")

if __name__ == '__main__':
    app.run()
