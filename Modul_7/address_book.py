from faker import Faker
f = Faker()
class BusinessCard:
    
    def __init__(self, name, surname, company, job_title, email):
           
        self.name = name
        self.surname = surname
        self.company = company
        self.job_title = job_title
        self.email = email
        self.all = name,surname,company,job_title,email     

    def __str__(self):
        return f"{self.name} {self.surname} {self.email}"

    def __repr__(self):
        return f"BusinessCard(name={self.name} surname={self.surname} company={self.company} job_title={self.job_title} email={self.email})"

    def contact(self):
        print(f"Kontaktuj się z ... {self.name} {self.surname} {self.job_title} {self.email}")

    @property
    def full_length(self):
        name_len = len(self.name)
        surname_len = len(self.surname)
        return name_len + surname_len +1      
  
card_a = BusinessCard(name="Ronan",surname="Gray",company="Dee's Drive-In",job_title="Tree trimmer",email="RonanGray@teleworm.us")
card_b = BusinessCard(name="Hector",surname="Aitken",company="Mansmann's Department Store",job_title="Diagnostic medical sonographer",email="HectorAitken@teleworm.us")
card_c = BusinessCard(name="Rosie",surname="Black",company="Steve & Barry's",job_title="Segmental paver",email="RosieBlack@dayrep.com")
card_d = BusinessCard(name="Belinda",surname="Banks",company="Benesome",job_title="Dressing room attendant",email="BelindaBanks@jourrapide.com")
card_e = BusinessCard(name="Kazimiera",surname="Kowalczyk",company="National Lumber",job_title="Nannie",email="KazimieraKowalczyk@armyspy.com")
card_x = BusinessCard(name = f.first_name(), surname = f.last_name(), company = f.company(), job_title = f.job(), email = f.email())

#sorting cards
cards = [card_a, card_b, card_c, card_d, card_e, card_x]

by_name = sorted(cards, key=lambda BusinessCard: BusinessCard.name)
by_surname = sorted(cards, key=lambda BusinessCard: BusinessCard.surname)
by_email = sorted(cards, key=lambda BusinessCard: BusinessCard.email) 

for card in cards:
    print(f"{card.name} {card.surname}: {card.company}, {card.email}")
print("-"*60)


card_b.contact()
print(f"Print will take up to {card_b.full_length} characters")



#for card in by_name:
#    print(card)
#print(by_name)
#print("-"*60)
#for card in by_surname:
#    print(card)
#print(by_surname)
#print("-"*60)
#for card in by_email:
#    print(card)
#print(by_email)
#print("-"*60)
#print(card_d)
#print(cards)