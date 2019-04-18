from flask import Flask, render_template, request
app = Flask(__name__)

Bt = [
        {
            'uses' : 'phanvanhao',
            'pass' : '12345'
        }
    ]

@app.route('/',methods=['POST'])
def Bt():
    user_name = request.form.get('user_name')
    pass_word = request.form.get('pass_word')
    if  user_name == 'phanvanhao' and pass_word == '12345':
        return "Login Successful!"
    else:
        return "Login Failed!"
    
@app.route('/')
def index(): 
    return render_template('index.html')
    
if __name__ == '__main__':
  app.run(debug=True)
 