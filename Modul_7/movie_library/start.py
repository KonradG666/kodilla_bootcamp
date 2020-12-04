import all_func
import main

def run():
    print("\t\tBibloteka filmów\n"+"\t\t"+"-"*16)
    generate_views()
    print(f"Najpopularniejsze filmy i seriale dnia {now}\n"+"\t\t"+"*"*10)
    top_titles()
    print("-"*60 + "\n \t\tMain Menu\n")
    menu()

run()