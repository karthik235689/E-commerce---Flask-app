from flask import *
import os ,hashlib ,os ,sqlite3
app = Flask(__name__)
# Session which allows you to store information specific to a user from one request to the next. This is implemented on top of cookies for you and signs the cookies cryptographically. What this means is that the user could look at the contents of your cookie but not modify it, unless they know the secret key used for signing.
app.secret_key = os.urandom(16)
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = set(['jpeg', 'jpg', 'png', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def root():
    return render_template('home.html')

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
    if 'email' in session:
        return redirect(url_for('root'))
    else:
        return render_template('login.html',error='')

@app.route("/login",methods=["POST","GET"])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if is_valid(email, password):
            session['email'] = email
            return redirect(url_for('root'))
        else:
            error = 'Invalid UserId / Password'
            return render_template('login.html', error=error)


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
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute('SELECT email, password FROM users')
    data = cur.fetchall()
    for row in data:
        if row[0] == email and row[1] == password:
            return True
    return False

@app.route("/register", methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        password = request.form['password']
        first_name = request.form['fname']
        last_name = request.form['lname']
        email = request.form['email']
        locality = request.form['address1']
        landmark = request.form['address2']
        pincode = request.form['pincode']
        city = request.form['city']
        state =request.form['state']
        country = request.form['country']
        phone = request.form['number']

        with sqlite3.connect('database.db') as con:
            try:
                cur = con.cursor()
                cur.execute('INSERT INTO users (password, email, firstName, lastName, address1, address2, zipcode, city, state, country, phone) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (password, email, first_name, last_name, locality, landmark, pincode, city, state, country, phone))

                con.commit()

                msg = "Registered Successfully"
            except:
                con.rollback()
                msg = "Error occured"
        con.close()
        return render_template("login.html", error=msg)


@app.route("/registerationForm")
def registerationForm():
    return render_template("register.html")

def allowed_file(filename):
    pass

def parse(data):
    pass

if __name__ == '__main__':
    app.run(debug=True)