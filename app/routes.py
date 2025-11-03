from flask import render_template, request, url_for, flash, redirect
from app import app
import re
from datetime import datetime

WEEKDAYS = [
    'Понедельник', 'Вторник', 'Среда', 'Четверг',
    'Пятница', 'Суббота', 'Воскресенье'
]

MONTHS_NOMINATIVE = [
    'Январь', 'Февраль', 'Март', 'Апрель', 'Май',
    'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь',
    'Ноябрь', 'Декабрь'
]


@app.route('/')
def home():
    current_time = datetime.now()
    weekday = WEEKDAYS[current_time.weekday()]
    month = MONTHS_NOMINATIVE[current_time.month - 1]
    formatted_time = f'{weekday}, {month} {current_time.day:02d}, {current_time.year}, {current_time.strftime("%H:%M:%S")}'
    return render_template('index.html', current_time=formatted_time)


@app.route('/about')
def about():
    team_members = [
        {'name': 'Алиса', 'role': 'Разработчик'},
        {'name': 'Боб', 'role': 'Дизайнер'},
        {'name': 'Чарли', 'role': 'Менеджер проекта'}
    ]
    return render_template('about.html', team_members=team_members)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        if not name or not email or not message:
            flash('Пожалуйста, заполните все поля!', 'error')
            return redirect(url_for('contact'))

        if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            flash('Некорректный формат email!', 'error')
            return redirect(url_for('contact'))

        flash('Ваше сообщение успешно отправлено!', 'success')
        return redirect(url_for('contact'))

    contact_info = {
        'manager': {
            'name': 'Анна Иванова',
            'position': 'Менеджер по работе с клиентами',
            'email': 'support@flaskpraktikum.ru'
        },
        'address': {
            'street': 'ул. Разработчиков, д. 42',
            'city': 'Москва',
            'postal_code': '101000'
        }
    }
    return render_template('contact.html', contact_info=contact_info)
