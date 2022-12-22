import json
import requests
from authentication import api_key, spotify_token
from refresh import Refresh
import lyricsgenius as lg


class saveSongs:

    def __init__(self):
        self.api_key = api_key
        self.spotify_token = ""

    def getCurrentlyPlaying(self):
        query = 'https://api.spotify.com/v1/me/player/currently-playing'
        response = requests.get(query, headers={"Content-Type": "application/json",
                                                "Authorization": "Bearer {}".format(self.spotify_token)})

        response_json = response.json()

        search = response_json["item"]["artists"][0]["name"] + \
            " " + response_json["item"]["name"]

        self.searchLyrics(search)

    def searchLyrics(self, search):

        genius = lg.Genius(self.api_key, skip_non_songs=True, excluded_terms=[
                           "(Live)"], remove_section_headers=True, verbose=True)

        song = genius.search_song(search)
        print(song.lyrics)

    def call_refresh(self):
        print("Refreshing")
        refreshCaller = Refresh()
        self.spotify_token = refreshCaller.refresh()
        self.getCurrentlyPlaying()


a = saveSongs()
a.call_refresh()
