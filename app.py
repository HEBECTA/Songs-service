from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///songs.dbs'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

class Songs(db.Model):
    __tablename__ = 'songs'
    id = db.Column(db.Integer, primary_key=True)
    artist = db.Column(db.String(30), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    date_created = db.Column(db.Date, nullable=False, default='N/A')
    link = db.Column(db.String(500))

    def __init__(self, artist, name, date_created, link):
        self.artist = artist
        self.name = name
        self.date_created = date_created
        self.link = link

    def __repr__(self):
        return 'id {}'.format(self.id)


@app.route('/songs', methods=['GET'])
def get_all():
    songs = Songs.query.all()
    output = []
    for song in songs:
        currSong = {}
        currSong['id'] = song.id
        currSong['artist'] = song.artist
        currSong['name'] = song.name
        currSong['date_created'] = song.date_created
        currSong['link'] = song.link
        output.append(currSong)
    return jsonify(output)

# curl http://localhost:5000/songs -X POST

@app.route('/songs/<song_id>', methods=['GET'])
def fetch(song_id):
    song = Songs.query.get_or_404(song_id)
    output = []
    currSong = {}
    currSong['id'] = song.id
    currSong['artist'] = song.artist
    currSong['name'] = song.name
    currSong['date_created'] = song.date_created
    currSong['link'] = song.link
    output.append(currSong)
    return jsonify(output)

# curl http://localhost:5000/songs/1 -X POST

@app.route('/songs', methods=['POST'])
def add():
    songData = request.get_json()
    date = datetime.strptime(songData['date_created'], "%Y-%m-%d")
    song = Songs(artist=songData['artist'], name=songData['name'], date_created=date, link=songData['link'])
    db.session.add(song)
    db.session.commit()
    return jsonify(songData)

# curl http://localhost:5000/songs -d '{"name":"daina", "artist":"muzikantas", "date_created":"2018-02-03", "link":"www.google.com"}' -H "Content-Type: application/json" -X POST


@app.route('/songs/<song_id>', methods=['DELETE'])
def delete(song_id):
    song = Songs.query.get_or_404(song_id)
    output = []
    currSong = {}
    currSong['id'] = song.id
    currSong['artist'] = song.artist
    currSong['name'] = song.name
    currSong['date_created'] = song.date_created
    currSong['link'] = song.link
    output.append(currSong)
    db.session.delete(song)
    db.session.commit()
    return jsonify(output)

# curl http://localhost:5000/songs/12 -X DELETE

@app.route('/songs/<song_id>', methods=['PUT'])
def edit(song_id):
    song = Songs.query.get_or_404(song_id)
    songData = request.get_json()
    song.artist = songData['artist']
    song.name = songData['name']
    song.date_created = datetime.strptime(songData['date_created'], "%Y-%m-%d")
    song.link = songData['link']
    db.session.commit()
    output = []
    currSong = {}
    currSong['id'] = song.id
    currSong['artist'] = song.artist
    currSong['name'] = song.name
    currSong['date_created'] = song.date_created
    currSong['link'] = song.link
    output.append(currSong)
    return jsonify(output)

# curl http://localhost:5000/songs/12 -d '{"name":"daina2", "artist":"muzikantas2", "date_created":"2018-02-03", "link":"www.google.com"}' -H "Content-Type: application/json" -X PUT


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)