from flask import Flask, render_template, request, redirect, url_for
from obsluga_api import currency_list


app = Flask(__name__)




@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        currency = request.form['currency']
        amount = request.form['amount']
        

        try:
            print(calc())

        except:
            return amount * exchange.value

    else:
        return render_template('corn_exchange.html')


def calc():
    for dic in currency_list:
        if dic["currency"] == currency:
            value = float(dic["ask"])
            return value


if __name__=="__main__":    
     app.run(debug=True)