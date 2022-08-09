from flask import Flask, render_template, request
import cx_Oracle

dsn = cx_Oracle.makedsn("localhost", 1521, service_name = "XE")
connection = cx_Oracle.connect(user="jo", password="sumin", dsn=dsn, encoding="UTF-8")

app = Flask(__name__)

@app.route('/movie')
def movie():    
    cursor = connection.cursor()
    sql = "select movieName, to_char(releaseDate,'yyyy-mm-dd') as releasedate, rating, director from movie"
    cursor.execute(sql)
    data_list = cursor.fetchall()
    return render_template('movie.html', data_list = data_list)

@app.route('/search', methods = ['GET','POST'])
def search():
    search = request.args.get("searchType")
    keyword = request.args.get("keyword")    
    cursor = connection.cursor()
    sql = f"select movieName, to_char(releaseDate,'yyyy-mm-dd') as releasedate, rating, director from movie where {search} like '%'||'{keyword}'||'%' "
    cursor.execute(sql)
    search_list = cursor.fetchall()
    return render_template('search.html', search_list = search_list)

@app.route('/sort', methods = ['GET','POST'])
def sort():
    sort = request.args.get("sort")
    cursor = connection.cursor()
    sql = f"select movieName, to_char(releaseDate,'yyyy-mm-dd') as releasedate, rating, director from movie order by rating {sort}"
    cursor.execute(sql)
    sort_list = cursor.fetchall()
    return render_template('sort.html', sort_list = sort_list)


if __name__ == '__main__':
    app.run(debug=True)


