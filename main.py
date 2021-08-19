from flask import Flask, redirect, render_template, request
from werkzeug.utils import secure_filename
import subprocess

app = Flask(__name__)
app.static_folder = 'static'

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/complete')
def rendercomplete():
    return render_template("complete.html")

@app.route('/progress', methods=['GET'])
def display_progress():
	with open('filename.txt', 'r') as f:
		return render_template('progress.html', text=f.read())

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'

@app.route('/render', methods = ['GET', 'POST'])
def render():
    if request.method == "GET":
        return render_template("renderimage.html")
    elif request.method == "POST":
        bp = request.form["bp"]
        file = request.form["fn"]
        output = request.form["out"]
        frame = request.form["frame_n1"]
        process = subprocess.Popen((f"{bp} -b {file} -o {output} -P script.py -f {frame}"), shell=True, stdout=subprocess.PIPE)
        while process.stdout.readable():
            line = process.stdout.readline()
            if not line:
                break
            with open('filename.txt', 'w') as f:
                i = 0
                while i < 1:
                    print("Render Progress: ", line.strip().decode('utf-8'), file=f)
                    i += 1
                    if i == 1:
                        break
    return redirect("/complete", code=302)


    

@app.route('/renderanim', methods = ['GET', 'POST'])
def render_anim():
    if request.method == "GET":
        return render_template("renderanimation.html")
    elif request.method == "POST":
        bp = request.form["bp"]
        file = request.form["fn"]
        output = request.form["out"]
        start_frame = request.form["s_frame"]
        end_frame = request.form["e_frame"]
        process = subprocess.Popen((f"{bp} -b {file} -o {output} -s {start_frame} -e {end_frame} -P script.py -a"), shell=True, stdout=subprocess.PIPE)
        while process.stdout.readable():
            line = process.stdout.readline()
            if not line:
                break
            with open('filename.txt', 'w') as f:
                i = 0
                while i < 1:
                    print("Render Progress: ", line.strip().decode('utf-8'), file=f)
                    i += 1
                    if i == 1:
                        break
    return redirect("/complete", code=302)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
