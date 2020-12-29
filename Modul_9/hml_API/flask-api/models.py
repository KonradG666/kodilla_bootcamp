import json


class Songs:
    def __init__(self):
        try:
            with open("songs.json", "r") as f:
                self.songs = json.load(f)
        except FileNotFoundError:
            self.songs = []

    def all(self):
        song = [song for song in self.all() if song['id'] == id]
        if song:
            return song[0]
        return []

    def get(self, id):
        return self.songs[id]

    def create(self, data):
        data.pop('csrf_token')
        self.songs.append(data)

    def save_all(self):
        with open("songs.json", "w") as f:
            json.dump(self.songs, f)

    def update(self, id, data):
        data.pop('csrf_token')
        self.songs[id] = data
        self.save_all()

    def delete(self, id):
        song = self.get(id)
        if song:
            self.songs.remove(song)
            self.save_all()
            return True
        return False


songs = Songs()