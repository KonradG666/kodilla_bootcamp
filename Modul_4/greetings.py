import sys

def say_hello(first_name, last_name, prefix):

    #first_name = input("What is your name?")
    #last_name = input("What is your last name?")
    print(f"Hello {prefix} {first_name} {last_name}!")

if __name__ == "__main__":
    if len(sys.argv) > 4:
        exit(1)
    first_name = sys.argv[1]
    last_name = sys.argv[2]
    prefix = sys.argv[3]
    say_hello(first_name, last_name, prefix)
