import flask
from flask import *

app= Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/upload_Text", methods=["GET", "POST"])
def uploadText():
    arr=[]
    plain_text = request.form['cipher-text']
    number = len(plain_text)
    for i in range(0,number):
        arr.append(plain_text[i].lower())
    print(arr)  

    return render_template("index.html", Arr=arr , len=len(plain_text))


if __name__ == '__main__':
    app.run(port=5500 , debug = True)