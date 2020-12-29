import requests, csv

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()

#create list of dict
for k,v in enumerate(data):
    new = []
    for x,y in v.items():
        new.append(y)

#remove not dictionary objects
currency_list = new[4]


def create_csv():
    with open("currency_exchange_rates.csv", "w", newline="") as csvfile:
        filednames = ['currency', 'code', 'bid', 'ask']
        writer = csv.DictWriter(csvfile, fieldnames=filednames, delimiter=";")
        writer.writeheader()
        writer.writerows(currency_list)
        print("data loaded to csv file")
