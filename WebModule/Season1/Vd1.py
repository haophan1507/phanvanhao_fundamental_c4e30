from flask import Flask, render_template
app = Flask(__name__)


# @app.route('/add/<a>/<b>')
# def index(a,b):
#     return str(int(a)+int(b))

@app.route('/')
def index():
    poem_data = [{
      'title' : 'tĩnh dạ tứ',
      'body' : 'nội dung',
      'author' : 'lý bạch'
    },
    {
      'title' : 'đông chí',
      'body' : 'nội dung',
      'author' : 'tố hữu'
    }]
    return render_template('index.html', data = poem_data)
if __name__ == '__main__':
  app.run(host = '127.0.0.1', port=8000, debug=True)
 
 