import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl 

# 웹페이지 URL 설정
url = 'https://www.weather.go.kr/w/weather/forecast/short-term.do'

# GET 요청 보내기
resp = requests.get(url).text
bs = BeautifulSoup(resp, 'html.parser')

summary_data = bs.select('.cmp-view-content > .summary > span')
comp_data = summary_data[0].get_text() # 종합
today_summary = summary_data[1].get_text() # 오늘 
tom_summary = summary_data[2].get_text() # 내일
the_day_after_tom = summary_data[3].get_text() # 모레
three_days_today = summary_data[4].get_text() # 글피 : 현재 일자의 3일 뒤 날씨

print(f"comp_data : {comp_data}") # 종합
print(f"today_summary : {today_summary}") # 오늘
print(f"tom_summary : {tom_summary}") # 내일
print(f"the_day_after_tom : {the_day_after_tom}") # 모레
print(f"three_days_today : {three_days_today}") # 글피 : 현재 일자의 3일 뒤 날씨

# 데이터프레임 생성
data = {
    "종합": [comp_data],
    "오늘": [today_summary],
    "내일": [tom_summary],
    "모레": [the_day_after_tom],
    "3일 후 날씨": [three_days_today]
}

df = pd.DataFrame(data)

# 엑셀 파일로 저장
excel_file = "weather_data.xlsx"
df.to_excel(f"C:\work\python_projects\{excel_file}", index=False)

print(f"데이터가 '{excel_file}' 파일로 저장되었습니다.")