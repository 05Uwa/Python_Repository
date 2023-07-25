from flask import Flask, render_template , request, redirect, url_for
import db
import book

app= Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/register')
def register_form():
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

@app.route('/',methods=['POST'])
def login():
    user_name = request.form.get('username')
    password = request.form.get('password')

    if db.login(user_name, password):
        return redirect(url_for('loginafter'))
    else :
        error='ユーザ名またはパスワードが違います。'
        return render_template('index.html', error=error)
    
@app.route('/login', methods=['GET'])
def loginafter():
    # book_list = book.get_all_library()
    return render_template('loginafter.html')

@app.route('/rootLogin')
def rootLogin():
    return render_template('rootLogin.html')

@app.route('/ro',methods=['POST'])
def roLogin():
    root_name = request.form.get('rootrname')
    rootpass = request.form.get('rootpass')

    if db.login(root_name,rootpass):
        return redirect(url_for('loginaf'))
    else :
        error='ユーザ名またはパスワードが違います。'
        return render_template('index.html', error=error)
    
@app.route('/root')
def root():
    return render_template('root.html')
    
@app.route('/login', methods=['GET'])
def loginaf():
    return render_template('root.html')

@app.route('/insertroot')
def insertRoot():
    return render_template('insertRoot.html')

@app.route('/insert',methods=['GET'])
def insert():
    title = request.args.get('title')
    author = request.args.get('author')
    publisher = request.args.get('publisher')
    isbn = request.args.get('isbn')
    
    count=book.insert_library(title,author,publisher,isbn)
    if count==1:
        msg ='図書の登録が完了しました。'
        return render_template('insertclear.html',msg=msg)
    else :
        error ='図書の登録に失敗しました。'
        return render_template('insertRoot.html',error=error)
    
    
@app.route('/serach')
def searchList():
    keyword = request.args.get('keyword')
    titles = book.select_library(keyword)
    return render_template('searchList.html',titles=titles)
if __name__ == "__main__":
    app.run(debug=True)