import utils

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

def menu():
    while True:
        op = input("Choose your action from:\n" + "\n".join(MENU_ITEMS) + "\n")
        if op not in ALLOWED_ACTIONS:
            print("Input error. Try again.")
            continue

        op = int(op)
        if op == OP_EXIT:
            print("Good Bye!")
            exit(0)
        elif op == OP_GENERATE:
            utils.generate_views()
        elif op == OP_MOVIES:
            print("List of movies:")
            movies = utils.get_movies()
        elif op == OP_SERIES:
            print("List of series:")
            series = utils.get_series()
        elif op == OP_SEARCH:
            utils.search()
        elif op == OP_TOP:
            utils.top_titles()            
        elif op == OP_SHOW:
            utils.show_library()