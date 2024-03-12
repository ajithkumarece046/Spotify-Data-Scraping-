import spotipy
from credentials import client_access_id,client_secret_id
from spotipy.oauth2 import SpotifyClientCredentials

# Replace 'your_client_id' and 'your_client_secret' with your actual credentials
auth_manager = SpotifyClientCredentials(client_id=client_access_id, client_secret=client_secret_id)
sp = spotipy.Spotify(auth_manager=auth_manager)

user_id=input("Enter the user id:")

playlist_id_list=[]

user_data=sp.user_playlists(user_id)
user_data_items=user_data['items']

for data in user_data_items:
    item1=data['id']
    playlist_id_list.append(item1)


