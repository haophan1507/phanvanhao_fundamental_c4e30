from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    Users = [
	{
		    'name' : 'Nguyen Quang Huy',
			'age' : 29
    },
    {
			'name' : 'Huynh Tuan Anh',
			'age' : 22
    }
    ]
    return render_template('index1.html',data = Users)

if __name__ == '__main__':
  app.run(debug=True)
 