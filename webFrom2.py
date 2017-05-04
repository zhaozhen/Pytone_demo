from flask import Flask, render_template,flash
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from flask import  session,redirect,url_for

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SECRET_KEY']='asdfadfasdfsahsdklfjaldfgashdjfgasydk'

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    # name = StringField('What is your name?')
    submit = SubmitField('Submit')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


# @app.route('/', methods=['GET', 'POST'])
# def index():
#     name = None
#     form = NameForm()
#     if form.validate_on_submit():
#         name = form.name.data
#         form.name.data = ''
#     return render_template('webIndex.html', form=form, name=name)
# //方法不能正确运行。。。。
@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('webIndex2.html', form=form, name=session.get('name'))


# @app.route('/',methods=['GET','POST'])
# def index():
#     form = NameForm()
#     if form.validate_on_submit():
#         old_name=session.get('name')
#         if old_name is not None and old_name!=form.name.data:
#             flash("Looks like you have changed you name!")
#         session['name']=form.name.data
#         return redirect(url_for('index'))
#     return render_template('webIndex2.html', form=form, name=session.get('name'))
#

if __name__ == '__main__':
    manager.run()
