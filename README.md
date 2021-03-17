# Songs-service

// Sukurti image "songs-image"
docker build -t songs-image .

// Paleisti image "songs-image" per porta 5000, (sukuria container "songs-container")
docker run --name songs-container -p 5000:5000 songs-image

// Pakartotinai (pries tai isjungus) paleisti container "songs-container"
docker start songs-container

Servisas pasiekiamas adresu localhost:5000

Serviso aptarnaujami resursai - songs.

SONG DATA STRUCTURE:

id - unique number
artist - artist name
name - song name
date_created - release date
link - youtube url

RESTFUL API:

(curl - command-line tool for transferring data using various network protocols)

(READ ALL)
GET http://localhost:5000/songs
pvz: curl http://localhost:5000/songs -X GET

(READ)
GET http://localhost:5000/songs/<songs_id>
pvz: curl http://localhost:5000/songs/1 -X GET

(ADD)
POST http://localhost:5000/songs
pvz: curl http://localhost:5000/songs -d '{"name":"daina", "artist":"muzikantas", "date_created":"2018-02-03", "link":"www.google.com"}' -H "Content-Type: application/json" -X POST

(REMOVE)
DELETE http://localhost:5000/songs/<songs_id>
pvz: curl http://localhost:5000/songs/12 -X DELETE

(UPDATE)
PUT http://localhost:5000/songs/<songs_id>
curl http://localhost:5000/songs/<12> -d '{"name":"daina2", "artist":"muzikantas2", "date_created":"2018-02-03", "link":"www.google.com"}' -H "Content-Type: application/json" -X PUT
