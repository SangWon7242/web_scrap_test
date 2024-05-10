# DB 생성
DROP DATABASE IF EXISTS `web_scraping`;
CREATE DATABASE `web_scraping`;

# DB 선택
USE `web_scraping`;


# 날씨 테이블 생성
create table weather_scrap_data (
	id int unsigned not null auto_increment primary key,
	regDate datetime not null,
	comprehensive_weather char(255) NOT NULL,
	today_weather CHAR(255) NOT NULL,
	tomarrow_weather CHAR(255) NOT NULL,
	the_day_after_weather CHAR(255) NOT NULL,
	three_days_from_today_weather CHAR(255) NOT NULL
);