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
   books_list = book.get_all_library()
   return render_template('loginafter.html', book=books_list)

@app.route('/rootLogin')
def rootLogin():
    return render_template('rootLogin.html')

@app.route('/lologin', methods=['GET'])
def lologin():
    return render_template('root.html')

@app.route('/roLogin',methods=['POST'])
def roLogin():
    root_name = request.form.get('Rootname')
    rootpass = request.form.get('Rootpass')

    if db.rootlogin(root_name,rootpass):
        return redirect(url_for('lologin'))
    else :
        error='ユーザ名またはパスワードが違います。'
        return render_template('rootLogin.html', error=error)
    

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
    return redirect(url_for('insertcl')) 
                    
                    
@app.route('/insertClear')
def insertcl():
    books_list = book.get_all_library()
    msg="本の登録が完了しました"
    return render_template('insertClear.html',msg=msg,book=books_list)   
    

@app.route('/list')
def books_list():
    books_list = book.get_all_library()
    return render_template('books_list.html', books=books_list)

@app.route('/selectdel')
def books_delete():
    books_list = book.get_all_library()
    return render_template('delete_select.html',book=books_list)

@app.route('/delete_books', methods=['POST'])
def delete():
    isbn = request.form.get('isbn')
    book.delete_book(isbn)
    books_list = book.get_all_library()
    return render_template('delcomplete.html',book=books_list)

@app.route("/search", methods=["GET"])
def search():
    title = request.args.get("title")
    if title == "":
        books_list = book.get_all_library()
        return render_template("loginafter.html", book=books_list)
    books_list = book.search_library(title)
    return render_template("searchList.html",book=books_list)

if __name__ == "__main__":
    app.run(debug=True)