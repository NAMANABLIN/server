from flask import Flask, url_for, render_template
from data import db_session
from data.Jobs import Job
from data.Users import User

app = Flask(__name__)

pages = ['/', '/index',
         '/training', '/list_prof', '/answer',
         '/auto_answer', '/login', '/table']

profs = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач',
         'инженер по терраформированию', 'климатолог', 'специалист по радиационной защите', 'астрогеолог',
         'гляциолог', 'инженер жизнеобеспечения', 'метеоролог', 'оператор марсохода',
         'киберинженер', 'штурман', 'пилот дронов']

dict = {
    'title': 'Анкета',
    'surname': 'Wathny',
    'name': 'Mark',
    'education': 'выше среднего',
    'profession': 'штурман марсохода',
    'sex': 'male',
    'motivation': 'Всегда мечтал застрять на Марсе!',
    'ready': 'True'
}

@app.route(pages[0])
def works_log():
    db_session.global_init('mars_explorer.db')
    db_sess = db_session.create_session()
    jobs = db_sess.query(Job).all()
    users = db_sess.query(User).all()
    return render_template('jobs.html', title='Журнал работ', jobs=jobs, users=users)

@app.route(pages[0] + '/<title>')
@app.route(pages[1] + '/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route(pages[2] + '/<prof>')
def show_map(prof):
    return render_template('index.html', prof=prof)


@app.route(pages[3] + '/<list>')
def show_profs(list):
    return render_template('list_prof.html', list=list, profs=profs)


@app.route(pages[4])
@app.route(pages[5])
def answer():
    return render_template('auto_answer.html', dict=dict)

@app.route(pages[6])
def login():
    return render_template('def.html', title='Аварийный доступ')

@app.route(pages[7] + '/<sex>' + '/<age>')
def table(sex, age):
    return render_template('table.html')

if __name__ == '__main__':
    for x in pages:
        print('http://127.0.0.1:8080' + x)
    app.run(port=8080, host='127.0.0.1')
