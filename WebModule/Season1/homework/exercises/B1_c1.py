from flask import Flask
app = Flask(__name__)


@app.route('/bmi/<int:weight>/<int:height>')
def index(weight,height):
    height = float(height)/100
    BMI = float(weight) / float(height*height)
    if BMI < 16 :
        return('Thieu can nghiem trong.')
    elif BMI <= 18.5 :
        return('Thieu can.')
    elif BMI <= 25 :
        return('Binh thuong.')
    elif BMI <= 30 :
        return('Thua can.')
    else :
        return('Beo phi.')

if __name__ == '__main__':
  app.run(debug=True)
