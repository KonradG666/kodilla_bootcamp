from faker import Faker
f = Faker()
from codetiming import Timer
class BaseContact:
    
    def __init__(self, name, surname, phone, email):
           
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email  

    def __str__(self):
        return f"{self.name} {self.surname} {self.email}"

    def __repr__(self):
        return f"\n* BaseCard(name={self.name} surname={self.surname} phone={self.phone} email={self.email})"

    def contact(self):
        print(f"Wybieram numer: {self.phone} i dzwonię do {self.name} {self.surname}")
        print(f"\tFull name print will take {self.full_length} characters.")

    @property
    def full_length(self):
        name_len = len(self.name)
        surname_len = len(self.surname)
        return name_len + surname_len +1

class BusinessContact(BaseContact):

    def __init__(self, job_title, company, work_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.job_title = job_title
        self.company = company
        self.work_phone = work_phone

    def business_contact(self):
        print(f"Wybieram numer: {self.work_phone} i dzwonię do {self.name} {self.surname}")
        print(f"\tFull name print will take {self.full_length} characters.")

    def __repr__(self):
        return f"\n* BusinessCard(name={self.name} surname={self.surname} phone={self.phone} company ={self.company} job_title={self.job_title} work_phone={self.work_phone} email={self.email})"
  

card_x1 = BaseContact(name = f.first_name(), surname = f.last_name(), phone = f.phone_number(), email = f.email())
card_y1 = BaseContact(name = f.first_name(), surname = f.last_name(), phone = f.phone_number(), email = f.email())
card_x2 = BusinessContact(name = f.first_name(), surname = f.last_name(), phone = f.phone_number(), company = f.company(), job_title = f.job(),work_phone= f.phone_number(),  email = f.email())
card_y2 = BusinessContact(name = f.first_name(), surname = f.last_name(), phone = f.phone_number(), company = f.company(), job_title = f.job(),work_phone= f.phone_number(),  email = f.email())

###############

OP_NAME = "name"
OP_SURNAME = "surname"
OP_EMAIL = "email"
OP_SHOW = "show"
OP_BUSINESS = "business"
OP_BASE = "base"
OP_SORT = "sort"
OP_CREATE = "create"
OP_EXIT = "exit"

ALLOWED_SORT = [OP_NAME, OP_SURNAME, OP_EMAIL, OP_EXIT]
ALLOWED_SHOW = [OP_BASE, OP_BUSINESS, OP_EXIT]
ALLOWED_CONTACT = [OP_CREATE, OP_SHOW, OP_SORT, OP_EXIT]
ALLOWED_CREATE = [OP_BASE, OP_BUSINESS, OP_EXIT]

fake_base_cards = []
fake_business_cards = []

def sort_by_name():
    return sorted(fake_base_cards, key=lambda Card: Card.name)
def sort_by_surname():
    return sorted(fake_base_cards, key=lambda Card: Card.surname)                   # surname sort not working
def sort_by_email():
    return sorted(fake_base_cards, key=lambda Card: Card.email)

#creating new contacts
@Timer(text="Contacts created in {:.2f} seconds")
def create_business():
    #card_num = int(input("How many contact do you want to create? "))               # need to be replaced with set_input() to remove time delay with manual imput 
    for index in enumerate(range(0,card_num)):
        fake_business_cards.append( 
            BusinessContact(
                name = f.first_name(),
                surname = f.last_name(),
                phone = f.phone_number(),
                company = f.company(),
                job_title = f.job(),
                work_phone= f.phone_number(),
                email = f.email())
                )
@Timer(text="Contacts created in {:.2f} seconds")
def create_base():
    #card_num = int(input("How many contact do you want to create? "))               # need to be replaced with set_input() to remove time delay with manual imput
    for index in enumerate(range(0,card_num)):
        fake_base_cards.append(
            BaseContact(
                name = f.first_name(), 
                surname = f.last_name(), 
                phone = f.phone_number(), 
                email = f.email())
                )
def set_input():
    card_num = int(input("How many contact do you want to create? "))
    return card_num


def contacts():
    while True:
        op = input("Choose your action from:\n- "+"\n- ".join(ALLOWED_CONTACT))
        if op not in ALLOWED_CONTACT:
            print("Input error. Try again.")
            continue
        if op == OP_EXIT:
            exit("Bye")

        elif op == OP_CREATE:
            op_c = input("What do you want to create or empty for return?\n- "+"\n- ".join(ALLOWED_CREATE))
            if op_c == OP_BASE:
                card_num = set_input()                                         # NameError: name 'card_num' is not defined
                create_base()
                print("Base card created")
            elif op_c == OP_BUSINESS:
                card_num = set_input()                                         # NameError: name 'card_num' is not defined
                create_business()
                print("Business card created")
            elif op_c == OP_EXIT:
                exit("Bye")
            else:
                print("Back to main menu")

        elif op == OP_SHOW:
            op_s = input ("What you want to see or empty for return.\n- "+"\n- ".join(ALLOWED_SHOW))
            if op_s == OP_BASE:
                print(fake_base_cards)
            elif op_s == OP_BUSINESS:
                print(fake_business_cards)
            elif op_s == OP_EXIT:
                exit("Bye")
            else:
                print("Back to main menu")

        elif op == OP_SORT:
            op_ss = input("Choose your sorting option or empty for return.\n- "+"\n- ".join(ALLOWED_SORT))
            if op_ss == OP_NAME:
                print(sort_by_name())
            elif op_ss == OP_SURNAME:
                print(sort_by_name())
            elif op_ss == OP_EMAIL:
                print(sort_by_email())
            elif op_ss == OP_EXIT:
                exit("Bye")
            else:
                print("Back to main menu")

contacts()
