from flask import Flask, render_template
import cx_Oracle

dsn = cx_Oracle.makedsn("localhost", 1521, service_name = "XE")
connection = cx_Oracle.connect(user="jo", password="sumin", dsn=dsn, encoding="UTF-8")

cur = connection.cursor()

app = Flask(__name__)

@app.route('/movie')
def movie():
    sql = "select movieName, to_char(releaseDate,'yyyy-mm-dd') as releasedate, rating, director from movie"
    cur.execute(sql)
    data_list = cur.fetchall()

    return render_template('movie.html', data_list = data_list)


if __name__ == '__main__':
    app.run(debug=True)


