library = [
    mov_1 = Movie(title = "Mad Max 2", release = "1981", genre = "action", watch = 0),
    mov_2 = Movie(title = "Die Hard", release = "1988", genre = "action", watch = 0),
    mov_3 = Movie(title = "Nausicaa of the Valley of the Wind", release = "1984", genre = "animation", watch = 0),
    mov_4 = Movie(title = "Castle in the Sky", release = "1986", genre = "animation", watch = 0),
    mov_5 = Movie(title = "Monty Python's Life of Brian", release = "1979", genre = "comedy", watch = 0),
    mov_6 = Movie(title = "Blade Runner", release = "1982", genre = "syfy", watch = 0),
    seri_1 = TvSeries(title = "The Soptanos", release = "1999", genre = "crime", episode = "E01", season = "S01", watch = 0),
    seri_2 = TvSeries(title = "The Office", release = "2005", genre = "sitcom", episode = "E02", season = "S04", watch = 0),
    seri_3 = TvSeries(title = "Doctor Who", release = "1963", genre = "syfy", episode = "E01", season = "S08", watch = 0),
    seri_4 = TvSeries(title = "Battlestar Galactica", release = "2004", genre = "syfy", episode = "E04", season = "S02", watch = 0),
    seri_5 = TvSeries(title = "South Park", release = "1997", genre = "animation", episode = "E05", season = "S14", watch = 0),
    seri_6 = TvSeries(title = "Fawlty Towers", release = "1975", genre = "sitcom", episode = "E03", season = "S02", watch = 0)
    ]

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

movie1 = Movie(title="Requiem",release = 1997, genre = "Nori", watched = 0)
movie2 = Movie(title="Requiem",release = 1997, genre = "Nori", watched = 0)
series = TvSeries(title = "The Bob", release = 2000, genre = "triller", episode= "E05", season = "S02", watched= 0)


print(f"movie1 {movie1.current_views}")
movie1.play(100)
print(f"movie1 {movie1.current_views}")
print(f"movie2 {movie2.current_views}")
movie2.play(10)
print(f"movie2 {movie2.current_views}")

def get_movies():
    pass

def get_series():
    pass

def search():
    pass

def generate_viewes():
    pass

def top_titles():
    pass