def hello_you():

    prefix = input("Please tell me: Mr/Mrs/Ms?")
    first_name = input("Your name?: ")
    last_name = input("Yours last name?: ")
    age_check = int(input("Your age please: "))
    if age_check >= 18:
        print(f"Hello {prefix} {first_name} {last_name} how you doin'?")
    else:
        print(f"Hello {prefix} {first_name} {last_name}")

hello_you()