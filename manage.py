from flask_script import Manager
from app import app
#from models import user

manager = Manager(app)

@manager.command
def hell():
    print('hello world')



if __name__ == '__main__':
    manager.run()






