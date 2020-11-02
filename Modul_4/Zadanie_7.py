"""
Stwórz własny skrypt, do którego zaimportujesz moduł logging. Na początek zdefiniuj logowanie na poziomie DEBUG i zaloguj w nim pojedynczą linijkę.
Czy istnieje teraz możliwość zmiany minimalnego poziomu logowania? Sprawdź w dokumentacji!
"""
import sys
import logging
logging.basicConfig(level=logging.DEBUG)

def call_out(name, age):
    if age > 18:
        print(f"Yo! {name} want a beer?")
    else:
        print(f"Hey {name} want some juice?")


if __name__ == "__main__":
    logging.debug("The program was called with this parameters %s" % sys.argv[1:])
    logging.debug("First parameter is %s" % sys.argv[1])
    name = sys.argv[1]
    age = int(sys.argv[2])
    call_out(name, age)