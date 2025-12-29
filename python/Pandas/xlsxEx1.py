import pandas as pd
import numpy as np
import os

# 1. 엑셀 데이터를 딕셔너리 형태로 변환
data = {
    '반': ['A반', 'B반', 'A반', 'B반', 'A반', 'A반', 'B반', 'B반', 'A반', 'B반'],
    '이름': ['구이서', '김이정', '오지수', '김선우', '하진희', '강현진', '김진솔', '박서준', '김성희', '이지서'],
    '성별': ['남', '여', '남', '남', '여', '남', '남', '여', '남', '여'],
    '국어': [90.0, 78.0, np.nan, 33.0, 0.0, np.nan, 90.0, 78.0, np.nan, 86.0],
    '수학': [89.0, 45.0, np.nan, 44.0, 85.0, np.nan, 89.0, 45.0, np.nan, 100.0],
    '응시여부': ['응시', '응시', '응시', '응시', '응시', np.nan, '응시', '응시', np.nan, '응시'],
    '확인여부': ['확인', '확인', '확인', np.nan, np.nan, np.nan, '확인', '확인', '확인', '확인']
}

# 2. 데이터프레임 생성
df = pd.DataFrame(data)

# 3. 현재 파일이 있는 위치에 data.xlsx로 저장
cur_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(cur_dir, 'data.xlsx')

df.to_excel(file_path, index=False)

print(f"파일 생성 완료: {file_path}")