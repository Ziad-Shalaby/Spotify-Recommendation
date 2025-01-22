import streamlit as st
import pickle as pkl
import requests

# Set page config
st.set_page_config(page_title='Songs Recommendation System', layout='wide')
st.header('Songs Recommendation System 🎶')

# Load data
if 'songs' not in st.session_state:
    st.session_state['songs'] = pkl.load(open(r'songs.pkl', 'rb'))
    st.session_state['similarity'] = pkl.load(open(r'similarity.pkl', 'rb'))

songs = st.session_state['songs']
similarity = st.session_state['similarity']
songs_list = songs['name'].values

selectvalue = st.selectbox("Select a song from the dropdown", songs_list)

CLIENT_ID = "f6ebe282a1a94f2c8c39ca58c88a54cd"  
CLIENT_SECRET = "9d219328d2d74b3f87db59425f40b750"  

# Function to fetch Spotify API token
@st.cache_data
def get_spotify_token(client_id, client_secret):
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret
    }
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        return response.json()['access_token']
    else:
        st.error("Failed to fetch Spotify token")
        return None

# Function to fetch album art from Spotify
def fetch_album_art(song_name):
    token = get_spotify_token(CLIENT_ID, CLIENT_SECRET)
    if token is None:
        return None

    url = "https://api.spotify.com/v1/search"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    params = {
        "q": song_name,
        "type": "track",
        "limit": 1
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        tracks = response.json().get('tracks', {}).get('items', [])
        if tracks:
            return tracks[0]['album']['images'][0]['url']  # High-res album art
    return None

# Recommendation function
def recommend(song):
    index = songs[songs['name'] == song].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
    recommend_songs_names = []
    recommend_artist_names = []
    recommend_songs_links = []
    recommend_songs_posters = []

    for i in distances[0:6]:
        recommend_songs_names.append(songs.iloc[i[0]]['name'])
        recommend_artist_names.append(songs.iloc[i[0]]['artist'])
        recommend_songs_links.append(songs.iloc[i[0]]['spotify_preview_url'])
        # Fetch album art dynamically
        poster_url = fetch_album_art(songs.iloc[i[0]]['name'])
        recommend_songs_posters.append(poster_url or "https://via.placeholder.com/150")  # Fallback image if poster not found

    return recommend_songs_names, recommend_artist_names, recommend_songs_links, recommend_songs_posters

# Streamlit UI
if st.button('Show Recommendations'):
    songname, artistname, songlink, songposter = recommend(selectvalue)
    cols = st.columns(len(songname))

    for col, name, artist, link, poster in zip(cols, songname, artistname, songlink, songposter):
        with col:
            st.text(name)
            st.text(artist)
            st.markdown(
                f'<a href="{link}" target="_blank"><img src="{poster}" width="100%"></a>',
                unsafe_allow_html=True
            )
