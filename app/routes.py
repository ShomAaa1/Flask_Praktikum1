from flask import render_template, request, url_for, flash, redirect
from app import app
import re


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


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

    return render_template('contact.html')


    return render_template('contact.html')
