from flask import Flask, render_template, request, redirect, url_for
from obsluga_api import currency_list


app = Flask(__name__)




@app.route('/', methods=['POST', 'GET'])
def index():
    print("index")
    if request.method == 'POST':
        currency = request.form['currency']
        amount = request.form['amount']
        print("POST - {currency}")
        print("POST - {amount}")

        try:
            pass
            

        except:
            return "it was an error :/"

    else:
        return render_template('corn_exchange.html')


if __name__=="__main__":    
     app.run(debug=True)