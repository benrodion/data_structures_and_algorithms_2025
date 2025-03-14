from flask import Flask, render_template

app = Flask(__name__)

#base home page using the stylers from the file home.html
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html"), render_template("layout.html")

#hello-page which is accessed by adding "/hello" to the link in the browser 
@app.route("/hello")
@app.route("/hello/<city>")
def hello(city):
    return f"hello {city}"


#adding an About-page
@app.route("/about")
def about_me():
    return render_template("about.html")


