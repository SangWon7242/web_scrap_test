import mysql.connector

# MySQL 연결 설정
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="sbsst",
    password="sbs123414",
    database="web_scraping"
)

# 커서 생성
cursor = conn.cursor()

# 테이블 생성 (이 부분은 필요에 따라 생략할 수 있습니다)
create_table_query = """
CREATE TABLE IF NOT EXISTS scraped_data (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    regDate DATETIME NOT NULL,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL
)
"""

cursor.execute(create_table_query)
conn.commit()