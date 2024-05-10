import requests
from bs4 import BeautifulSoup
import mysql.connector

# 웹페이지 URL 설정
url = 'https://www.weather.go.kr/w/weather/forecast/short-term.do'

# GET 요청 보내기
resp = requests.get(url).text
bs = BeautifulSoup(resp, 'html.parser')

# MySQL 연결 설정
conn = mysql.connector.connect(
  host="127.0.0.1",
  user="sbsst",
  password="sbs123414",
  database="web_scraping"
)

# 커서 생성
cursor = conn.cursor()

summary_data = bs.select('.cmp-view-content > .summary > span')
comp_data = summary_data[0].get_text() # 종합
today_summary = summary_data[1].get_text() # 오늘 
tom_summary = summary_data[2].get_text() # 내일
the_day_after_tom = summary_data[3].get_text() # 모레
three_days_today = summary_data[4].get_text() # 글피

print(f"comp_data : {comp_data}") # 종합
print(f"today_summary : {today_summary}") # 오늘
print(f"tom_summary : {tom_summary}") # 내일
print(f"the_day_after_tom : {the_day_after_tom}") # 모레
print(f"three_days_today : {three_days_today}") # 글피 : 현재 일자의 3일 뒤 날씨

create_table_query = f"""
INSERT INTO weather_scrap_data
SET regDate = NOW(),
comprehensive_weather = '{comp_data}',
today_weather = '{today_summary}',
tomarrow_weather = '{tom_summary}',
the_day_after_weather = '{the_day_after_tom}',
three_days_from_today_weather = '{three_days_today}'
"""

print(create_table_query)

summary_data_depth4 = bs.select('.cmp-view-content > .summary > span.depth_4')

for depth_4 in summary_data_depth4:
  print(depth_4.get_text())
  
cursor.execute(create_table_query)
conn.commit()