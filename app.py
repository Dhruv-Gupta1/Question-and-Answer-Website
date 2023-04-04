from flask import Flask, render_template,url_for,request,jsonify
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

db = yaml.load(open('db.yaml'),Loader=yaml.FullLoader)
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

@app.route('/')
def base():
    return render_template('base.html')

@app.route('/<string:username>')
def base_loggedin(username):
    return render_template('base_loggedin.html',username=username)

@app.route('/login', methods=['GET'])
def login():
    if request.method == 'GET':
        username = request.args.get('username')
        password = request.args.get('password')
        cur = mysql.connection.cursor()
        sql = "SELECT * FROM users WHERE UserName = %s AND UserPass = %s"
        val = (username, password)
        cur.execute(sql, val)
        result = cur.fetchone()
        mysql.connection.commit()
        cur.close()
        if result!=None:
            return render_template('base_loggedin.html',username=username)
        else:
            return render_template('login.html')
    else:
        return render_template('login.html')
    

@app.route('/tags2/<string:username>',methods=['GET'])
def tags2(username):
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        sort = request.args.get('sort')
        if sort==None:
            sort="TagId"
        cur.execute("SELECT * FROM tags ORDER BY "+sort)
        tags = cur.fetchall()
        return render_template('tags_loggedin.html', tags=tags,username=username)
    return render_template('tags_loggedin.html',username=username)


@app.route('/tags',methods=['GET'])
def tags():
    if request.method == 'GET':
        cur = mysql.connection.cursor()

        sort = request.args.get('sort')
        if sort==None:
            sort="TagId"
            
        cur.execute("SELECT * FROM tags ORDER BY "+sort)
        tags = cur.fetchall()
        return render_template('tags.html', tags=tags)
    return render_template('tags.html')



@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(UserName,UserEmail,UserPass) VALUES (%s, %s, %s)", (username,email,password))
        mysql.connection.commit()
        cur.close()
        #return render_template('logged_in_base.html',username=username)
        return render_template('base.html')
    return render_template('signup.html')

@app.route('/questions',methods=['GET'])
def questions():
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM questions")
        questions = cur.fetchall()
        
        return render_template('questions.html', questions=questions)
    return render_template('questions.html')

@app.route('/questions2/<string:username>',methods=['GET'])
def questions2(username):
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM questions")
        questions = cur.fetchall()
        return render_template('questions_loggedin.html', questions=questions,username=username)
    return render_template('questions_loggedin.html',username=username)

@app.route('/users',methods=['GET'])
def users():
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users")
        users = cur.fetchall()
        return render_template('users.html', users=users)
    return render_template('users.html')

# @app.route('/',methods=['GET'])
# def get_data(id):
#     if request.method == "GET":
#         cur = mysql.connection.cursor()
#         cur.execute("SELECT UserName FROM users WHERE UserId = %s", (id,))
#         user_details = cur.fetchall()
#         cur.close()
#         return jsonify(user_details)
#     return "YES"


if __name__ == "__main__":
    app.run(debug=True,port=8034)