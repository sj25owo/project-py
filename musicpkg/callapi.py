def verify_spotipy() :
    try:
        import spotipy
    except ImportError: # 스포티파이 API import 해보고 설치가 안 되어있을 경우 설치 후 import
        import subprocess
        import sys
        subprocess.check_call([sys.executable, "-m", "pip", "install", "spotipy"])
        import spotipy
