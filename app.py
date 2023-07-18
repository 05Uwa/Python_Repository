from flask import Flask, render_template , request
import db

app= Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def login():
    error = 'ログインに失敗しました。'
    return render_template('index.html',error=error)

@app.route('/register')
def register_fomr():
    return render_template('register.html')

@app.route('/register_exe' , methods=['POST'])
def register_exe():
    user_name = request.form.get('username')
    password = request.form.get('password')
    
    count = db.insert_user(user_name , password)
    if count==1:
        msg='登録が完了しました。'
        return render_template('index.html',msg=msg)
    else:
        error='登録に失敗しました。'
        return render_template('register.html',error=error)
    
if __name__ == "__main__":
    app.run(debug=True)