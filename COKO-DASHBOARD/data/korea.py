import requests
import pandas as pd
import xmltodict
from sqlalchemy import create_engine
from datetime import datetime, timedelta

### mysql 연결
MYSQL_HOSTNAME = 'database-1.chj8bifpnqxd.ap-northeast-2.rds.amazonaws.com'  # mysql ip
MYSQL_USER = 'admin'  # user
MYSQL_PASSWORD = 'qwer1234' # pw
MYSQL_DATABASE = 'gmb_db'   # db name

connection_string = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}/{MYSQL_DATABASE}'
db = create_engine(connection_string)   # db 연결

new_date = datetime.now().date() - timedelta(1)
url = 'http://apis.data.go.kr/1352000/ODMS_COVID_04/callCovid04Api'
month = 30
day = datetime.now().date() - timedelta(month)

# DB에 데이터가 없는 경우
def api_to_mysql():
    for i in range(month, 0, -1):
        day = datetime.now().date() - timedelta(i)
        params = {'serviceKey': 'mzjIzYfhSW5dqdJTPqPf3RJs2SStFPYtduOgTIRFz28fZZ8iHByfnxVaEtoqiErdfjS0Mo60WUCWNWks9Z3OwQ==',
                  'apiType': 'xml',
                  'std_day': f"{day}" }

        req = requests.get(url, params=params).content
        xmlObject = xmltodict.parse(req)
        dict_data = xmlObject['response']['body']['items']['item']
        df_conf = pd.DataFrame(dict_data) # dict to pd.DataFrame
        df_conf_1 = df_conf.astype(
            {'deathCnt': 'int', "isolClearCnt": "int",
             "localOccCnt": "int", "overFlowCnt": "int", "stdDay": "datetime64"})
        df_conf_1.to_sql(name='corona', con=db, if_exists='append', index=False)
        print(day)
    print("테이블 생성")
    # 데이터 칼럼 타입 변경
    db.execute('ALTER TABLE corona ADD COLUMN id INT(9) NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST;')
    print("PK 칼럼 추가")

# DB에 데이터가 있는 경우
def new_data():
    print(new_date)
    params = {'serviceKey': 'mzjIzYfhSW5dqdJTPqPf3RJs2SStFPYtduOgTIRFz28fZZ8iHByfnxVaEtoqiErdfjS0Mo60WUCWNWks9Z3OwQ==',
              'apiType': 'xml',
              'std_day': f"{new_date}"}
    req = requests.get(url, params=params).content
    xmlObject = xmltodict.parse(req)
    dict_data = xmlObject['response']['body']['items']['item']
    df_conf = pd.DataFrame(dict_data) # dict to pd.DataFrame
    df_conf_1 = df_conf.astype(
        {'deathCnt': 'int', "isolClearCnt": "int",
         "localOccCnt": "int", "overFlowCnt": "int", "stdDay": "datetime64"})
    df_conf_1.to_sql(name='corona', con=db, if_exists='append', index=False)
    print(df_conf_1)
    print(datetime.now())
    print("데이터갱신")
db_tables = db.execute('SHOW TABLES;')
db_tables = db_tables.fetchall()
table = ('corona',)

if table in db_tables:
    print('리스트 있음')
    new_data()
    db_tables = db.execute('DELETE FROM corona WHERE id IN (select tmp2.id from(SELECT MAX(id) as id FROM corona GROUP BY gubun, stdDay HAVING COUNT(*) > 1) as tmp2);')
    print("갱신 완료")
else:
    print('리스트 없음')
    api_to_mysql()
    print("갱신 완료")