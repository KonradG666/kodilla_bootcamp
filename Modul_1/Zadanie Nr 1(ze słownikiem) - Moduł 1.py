text = """– Czemu tak ciągle gadasz o kobietach, Stan?
– Bo chcę zostać kobietą. Chcę być kobietą. Chce żebyście od dziś mówili na mnie „Loretta”. To moje niezbywalne prawo jako mężczyzny.
– Ale dlaczego chcesz zostać Lorettą, Stan?
– Bo chcę mieć dzieci.
– Dzieci?
– Każdy mężczyzna ma prawo mieć dzieci, jeśli chce.
– Przecież ty nie możesz mieć dzieci!
– Nie prześladuj mnie!
– Nie prześladuję cię, Stan! Nie masz macicy! Gdzie będziesz trzymał swojego embriona? W pudełku?
– Mam pomysł! Przyjmijmy, że Stan nie może póki co mieć dzieci, gdyż nie ma macicy, co nie jest niczyją winą, nawet Rzymian, ale musimy przyznać, że ma prawo do dzieci!
– Świetnie, Judith! Będziemy walczyć z ciemiężycielami…
– Przepraszam.
– A po co?
– Co po co?
– Po co walczyć o jego prawo do posiadania dzieci…
– To symbol naszej beznadziejnej walki z najeźdźcą.
– Symbol jego beznadziejnej walki z rzeczywistością."""

number_of_a = {"a": 0}
number_of_e = {"e": 0}
number_of_i = {"i": 0}
number_of_o = {"o": 0}
number_of_u = {"u": 0}
number_of_y = {"y": 0}

for letter in text:
  # if want to count all letters use second call
#for letter in text.lower():

    if letter == "a":
        number_of_a["a"] += 1
    elif letter == "e":
        number_of_e["e"] += 1
    elif letter == "i":
        number_of_i["i"] += 1
    elif letter == "o":
        number_of_o["o"] += 1
    elif letter == "u":
        number_of_u["u"] += 1
    elif letter == "y":
        number_of_y["y"] += 1
    else:
        pass

print(f"number of a =", number_of_a["a"])
print(f"number of e =", number_of_e["e"])
print(f"number of i =", number_of_i["i"])
print(f"number of o =", number_of_o["o"])
print(f"number of u =", number_of_u["u"])
print(f"number of y =", number_of_y["y"])
