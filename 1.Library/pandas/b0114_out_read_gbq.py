# pip install pandas-gbq
import pandas as pd
import os

# 서비스 계정 인증
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path_to_your_service_account_json_file.json"

# Google Cloud 프로젝트 ID
project_id = "your-project-id"

# BigQuery에서 SQL 쿼리 실행
query = """
    SELECT name, age
    FROM `your-project-id.dataset_name.table_name`
    WHERE age > 25
"""

# BigQuery에서 데이터를 읽어와 DataFrame으로 변환
df = pd.read_gbq(query, project_id=project_id, dialect='standard')

# 결과 출력
print("DataFrame from BigQuery:")
print(df)
