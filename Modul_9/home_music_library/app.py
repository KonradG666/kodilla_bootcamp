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


@app.route("/delete/<int:song_id>")
def delete_song(song_id):
    song = songs.delete(song_id)
    if not song:
        abort(404)
        
    return render_template("index.html", form=form, songs=songs.all(), error=error)


@app.route("/update/<int:song_id>", methods=["PUT"])
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















@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request', 'status_code': 400}), 400)









if __name__ == "__main__":
    app.run(debug=True)