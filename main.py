from flask import Flask
from data.users import User
from data.jobs import Jobs
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

def main():
    db_session.global_init('db/mars_explorer.sqlite')
    session = db_session.create_session()
    user = User()
    user.surname = 'Scott'
    user.name = 'Ridley'
    user.age = 21
    user.position = 'captain'
    user.speciality = 'research engineer'
    user.address = 'module_1'
    user.email = 'scott_chief@mars.org'
    session.add(user)

    user = User()
    user.surname = 'Mo'
    user.name = 'Mamba'
    user.age = 18
    user.position = 'second captain'
    user.speciality = 'warrior'
    user.address = 'module_2'
    user.email = 'Mo_Mamba@mars.org'
    session.add(user)

    user = User()
    user.surname = 'Dick'
    user.name = 'Big'
    user.age = 69
    user.position = 'first pilot'
    user.speciality = 'main chef'
    user.address = 'module_228'
    user.email = 'cook_your_eggs@mars.org'
    session.add(user)
    session.commit()
    app.run()

if __name__ == '__main__':
    main()