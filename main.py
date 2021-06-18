from flask import *
import os
app = Flask(__name__)
# Session which allows you to store information specific to a user from one request to the next. This is implemented on top of cookies for you and signs the cookies cryptographically. What this means is that the user could look at the contents of your cookie but not modify it, unless they know the secret key used for signing.
app.secret_key = os.urandom(16)
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = set(['jpeg', 'jpg', 'png', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def root():
    return "SHOP-IT"

@app.route("/add")
def admin():
    pass

@app.route("/additem",methods=["POST,GET"])
def additem():
    pass

@app.route("/remove")
def remove():
    pass

@app.route("/removeitem")
def removeitem():
    pass

@app.route("/displayCategory")
def displayCategory():
    pass

@app.route("/account/profile")
def profileHome():
    pass

@app.route("/account/profile/edit")
def editprofile():
    pass

@app.route("/account/profile/changePassword")
def changePassword():
    pass

@app.route("/updateProfile",methods=["POST","GET"])
def updateProfile():
    pass

@app.route("/loginForm")
def loginForm():
    pass

@app.route("/login",methods=["POST","GET"])
def login():
    pass

@app.route("/productDescription")
def productDescription():
    pass

@app.route("/addTocart")
def addTocart():
    pass

@app.route("/cart")
def cart():
    pass

@app.route("/removeFromcart")
def removeFromcart():
    pass

@app.route("/logout")
def logout():
    pass

def is_valid(email, password):
    pass

@app.route("/register", methods = ['GET', 'POST'])
def register():
    pass

@app.route("/registerationForm")
def registerationForm():
    pass

def allowed_file(filename):
    pass

def parse(data):
    pass

if __name__ == '__main__':
    app.run(debug=True)