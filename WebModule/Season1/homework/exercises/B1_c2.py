from flask import Flask, render_template
app = Flask(__name__)


@app.route('/bmi/<int:w>/<int:h>')
def index(w,h):
    BMI = w/((h*h)/10000)
    return render_template('index.html', BMI = BMI)

if __name__ == '__main__':
  app.run( debug=True)
 