from flask import Flask, render_template, request, redirect, url_for
from obsluga_api import currency_list




app = Flask(__name__)




@app.route('/', methods=['POST', 'GET'])
def index():
    print("index")
    if request.method == 'POST':
        currency = request.form['currency']
        amount = request.form['amount']

        try:
            for dic in currency_list:
                if dic["currency"] == currency:
                    value = dic["ask"]
                    value = format((value*int(amount)), "7.2f")
                    score = str(value)

        except:
            print("Somethin went wrong with your operatin!")
        else:
            print("calculation completed")
            return render_template('corn_exchange_completed.html', score=score)


    else:
        return render_template('corn_exchange.html')


if __name__=="__main__":    
     app.run(debug=True)