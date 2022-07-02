from flask import flash, redirect, url_for, render_template

from msg_board import app, db
from msg_board.forms import MsgForm
from msg_board.models import Message


@app.route('/msg', methods=['GET', 'POST'])
def index():
    form = MsgForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(body=body, name=name)
        db.session.add(message)
        db.session.commit()
        flash('成功添加留言~')
        return redirect(url_for('index'))

    messages = Message.query.order_by(Message.timestamp.desc()).all()
    return render_template('index.html', form=form, messages=messages)
