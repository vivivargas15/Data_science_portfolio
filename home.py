from flask import Flask, render_template


app= Flask(__name__)

@app.route("/")
def hola():
    return "hola mundo sssss"


@app.route("/home")
def home():
    return render_template("index2.html")








if __name__=="__main__":
    app.run()