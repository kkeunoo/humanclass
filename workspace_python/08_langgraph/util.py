from pathlib import Path
import pandas as pd
import traceback

def load_csv(fileName) :
    BASE_DIR = Path(__file__).resolve().parents[0] # 08_langgraph 폴더로 이동
    DOCUMENT_FILE = BASE_DIR / "data" / "ml-latest-small" / fileName
    # print(DOCUMENT_FILE)

    frame = None
    try:
        frame = pd.read_csv(DOCUMENT_FILE)
    except Exception as e :
        traceback.print_exc()
        print('read_csv 파일 로딩 오류', e)

    return frame