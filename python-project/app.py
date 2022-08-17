import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

import pymysql
import MySQLdb
import MySQLdb.cursors

db = MySQLdb.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='mysql',
    db='python',
    charset='utf8'
)


app = Flask(__name__)
CORS(app)


@app.route('/movie', methods = ['GET'])
def movie():    
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    sql = "select movieName, date_format(releaseDate,'%Y-%m-%d') as releasedate, rating, director from movie"
    cursor.execute(sql)
    data_list = cursor.fetchall()
    return jsonify(data_list)

@app.route('/search', methods = ['GET'])
def search():
    searchType = request.args.get("searchType")
    keyword = request.args.get("keyword")    
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    sql = f"select movieName, date_format(releaseDate,'%Y-%m-%d') as releasedate, rating, director from movie where {searchType} like '%{keyword}%' "
    cursor.execute(sql)
    search_list = cursor.fetchall()
    return jsonify(search_list)

@app.route('/sort', methods = ['GET'])
def sort():
    sort = request.args.get("sort")
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    sql = f"select movieName, date_format(releaseDate,'%Y-%m-%d') as releasedate, rating, director from movie order by rating {sort}"
    cursor.execute(sql)
    sort_list = cursor.fetchall()
    return jsonify(sort_list)


url = 'https://movie.naver.com/movie/running/current.naver?view=list&tab=normal&order=open'
headers = {'Content-Type': 'application/json; charset=utf-8'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

title = soup.select('#content > div.article > div > div.lst_wrap > ul > li > dl > dt > a')
rating = soup.select('#content > div.article > div > div.lst_wrap > ul > li > dl > dd.star > dl > dd > div > a > span.num')
director = soup.select('#content > div.article > div > div.lst_wrap > ul > li > dl > dd:nth-child(3) > dl > dd:nth-child(4) > span > a')
releaseDate = soup.select('#content > div.article > div > div.lst_wrap > ul > li > dl > dd:nth-child(3) > dl > dd:nth-child(2) > span:nth-child(3)')

titles = []
ratings = []
directors = []
dates = []

for t in title:
    titles.append(t.get_text())

for r in rating:
    ratings.append(r.get_text())

for d in director:
    directors.append(d.get_text())

for rd in releaseDate:
    dates.append(rd.next_sibling.strip().split(" ")[0])

datas = [data for data in zip(titles,ratings,directors,dates)]

@app.route('/crawling')
def crawling():    
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    
    for data in datas:
        sql = f"insert into movie(movieName, rating, director, releaseDate) values('{data[0]}','{data[1]}','{data[2]}','{data[3]}')"
        cursor.execute(sql)

    db.commit()
    data_list = cursor.fetchall()
    return jsonify(data_list)

 
if __name__ == "__main__":
    app.run(debug=True)
