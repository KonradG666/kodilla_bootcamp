from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class Contacts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), nullable=False)
    surname = db.Column(db.String(15), nullable=True)
    message = db.Column(db.String(400),nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, name, surname, message):
        self.name = name
        self.surname = surname
        self.message = message

@app.route('/')
@app.route('/index.html')
def index():
    return render_template("index.html")

@app.route('/about_me.html')
def about_me():
    return render_template("about_me.html")

@app.route('/message_send.html')
def done():
    return render_template("message_send.html")


@app.route('/contact_me.html', methods=['POST', 'GET'])
def contact_me():

    if request.method == 'POST':
        if not request.form['name'] or not request.form['surname'] or not request.form['message']:
            flash("Please enter all required data", 'error')
        else:
            new_message = Contacts(
                request.form['name'], request.form['surname'], request.form['message'])

            db.session.add(new_message)
            db.session.commit()

            flash("Message successfully send.")
            return render_template("/message_send.html")
    return render_template("/contact_me.html")


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
