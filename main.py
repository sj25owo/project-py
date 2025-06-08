def ui(): # ui로 진행
    from testpkg import TEST_ui
    from musicpkg import callmusic_ui
    from musicpkg import callapi
    callapi.verify_pillow()
    genre = TEST_ui.start_window()
    callmusic_ui.recom_music(genre)


def text(): # 터미널에서 진행
    from musicpkg.callmusic import search_tracks
    from testpkg.TEST_module import music_test
    genre = music_test()

    #text 일때 결과 불러오기
    if genre and genre.lower() != "none":
        print(f"\n 제가 추천해드리는 장르는 '{genre}'입니다")
        
        while True:
            print(" 장르에 해당되는 추천 음악을 가져올게요! \n")
            search_tracks(genre)
            
            # 다시 물어보기
            try_1 = input(" 같은 장르로 더 추천해드릴까요? (Y/N): ").strip().upper()
            if try_1 != "Y":
                print(" 다음에 또 테스트 해주세요! 다양한 장르로 추천해드릴게요! ")
                break

def question() : # 진행 플랫폼 결정
    mode = input(" 어떤것으로 지원해드릴까요? UI 모드로 실행하려면 1, 텍스트 입력 모드는 2 을 입력해주세요: ")
    if mode == "1":
        print(" UI 로 테스트를 진행할게요 ")
        ui()
    elif mode == "2":
        print(" 텍스트 로 테스트를 진행할게요 ")
        text()
    else:
        print(" 1 또는 2만 입력해주세요. ")
        question()

# 메인 실행
if __name__ == "__main__":
    from musicpkg import callapi
    callapi.verify_spotipy()
    question()
