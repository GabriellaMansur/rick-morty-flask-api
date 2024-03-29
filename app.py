from flask import Flask, render_template, jsonify
import urllib.request, json

app = Flask(__name__)

@app.route("/")
def get_list_characters_page():
    url = "https://rickandmortyapi.com/api/character"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template("characters.html", characters=dict["results"])

@app.route("/profile/<id>")
def get_profile(id):
    url = f"https://rickandmortyapi.com/api/character/{id}"
    response = urllib.request.urlopen(url)
    data = response.read()
    profile_dict = json.loads(data)

    return render_template("profile.html", profile=profile_dict)

@app.route("/locations")
def get_list_locations():
    url = "https://rickandmortyapi.com/api/location"
    response = urllib.request.urlopen(url)
    data = response.read()
    locations_dict = json.loads(data)

    return render_template("locations.html", locations=locations_dict['results'])

@app.route("/lista")
def get_list_characters():
    url = "https://rickandmortyapi.com/api/character"
    response = urllib.request.urlopen(url)
    characters = response.read()
    dict = json.loads(characters)

    characters = []

    for character in dict["results"]:
        character = {
            "name": character["name"],
            "status": character["status"]
        }

        characters.append(character)

    return {"characters": characters}