
import requests
import xmltodict
import pandas as pd
from sqlalchemy import create_engine

### mysql 연결
MYSQL_HOSTNAME = 'database-1.chj8bifpnqxd.ap-northeast-2.rds.amazonaws.com'  # mysql ip
MYSQL_USER = 'admin'  # user
MYSQL_PASSWORD = 'qwer1234' # pw
MYSQL_DATABASE = 'gmb_db'   # db name

connection_string = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}/{MYSQL_DATABASE}'
db = create_engine(connection_string) # db 연결

url = "http://openapi.seoul.go.kr:8088/4b4878424b646c6331394362647463/xml/TbCorona19CountStatusJCG/1/5/" # xml
rows=['JONGNOADD', 'JUNGGUADD', 'YONGSANADD', 'GWANGJINADD', 'DDMADD', 'JUNGNANGADD', 'SEONGBUKADD', 'GANGBUKADD', 'DOBONGADD', 'NOWONADD','EPADD','SDMADD','MAPOADD','YANGCHEONADD','GANGSEOADD','GUROADD','GEUMCHEONADD','YDPADD','DONGJAKADD','GWANAKADD','SEOCHOADD','GANGNAMADD','SONGPAADD','GANGDONGADD', 'ETCADD']
columns = ['JONGNO', 'JUNGGU', 'YONGSAN', 'GWANGJIN', 'DDM', 'JUNGNANG', 'SEONGBUK', 'GANGBUK', 'DOBONG', 'NOWON','EP','SDM','MAPO','YANGCHEON','GANGSEO','GURO','GEUMCHEON','YDP','DONGJAK','GWANAK','SEOCHO','GANGNAM','SONGPA','GANGDONG', 'ETC']

req = requests.get(url).content
xmlObject = xmltodict.parse(req)
dict_data = xmlObject['TbCorona19CountStatusJCG']['row']
df_conf = pd.DataFrame(dict_data) # dict to pd.DataFrame
df_conf = pd.melt(df_conf,
                  id_vars=['JCG_DT'],
                  value_vars=rows,
                  value_name='con',
                  ignore_index=False) # melt를 활용한 재구조화

df_conf_1 = df_conf.astype(
    {'JCG_DT': 'datetime64', "con": "int"})
df_conf_1.to_sql(name='corona_con', con=db, if_exists = 'replace', index= False)
db.execute('ALTER TABLE corona_con ADD COLUMN id INT(9) NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST;')
print(df_conf_1)
print("corona_con 갱신완료")