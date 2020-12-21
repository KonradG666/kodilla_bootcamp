from flask import Flask, request, render_template, redirect, url_for
from forms import MusicLibrary
from models import songs

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"

@app.route("/", methods=["GET", "POST"])
@app.route("/index.html/", methods=["GET", "POST"])
def songs_list():
    form = MusicLibrary()
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            songs.create(form.data)
            songs.save_all()
        return redirect(url_for("songs_list"))
    
    return render_template("index.html", form=form, songs=songs.all(), error=error)


@app.route("/index/<int:song_id>/", methods=["GET", "POST"])
def song_details(song_id):
    print("dupa")
    song = songs.get(song_id - 1)
    form = Songs(data=song)

    if request.method == "POST":
        if form.validate_on_submit():
            songs.update(song_id - 1, form.data)
        return redirect(url_for("songs_list"))
    return render_template("index.html", form=form, song_id=song_id)



@app.route("/index/<int:song_id>", methods=['DELETE'])
def delete_song(song_id):
    result = songs.delete(song_id)
    if not result:
        abort(404)
    return jsonify({'result': result})


@app.route("/index/<int:song_id>", methods=["PUT"])
def update_song(song_id):
    song = songs.get(song_id)
    if not song:
        abort(404)
    if not request.json:
        abort(400)
    data = request.json
    if any([
        'title' in data and not isinstance(data.get('title'), str),
        'band' in data and not isinstance(data.get('band'), str),
        'genre' in data and not isinstance(data.get('genre'), str)
    ]):
        abort(400)
    song = {
        'title': data.get('title', song['title']),
        'band': data.get('band', song['band']),
        'genre': data.get('genre', song['genre'])
    }
    song.update(song_id, song)
    return jsonify({'song': song})



if __name__ == "__main__":
    app.run(debug=True)