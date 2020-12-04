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