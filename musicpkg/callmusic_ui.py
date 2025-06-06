import tkinter as tk
from musicpkg import callmusic
from PIL import Image, ImageTk
import requests
from io import BytesIO
import webbrowser

def recom_music(x) :
    access_token = callmusic.get_access_token()
    sp = callmusic.create_spotify_client(access_token)

    limit = 50
    offset = 0
    tracks = []
    index = 0
    music_url = ""

    root = tk.Toplevel()
    root.title("테스트 기반 음악 추천")

    album_img_label = tk.Label(root)
    album_img_label.pack(pady=10)

    info_label = tk.Label(root, text="", font=("Helvetica", 12), wraplength=400, justify="left")
    info_label.pack(pady=10)

    def load_tracks(genre):
        nonlocal tracks, offset, index
        result = sp.search(q=f"genre:{genre}", type='track', limit=limit, offset=offset)
        tracks = result['tracks']['items']
        index = 0
        offset += limit

    def show_next_track():
        nonlocal index, music_url, album_img_label

        if index >= len(tracks):
            load_tracks()
            if not tracks:
                info_label.config(text="더 이상 곡이 없습니다.")
                return

        track = tracks[index]
        name = track['name']
        artist = track['artists'][0]['name']
        album = track['album']['name']
        release = track['album']['release_date']
        music_url = track['external_urls']['spotify']

        image_url = track['album']['images'][0]['url']
        img = Image.open(BytesIO(requests.get(image_url).content)).resize((200, 200))
        album_img = ImageTk.PhotoImage(img)
        album_img_label.config(image=album_img)
        album_img_label.image = album_img

        info_label.config(text=f"🎵 곡명: {name}\n🎤 아티스트: {artist}\n💿 앨범: {album}\n📅 발매일: {release}")
        index += 1

    def open_in_browser():
        if music_url:
            webbrowser.open(music_url)

    next_button = tk.Button(root, text="다음 곡 보기", command=show_next_track)
    next_button.pack(pady=5)

    open_button = tk.Button(root, text="브라우저에서 열기", command=open_in_browser)
    open_button.pack(pady=5)

    load_tracks(x)
    show_next_track()

    root.mainloop()
