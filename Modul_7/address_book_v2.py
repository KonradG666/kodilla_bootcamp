from faker import Faker
f = Faker()
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

    def __str__(self):
        return f"{self.name} {self.surname} {self.email}"

    def __repr__(self):
        return f"\n* BusinessCard(name={self.name} surname={self.surname} phone={self.phone} company ={self.company} job_title={self.job_title} work_phone={self.work_phone} email={self.email})"
  
card_a1 = BaseContact(name="Ronan",surname="Gray",phone="+1 602-436-1405",email="RonanGray@teleworm.us")
card_b1 = BaseContact(name="Hector",surname="Aitken",phone="+1 703-720-7243",email="HectorAitken@teleworm.us")
card_c1 = BaseContact(name="Rosie",surname="Black",phone="+44 078 8186 3677",email="RosieBlack@dayrep.com")
card_d1 = BaseContact(name="Belinda",surname="Banks",phone="+44 070 1275 8118",email="BelindaBanks@jourrapide.com")
card_e1 = BaseContact(name="Kazimiera",surname="Kowalczyk",phone="+48 67 901 44 25",email="KazimieraKowalczyk@armyspy.com")
card_x1 = BaseContact(name = f.first_name(), surname = f.last_name(), phone = f.phone_number(), email = f.email())
card_y1 = BaseContact(name = f.first_name(), surname = f.last_name(), phone = f.phone_number(), email = f.email())

card_a2 = BusinessContact(name="Ronan",surname="Gray",phone="+1 602-436-1405",company="Dee's Drive-In",job_title="Tree trimmer",work_phone="+1 203-225-0241", email="RonanGray@teleworm.us")
card_b2 = BusinessContact(name="Hector",surname="Aitken",phone="+1 703-720-7243",company="Mansmann's Department Store",job_title="Diagnostic medical sonographer",work_phone="+1 812-402-6815", email="HectorAitken@teleworm.us")
card_c2 = BusinessContact(name="Rosie",surname="Black",phone="+44 078 8186 3677",company="Steve & Barry's",job_title="Segmental paver",work_phone="+33 01.86.23.65.74", email="RosieBlack@dayrep.com")
card_d2 = BusinessContact(name="Belinda",surname="Banks",phone="+44 070 1275 8118",company="Benesome",job_title="Dressing room attendant",work_phone="+610(08) 9229 1383", email="BelindaBanks@jourrapide.com")
card_e2 = BusinessContact(name="Kazimiera",surname="Kowalczyk",phone="+48 67 901 44 25",company="National Lumber",job_title="Nannie",work_phone="+48 88 547 84 48", email="KazimieraKowalczyk@armyspy.com")
card_x2 = BusinessContact(name = f.first_name(), surname = f.last_name(), phone = f.phone_number(), company = f.company(), job_title = f.job(),work_phone= f.phone_number(),  email = f.email())
card_y2 = BusinessContact(name = f.first_name(), surname = f.last_name(), phone = f.phone_number(), company = f.company(), job_title = f.job(),work_phone= f.phone_number(),  email = f.email())

#sorting cards
cards = [card_a1, card_b1, card_c1, card_d1, card_e1, card_x1]
def sorting():
    by_name = "By name"
    by_surname = "By surname"
    by_email = "By email"
    menu = "Main menu"
    end = "Q"

    op_list = [
        by_name, by_email, by_surname, end, menu
    ]
    op = input("Please select your sorting option or 'Q' for exit.\n * " + "\n* ".join(op_list))
    while True:
        if op not in op_list:
            print(f"Input error. {op} not in options list")
            sorting()
        if op == "Q":
            print("Bye")
            exit()
        elif op == "By name":
            print(sort_by_name())
        elif op == "By surname":
            print(sort_by_surname())
        elif op == "By emial":
            print(sort_by_email())
        elif op == "Main menu":
            menu()
        sorting()
def sort_by_name():
    return sorted(cards, key=lambda Contact: Contact.name)
def sort_by_surname():
    return sorted(cards, key=lambda Contact: Contact.surname)
def sort_by_email():
    return sorted(cards, key=lambda Contact: Contact.email)
#creating new contacts
fake_base_card = []
fake_business_card = []
def create_contacts():
    print("Compose New Card. \n"+"."*32)
    business = "Business"
    base = "Base"
    get_base = "Show Base"
    get_business = "Show Business"
    end = "Q"
    menu = "Main menu"
    parameters = [
        business, base, end, get_base, get_business, menu
    ]
    op = input("What card do you want to create or 'Q' for exit.\n- " + "\n- ".join(parameters))
    while True:
        if op not in parameters:
            print(f"Input error. {op} not in options list")
            create_contacts()
        if op == "Business":
            create_business()            
        elif op == "Base":
            create_base()
        elif op == "Show Base":
            print(fake_base_card)
        elif op == "Show Business":
            print(fake_business_card)
        elif op== "Q":
            print("Bye")
            exit()
        elif op == "Main menu":
            menu()
        create_contacts()
def create_business():
    card_num = int(input("How many contact do you want to create? "))
    for index in enumerate(range(0,card_num)):
        fake_business_card.append(
            BusinessContact(
                name = f.first_name(),
                surname = f.last_name(),
                phone = f.phone_number(),
                company = f.company(),
                job_title = f.job(),
                work_phone= f.phone_number(),
                email = f.email())
                )
def create_base():
    card_num = int(input("How many contact do you want to create? "))
    print(f"{card_num} new base cards created.")
    for index in enumerate(range(0,card_num)):
        fake_base_card.append(
            BaseContact(
                name = f.first_name(), 
                surname = f.last_name(), 
                phone = f.phone_number(), 
                email = f.email())
                )
                

#base
card_x1.contact()
print("-"*80)
#business
card_x2.business_contact()
print("-"*80)

#main menu
def menu():
    op_create = "Create contact"
    op_sort = "Sort contacts"
    op_exit = "exit"

    op_list = [
        op_create, op_exit, op_sort
    ]
    menu_op = input("Choose your action:\n- "+"\n- ".join(op_list))
    while True:
        if menu_op not in op_list:
            print("Input error. Try again.")
            menu()
        if menu_op == "exit":
            print("Bye")
            exit()
        elif menu_op == "Create contact":
            create_contacts()
        elif menu_op == "Sort contacts":
            sorting()
        menu()

menu()