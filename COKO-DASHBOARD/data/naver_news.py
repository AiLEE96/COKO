from PyNaver import Naver
from sqlalchemy import create_engine
import re

### mysql 연결
MYSQL_HOSTNAME = 'database-1.chj8bifpnqxd.ap-northeast-2.rds.amazonaws.com'  # mysql ip
MYSQL_USER = 'admin'  # user
MYSQL_PASSWORD = 'qwer1234' # pw
MYSQL_DATABASE = 'gmb_db'   # db name

connection_string = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}/{MYSQL_DATABASE}'
db = create_engine(connection_string) # db 연결

client_id = "NAVER api"
client_secret = "NAVER api"
url = "https://openapi.naver.com/v1/search/news.xml?query="

naver = Naver(client_id, client_secret)
query = "코로나 확진자" # '코로나 확진자'가 포함 된 검색
display = '10' # 출력 개수
sort = "sim"

df = naver.search_news(query=query, display=display, sort=sort)
df = df.astype({"pubDate": "datetime64"}) # 날짜데이터 타입변경
df.to_sql(name='news', con=db, if_exists = 'replace', index= False)

# if_exists
db.execute('ALTER TABLE news ADD COLUMN id INT(9) NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST;')
print(df)
print("news 갱신 완료")

# replace = 기존데이터 삭제후 새로운데이터 갱신
# append = 기존데이터 위에 덮어쓰기