import base64
import requests
import spotipy
import random

def get_access_token(): # 스포티파이 API 사용 위해 토큰 발급(홈페이지에 나와있는 방식 그대로)
    client_id = '963c5f6c205b4912a1be1c661595d6a8'
    client_secret = '5ab21414c3b64b318e6d987c5e4cde36'
    redirect_url = "http://127.0.0.1:8888/callback"

    encoded = base64.b64encode(f'{client_id}:{client_secret}'.encode('utf-8')).decode('ascii')
    headers = {'Authorization': f'Basic {encoded}'}

    token_url = "https://accounts.spotify.com/api/token"
    payload = {'grant_type': 'client_credentials'}
    response = requests.post(token_url, data=payload, headers=headers)
    access_token = response.json()['access_token']
    return access_token

def create_spotify_client(access_token):
    return spotipy.Spotify(auth=access_token)

def search_tracks(genre, total=100, sample_size=10):
    access_token = get_access_token()
    sp = create_spotify_client(access_token)

    results1 = sp.search(q=f'genre:{genre}', limit=50, type='track')
    # genre:(검색할 장르) 형태로 검색
    tracks1 = results1['tracks']['items']

    results2 = sp.search(q=f'genre:{genre}', limit=50, offset=50, type='track')
    tracks2 = results2['tracks']['items']
    # offset: 이미 앞에서 50개의 음악 정보를 불러왔기 때문에 그만큼 건너뛰고 검색

    all_tracks = tracks1 + tracks2
    # 스포티파이 api에서 음악 정보를 최대 50개까지 불러올 수 있어서 나눠서 검색

    sampled_tracks = random.sample(all_tracks, min(sample_size, len(all_tracks)))
    # 설정한 음악 개수만큼 print

    print(f"장르 '{genre}'에서 랜덤으로 뽑은 {len(sampled_tracks)}개의 추천 음악:")
    for i, track in enumerate(sampled_tracks):
        print(f"\n{i + 1}. {track['name']} by {track['artists'][0]['name']}")
        print(f"   앨범: {track['album']['name']}")
        print(f"   발매일: {track['album']['release_date']}")
        print(f"   링크: {track['external_urls']['spotify']}")
        # name, external_urls, release_date 등은 이미 스포티파이에서 지정한 변수명
