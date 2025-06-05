def verify_spotipy() :
    try:
        import spotipy
    except ImportError:
        import subprocess
        import sys
        print("Spotipy API를 다운로드합니다.")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "spotipy"])
        import spotipy

def verify_pillow() :
    try:
        import PIL
    except ImportError:
        import subprocess
        import sys
        print("Pillow를 다운로드합니다다.")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
        import PIL
