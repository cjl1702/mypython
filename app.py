from flask import Flask
#from flask-mongoengine import mongoengine


#如果是__name__是被包含文件，__main__是主执行文件
app = Flask(__name__)
#app.config['MONGODB_STRING'] = {'db':'python'}
#db = MongoEngine(app)


@app.route('/oneday')
def oneday():
    return 'oneday'



if __name__ == '__main__':
    app.run()





