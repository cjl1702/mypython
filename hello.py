from flask import Flask, url_for,render_template,request,Flask
app = Flask(__name__)

#@app.route('/')
#def hello_world():
    #return 'Hello World'

@app.route('/hello')
def hello():
    return 'hello world2'

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User ' + username
    #return 'User %s' % username

@app.route('/post/<int:user_id>')
def show_post(user_id):
    return 'Post %d' % user_id

@app.route('/projects')
def projects():
    return 'the projects page'

@app.route('/about/')
def about():
    return 'the about page'

#模板渲染
@app.route('/drip/<name>')
def drip(name=None):
    return render_template('drip.html',name=name)


#请求方法
@app.route('/login',methods=['POST','GET'])
def login():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username and password:
            return render_template('login.html',dict = {'name':username,'password':password})
        else:
            return render_template('login.html',error='请输入用户名和密码')
    else:
        return render_template('login.html')



@app.route('/')
def index(): pass





if __name__ == '__main__':
    app.debug = True
    app.run()
    #app.run(debug=True)
    #app.run(host='0.0.0.0')print