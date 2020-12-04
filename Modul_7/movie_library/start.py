import utils
import main
from utils import top

def run():
    print("\t\tBibloteka filmów\n"+"\t\t"+"-"*16)
    utils.generate_views()
    print(f"Najpopularniejsze filmy i seriale z dnia {utils.now}\n"+"to:")
    utils.top_titles()
    utils.top_3(top)
    print("-"*60 + "\n \t\tMain Menu\n")
    main.menu()

run()