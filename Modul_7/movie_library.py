#movies library
from random import randint
import time

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

now = time.strftime("%d/%m/%Y")

class Movie():
    
    def __init__(self, title, release, genre, watched):
        self.title = title
        self.release = release
        self.genre = genre
        self.watched = watched        

    def __str__(self):
        return f"{self.title} - {self.release}"     # : has been watched: {self.watched}"

    def __repr__(self):
        return f"Movie: {self.title}\n - released in: {self.release}\n - genre: {self.genre}"

    @property
    def current_views(self):
        return self.watched
    
    def play(self, step):
        self.watched += step

class TvSeries(Movie):
    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.episode = episode
        self.season = season

    def __str__(self):
        return f"{self.title}: {self.season}{self.episode}"     # - has been watched: {self.watched}"

    def __repr__(self):
        return f"Series: {self.title}\n - first aired: {self.release}\n - genre: {self.genre}\n - content: {self.season}{self.episode}"

main_library = [
    Movie(title = "Mad Max 2", release = "1981", genre = "action", watched = 0),
    Movie(title = "Die Hard", release = "1988", genre = "action", watched = 0),
    Movie(title = "Nausicaa of the Valley of the Wind", release = "1984", genre = "animation", watched = 0),
    Movie(title = "Castle in the Sky", release = "1986", genre = "animation", watched = 0),
    Movie(title = "Monty Python's Life of Brian", release = "1979", genre = "comedy", watched = 0),
    Movie(title = "Blade Runner", release = "1982", genre = "syfy", watched = 0),
    TvSeries(title = "The Sopranos", release = "1999", genre = "crime", episode = "E01", season = "S01", watched = 0),
    TvSeries(title = "The Office", release = "2005", genre = "sitcom", episode = "E02", season = "S04", watched = 0),
    TvSeries(title = "Doctor Who", release = "1963", genre = "syfy", episode = "E01", season = "S08", watched = 0),
    TvSeries(title = "Battlestar Galactica", release = "2004", genre = "syfy", episode = "E04", season = "S02", watched = 0),
    TvSeries(title = "South Park", release = "1997", genre = "animation", episode = "E05", season = "S14", watched = 0),
    TvSeries(title = "Fawlty Towers", release = "1975", genre = "sitcom", episode = "E03", season = "S02", watched = 0)
    ]

def get_movies():
    for row in main_library:
        if isinstance(row, Movie):
            print(f"- {row.title}")

def get_series():
    for row in main_library:        
        if isinstance(row, TvSeries):            
            print(f"- {row.title}")   
def search():
    look_up = input("What you are looking for? ")
    for i,v in enumerate(main_library):
        if v.title == look_up:
            print(main_library[i].__repr__())
def top_titles():
    for i,v in enumerate(main_library):
        if v.watched > 0:
            print(f"{v} with {v.watched} views")
            
top_titles()
#generator
def generate_views(times = 10):
    for i in range(times):
        index = random_element()
        add_views(index)
        current_views = main_library[index].current_views
        title = main_library[index].title
        #print(f"View generated for {title} ({current_views})")

def random_element():
    elements =len(main_library) 
    return randint(0, elements-1)

def add_views(index):
    views = randint(1,100)
    return main_library[index].play(views)

#print library
def show_library():
    print("Main Library:")
    for i,v in enumerate(main_library):
        print(f"- {v}")

def menu():
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
def run():
    print("\t\tBibloteka filmów\n"+"\t\t"+"-"*16)
    generate_views()
    print(f"Najpopularniejsze filmy i seriale dnia {now}\n"+"\t\t"+"*"*10)
    top_titles()
    print("-"*60 + "\n \t\tMain Menu\n")
    menu()

run()
