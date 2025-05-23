def verify_spotipy() :
    try:
        import spotipy
    except ImportError:
        import subprocess
        import sys
        subprocess.check_call([sys.executable, "-m", "pip", "install", "spotipy"])
        import spotipy