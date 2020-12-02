from faker import Faker
f = Faker()

database = []

class BaseContact:
    def __init__(self, name, surname, phone, email):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"{self.name} {self.surname} {self.email}"

    __repr__ = __str__

    def contact(self):
        print(f"Wybieram numer {self.phone} i dzwonię do {self.name} {self.surname}")

class BusinessContact(BaseContact):
    def __init__(self, job_title, company, work_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.job_title = job_title
        self.company = company
        self.work_phone = work_phone

    def business_contact(self):
        print(f"Wybieram numer: {self.work_phone} i dzwonię do {self.name} {self.surname}")
    
    # tu nie ma funkcji __str__ bo jest dziedziczona z BaseContact

# stale sa definiowane jako globalne, poza cialem funkcji
# stale definiujemy z wielkich liter
OP_CREATE = "create"
OP_SORT = "sort"
OP_EXIT = "exit"
OP_SHOW = "show"
ALLOWED_OPERATIONS = [OP_CREATE, OP_SORT, OP_SHOW, OP_EXIT]

CONTACT_BASE = "base"
CONTACT_BUSINESS = "business"
ALLOWED_CONTACTS = [CONTACT_BASE, CONTACT_BUSINESS]



def run():
    while True:
        op  = input("Choose your action from:\n- "+"\n- ".join(ALLOWED_OPERATIONS))
        if op not in ALLOWED_OPERATIONS:
            print("Input error. Try again.")
            continue
        if op == OP_EXIT:
            print("Bye")
            exit()
        
        if op == OP_CREATE:
            contact = create_contact(
                name = f.first_name(), 
                surname = f.last_name(), 
                phone = f.phone_number(), 
                company = f.company(), 
                job_title = f.job(),
                work_phone= f.phone_number(),  
                email = f.email()
                )
            database.append(contact)
        elif op == OP_SORT:
            sort_contacts()
        elif op == OP_SHOW:
            print(database)


def create_contact(name, surname, phone , company, job_title, work_phone, email):
    while True:
        op = input("What card do you want to create ?\n- " + "\n- ".join(ALLOWED_CONTACTS))
        if op not in ALLOWED_CONTACTS:
            print(f"Input error. {op} not in options list")
            continue
        if op == CONTACT_BUSINESS:
            return BusinessContact(
                name = name,
                surname = surname,
                phone = phone,
                company = company,
                job_title = job_title,
                work_phone= work_phone,
                email = email
                )
        elif op == CONTACT_BASE:
            return BaseContact(name = name, surname = surname, phone = phone, email = email)


#start
run()


"""
1. Stale definiujemy albo w klasie, albo globalnie, bardzo rzadko jako stale lokalne dla funkcji
2. Nazwy stalych deklarujemy z wielkich liter
3. Jak je deklarujemy to uzywajmu ;) https://github.com/Cram-In/kodilla_bootcamp/blob/main/Modul_7/address_book_v2.py#L177 to powinno byc OP_EXIT zamias "exit"
4. Staramy sie ograniczac odpowiedzialnosc funkcji - jak create to tworzy, jak show to pokazuje - 2 rozne funkcjonalnosci - 2 rozne fukncje
5. Funkcje moga przyjmowac parametry - korzystajmy z tego (np create_contact w moim przykladzie)
"""