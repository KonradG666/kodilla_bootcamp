#movies library
class Movie():
    
    def __init__(self, title, release, genre, watched):
        self.title = title
        self.release = release
        self.genre = genre
        self.watched = watched
        #vareable
        self._watched = watched        

    def __str__(self):
        return f"{self.title} {self.release}"

    @property
    def current_views(self):
        return self._watched
    
    def play(self, step=1):
        self._watched += step

class TvSeries(Movie):
    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.episode = episode
        self.season = season

    def __str__(self):
        return f"{self.title} {self.season}{self.episode}"

main_library = [
    Movie(title = "Mad Max 2", release = "1981", genre = "action", watched = 0),
    Movie(title = "Die Hard", release = "1988", genre = "action", watched = 0),
    Movie(title = "Nausicaa of the Valley of the Wind", release = "1984", genre = "animation", watched = 0),
    Movie(title = "Castle in the Sky", release = "1986", genre = "animation", watched = 0),
    Movie(title = "Monty Python's Life of Brian", release = "1979", genre = "comedy", watched = 0),
    Movie(title = "Blade Runner", release = "1982", genre = "syfy", watched = 0),
    TvSeries(title = "The Soptanos", release = "1999", genre = "crime", episode = "E01", season = "S01", watched = 0),
    TvSeries(title = "The Office", release = "2005", genre = "sitcom", episode = "E02", season = "S04", watched = 0),
    TvSeries(title = "Doctor Who", release = "1963", genre = "syfy", episode = "E01", season = "S08", watched = 0),
    TvSeries(title = "Battlestar Galactica", release = "2004", genre = "syfy", episode = "E04", season = "S02", watched = 0),
    TvSeries(title = "South Park", release = "1997", genre = "animation", episode = "E05", season = "S14", watched = 0),
    TvSeries(title = "Fawlty Towers", release = "1975", genre = "sitcom", episode = "E03", season = "S02", watched = 0)
    ]

print(f"movie1 {mov_1.current_views}")
mov_1.play(100)
print(f"movie1 {mov_1.current_views}")
print(f"movie2 {mov_2.current_views}")
mov_2.play(10)
print(f"movie2 {mov_2.current_views}")

def get_movies():
    for i in main_library:
        if i == Movie:
            return i
def get_series():
    for i in main_library:
        if i == TvSeries:
            return i
def search():
    look_up = input("Type the title you are lookig for: ")
    for i in main_library:
        if i == look_up:
            print(i)
def generate_viewes():
    pass

def top_titles():
    pass

#interface
OP_MOVIES = "get movies"
OP_SERIES = "get series"
OP_SEARCH = "search"
OP_GENERATE = "generate viewes"
OP_TOP = "top titles"
OP_EXIT = "exit"

ALLOWED_ACCTIONS = [OP_MOVIES, OP_SERIES, OP_SEARCH, OP_GENERATE, OP_TOP, OP_EXIT]

def run():
    while True:
        op = input("Choose your action from:\n- "+"\n- ".join(ALLOWED_ACCTIONS))
        if op not in ALLOWED_ACCTIONS:
            print("Input error. Try again.")
            continue
        #menu
        if op == OP_EXIT:
            exit("Good Bye!")
        elif op == OP_GENERATE:
            generate_viewes()
        elif op == OP_MOVIES:
            print(get_movies)
        elif op == OP_SERIES:
            print(get_series)
        elif op == OP_SEARCH:
            search()
        elif op == OP_TOP:
            print(top_titles)
#start
run()