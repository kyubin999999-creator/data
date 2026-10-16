import os
import pandas as pd

# 1. 저장소 내 상대 경로
LOCAL_FILE_PATH = "2026년 09월  교통카드 통계자료 (1).xls"

# 2. GitHub Raw URL (외부 환경/코랩용)
RAW_URL = "https://raw.githubusercontent.com/kyubin999999-creator/data/main/2026%EB%85%84%2009%EC%9B%94%20%20%EA%B5%90%ED%86%B5%EC%B9%B4%EB%93%9C%20%ED%86%B5%EA%B3%84%EC%9E%90%EB%A3%8C%20(1).xls"

def load_traffic_data():
    """
    로컬 파일이 존재하면 로컬 경로에서,
    없으면 GitHub Raw URL에서 엑셀 데이터를 불러옵니다.
    """
    target_path = LOCAL_FILE_PATH if os.path.exists(LOCAL_FILE_PATH) else RAW_URL
    print(f"데이터 불러오는 위치: {target_path}")

    try:
        df = pd.read_excel(target_path, engine="xlrd")
    except Exception as e:
        print(f"xlrd 엔진 로드 실패로 기본 엔진 재시도: {e}")
        df = pd.read_excel(target_path)

    return df

if __name__ == "__main__":
    df = load_traffic_data()
    print("\n--- 데이터 로드 성공 ---")
    print(f"데이터 크기 (행, 열): {df.shape}")
    print(df.head())
