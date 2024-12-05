from flask import Flask, render_template, request, redirect, Blueprint, url_for, flash, session
from models import db, Prgrms, College

prgrms = Blueprint('prgrm', __name__,)

@prgrms.route('/viewpgrm')
def show_pgrm():
    if 'user_id' not in session:
        flash('Please log in first', 'warning')
        return redirect(url_for('views.login'))
    questions = Prgrms.query.all()
    colleges = College.query.all()
    return render_template('program.html', questions=questions, colleges=colleges)

@prgrms.route('/addpgrm', methods=['POST'])
def add_pgrm():
    question_text = request.form.get('question_text')
    college = request.form.get('college')
    new_question = Prgrms(program=question_text, college=college)
    db.session.add(new_question)
    db.session.commit()
    return redirect(url_for('prgrm.show_pgrm'))

@prgrms.route('/deletepgrm', methods=['POST'])
def delete_pgrm():
    question_id = request.form.get('selected_question_id')
    question = Prgrms.query.get(question_id)
    db.session.delete(question)
    db.session.commit()
    return redirect(url_for('prgrm.show_pgrm'))

