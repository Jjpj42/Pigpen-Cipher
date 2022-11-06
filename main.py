from flask import Flask , render_template , request , Markup

app= Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/upload_Text", methods=["GET", "POST"])
def uploadText():
    arr=[]
    if request.method == 'POST':
        plain_text = request.form['cipher-text']
        number = len(plain_text)
        for i in range(0,number):

            arr.append(plain_text[i].lower())
        print(arr)
    return render_template("index.html", arr=arr , Num=number)


if __name__ == '__main__':
    app.run(port=5500, debug = True)