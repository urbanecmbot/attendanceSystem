from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html", tittle='SimpleAttendanceSystem')

if __name__ == "__main__":
    app.run()
