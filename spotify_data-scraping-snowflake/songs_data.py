import spotipy
from credentials import client_access_id, client_secret_id
from spotipy.oauth2 import SpotifyClientCredentials
from playlist_id import playlist_id_list
import csv

# Replace 'your_client_id' and 'your_client_secret' with your actual credentials
auth_manager = SpotifyClientCredentials(client_id=client_access_id, client_secret=client_secret_id)
sp = spotipy.Spotify(auth_manager=auth_manager)

for playlist_id in playlist_id_list:
    tracks_data = sp.playlist_tracks(playlist_id)
    print("Playlist ID:", playlist_id)
    print("Total tracks:", len(tracks_data['items']))
    file_name = input("Enter the file name: ")
    with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Song_name', 'Album_name'])
        for item in tracks_data['items']:
            song_name = item['track']['name']
            album_name = item['track']['album']['name']
            csv_writer.writerow([song_name, album_name])
