from flask import Flask, render_template, request, redirect, Blueprint, url_for, flash, session
from models import db, Fclty, College

fclty = Blueprint('fclty', __name__,)

@fclty.route('/viewfclty')
def show_fclty():
    if 'user_id' not in session:
        flash('Please log in first', 'warning')
        return redirect(url_for('views.login'))
    questions = Fclty.query.all()
    college = College.query.all()
    return render_template('faculty.html', questions=questions, college=college)

@fclty.route('/addfclty', methods=['POST'])
def add_fclty():
    question_text = request.form.get('question_text')
    college = request.form.get('college')
    new_question = Fclty(faculty=question_text, college=college)
    db.session.add(new_question)
    db.session.commit()
    return redirect(url_for('fclty.show_fclty'))

@fclty.route('/deletefclty', methods=['POST'])
def delete_fclty():
    question_id = request.form.get('selected_question_id')
    question = Fclty.query.get(question_id)
    db.session.delete(question)
    db.session.commit()
    return redirect(url_for('fclty.show_fclty'))

