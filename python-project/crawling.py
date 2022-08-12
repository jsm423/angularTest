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


url = 'https://movie.naver.com/#none'
headers = {'Content-Type': 'application/json; charset=utf-8'}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

result = soup.select('a._select_title_anchor strong')

@app.route('/crawling')
def movie():    
    cursor = db.cursor(MySQLdb.cursors.DictCursor)

    for mName in result:
        sql = f"insert into movie(movieName) values ('{mName.get_text()}')"
        cursor.execute(sql)
        
    db.commit()
    data_list = cursor.fetchall()
    return jsonify(data_list)


if __name__ == "__main__":
    app.run('127.0.0.1', port = 5010, debug=True)    