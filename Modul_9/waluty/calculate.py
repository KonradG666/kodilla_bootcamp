from flask import Flask, render_template, request, redirect, url_for
from obsluga_api import currency_list


# get the cash amount for called amount
def calc(currency, amount):
    amount = float(amount)

    for dic in currency_list:
        if dic["currency"] == currency:
            value = float(dic["ask"])
            

    return (value*amount)
