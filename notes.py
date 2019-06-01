from flask import Flask, jsonify

app =  Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route(" / ")
def start():
    return "Welcome to online notes, write your class notes! (/work or /private or /archive)."


@app.route('/work')
def get_work_notes():
    return jsonify( {
        'id': 1,
        'autor': 'Vlad',
        'title': 'Создание онлайн-заметок',
        'text': 'Первая лекция по выполнению работ.',
        'date': '21.05.2019',
        'status': 'Complite'
    },
    {
        'id': 2,
        'autor': 'Alex',
        'title': 'Java script',
        'text': 'Провести лекцию по java script',
        'date': '28.05.2019',
        'status': 'Complite'
    }
    )
    
@app.route('/private')
def get_private_notes():
    return jsonify({
        'id': 1,
        'autor': 'Ivan',
        'title': 'Бизнес-логика',
        'text': 'Провести лекцию по бизнес-логике',
        'date': '30.06.2019',
        'status': 'Active'

    },
    {
        'id': 2,
        'autor': 'Mihail',
        'title': 'Разведка конкуренции между компаниями',
        'text': 'Проверка компаний на работу с клиентами, по поводу постройки бани',
        'date': '12.04.2019',
        'status': 'Complite'
    }
    )
    

@app.route('/archive')
def get_archive_notes():
    return jsonify({
        'id': 1,
        'autor': 'Ilya',
        'title': 'Автомобиль',
        'text': 'Провести техническое обслуживание',
        'date': '13.01.2019',
        'status': 'Archivate'

    },
    {
        'id': 2,
        'autor': 'Nikita',
        'title': 'Сдача курсововой работы',
        'text': 'Начать писать курсовую работу, написать первую главу',
        'date': '23.02.2019',
        'status': 'Archivate'
    }
    )
    
app.run