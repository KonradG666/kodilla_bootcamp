from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
db = SQLAlchemy(app)

class contacts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), nullable=False)
    surname = db.Column(db.String(15), nullable=True)
    message = db.Column(db.String(200),nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/')
@app.route('/index.html')
def index():
    return render_template("index.html")

@app.route('/about_me.html')
def about_me():
    return render_template("about_me.html")

@app.route('/contact_me.html', methods=['POST', 'GET'])
def contact_me():
    print("start def")
    if request.method == 'POST':
        print("got posted")
        content = (request.form['name'], request.form['surname'], request.form['message'])
        new_message = contacts(content)
        print(content)
        try:
            db.session.add(new_message)
            db.session.commit()
            return redirect('/')
        except:
            return "There was an issue with your form"
        
    else:
        return render_template("contact_me.html")











if __name__=="__main__":    
     app.run(debug=True)