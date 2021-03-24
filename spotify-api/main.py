from requests import auth
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json 

client_id = ''
client_secret = ''

def authenticate():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret,
    redirect_uri='hosting-songs-login://callback', scope='user-read-recently-played'))
    results = sp.current_user_recently_played()
    for idx, item in enumerate(results['items']):
        track = item['track']
        print(idx, track['artists'][0]['name'], "-", track['name']) 
        

if __name__ == "__main__":
    authenticate()