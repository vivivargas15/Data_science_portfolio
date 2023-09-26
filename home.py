from flask import Flask, render_template


app= Flask(__name__)

@app.route("/")
def hola():
    return "hola mundo sssss"

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/cv")
def curriculum():
    return render_template("CV.html")

@app.route("/edasuicides")
def suicides():
    return render_template("suicides.html")






if __name__=="__main__":
    app.run()