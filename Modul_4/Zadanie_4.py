"""
Żeby dobrze sobie to przećwiczyć, zadeklaruj trzy funkcje z pustą implementacją, czyli z komendą pass.
Pierwsza z nich, fun_default, powinna przyjmować argumenty pozycyjne albo nazwane. 
Druga, fun_positional, tylko pozycyjne. Trzecia, fun_keyword, tylko nazwane. 
Testem na to, czy druga i trzecia funkcja jest dobrze zadeklarowana będzie próba podstawienia argumentów odwrotnie, 
niż było w planie, czyli np. do fun_keyword, próba podania argumentów pozycyjnych.
"""


# 1
def fun_default():
    pass

# 2
def fun_positional(pay = 'card',shop = 'kiosk'):
    pass

# 3
def fun_keyword(pay = 'card', *, shop = 'kiosk'):
    pass
