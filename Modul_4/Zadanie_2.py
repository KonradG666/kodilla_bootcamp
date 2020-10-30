def customized_hello(first_name, last_name, gender_prefix = "Mr"):
    print(f"Hello {gender_prefix} {first_name} {last_name} !!!")

customized_hello("John", "Cleese")
customized_hello("Clara", "Cleese")
customized_hello("Clara", "Cleese", "Ms")