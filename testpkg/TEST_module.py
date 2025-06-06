def determine_input(question):
    while True:
        answer = input(question).strip().upper()
        if answer in ["Y", "N"]:
            return answer
        else:
            print("Y 또는 N을 입력해주세요.")


def music_test() :
    print ("안녕하세요:) 테스트 중심 음악 추천 프로그램 입니다. \n당신의 취향에 맞는 노래를 추천해드려요! \n질문에 맞게 Y/N 로 대답해주세요!")

    genre_result = "" #  api에 적용하기 위해서 변수 생성

    A1 = input("Q. 밝은 분위기의 노래를 선호하시나요? (Y/N)").strip().upper() 
    # 1. A1으로 한 이유는 질문이 너무 많아서 축약 했어요
    # 2. strip() 은 공백제거 3. upper은 대문자로 변환
    
    if A1 == "Y" :
        A2 = determine_input("Q. 리듬감 있는 음악을 선호하시나요? (Y/N)").strip().upper() 
        if A2 == "Y" :
            A3 = determine_input("Q. 아이돌 스타일의 음악을 선호하시나요? (Y/N)").strip().upper() 
            if A3 == "Y" :
                result = "k-pop" #최종 결과를 result에 넣어서 result를 메인으로 부르기!
            else:
                A4 = determine_input("Q. 밴드사운드를 선호하시나요? (Y/N)").strip().upper()
                if A4 == "Y" :
                    A5 = determine_input("Q. 랩처럼 리듬감있는 음악을 선호하시나요? (Y/N)").strip().upper()
                    if A5 == "Y" :
                        result = "hip-hop"
                    else :
                        result = "rock"
                else : 
                    result = "dance pop"
        else :
            A6 = determine_input("Q. 부드러운 목소리의 음악을 선호하시나요? (Y/N)").strip().upper()
            if A6 == "Y" :
                result = "indie pop"
            else : result = " pop"
    elif A1 == "N" :
        A7 = determine_input("Q. 가사를 중요하게 생각하시나요? (Y/N)").strip().upper()
        if A7 == "Y" :
            result = "ballad"
        else :
            A8 = determine_input("Q. 악기 연주가 중심인 음악을 선호하시나요? (Y/N)").strip().upper()
            if A8 == "Y":
                A9 = determine_input("Q. 클래식 연주를 선호하시나요? (Y/N)").strip().upper()
                if A9 == "Y" :
                    result = "classical"
                else : 
                    result = "jazz"
            else : 
                result = "acostic"
    else :
        print ("Y 또는 N을 입력해주세요")
        result = "None"

    return result
