from random import randint
import all_func
import class_file

OP_MOVIES = 1
OP_SERIES = 2
OP_SEARCH = 3
OP_GENERATE = 4
OP_TOP = 5
OP_SHOW = 6
OP_EXIT = 7

ACTIONS = {
    OP_MOVIES: "Get movies",
    OP_SERIES: "Get series",
    OP_SEARCH: "Search",
    OP_GENERATE: "Generate views",
    OP_TOP: "Top titles",
    OP_SHOW: "Library",
    OP_EXIT: "Exit"
}

ALLOWED_ACTIONS = [str(i) for i in ACTIONS.keys()]
MENU_ITEMS = [f"{index} - {action}" for index, action in ACTIONS.items()]

def run():
    while True:
        op = input("Choose your action from:\n" + "\n".join(MENU_ITEMS) + "\n")
        if op not in ALLOWED_ACTIONS:
            print("Input error. Try again.")
            continue
        #menu
        op = int(op)
        if op == OP_EXIT:
            print("Good Bye!")
            exit(0)
        elif op == OP_GENERATE:
            generate_views()
        elif op == OP_MOVIES:
            print("List of movies:")
            movies = get_movies()
        elif op == OP_SERIES:
            print("List of series:")
            series = get_series()
        elif op == OP_SEARCH:
            search()
        elif op == OP_TOP:
            top_titles()            
        elif op == OP_SHOW:
            show_library()
#start
run()