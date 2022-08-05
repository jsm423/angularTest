from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
	valueList = ['list1','list2','list3']
	return render_template("index.html", values = valueList)

if __name__ == '__main__':
    app.run(debug=True)