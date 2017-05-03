from flask import Flask, render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap

app = Flask(__name__)

manager = Manager(app)
bootstrap = Bootstrap(app)


# 頁面沒有找到
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# @app.route('/')
# def index():
#     return render_template('index.html')
#
#
# @app.route('/user/<name>')
# def user(name):
#     return render_template('bootstrap.html', name=name)
#
#
# if __name__ == '__main__':
#     manager.run()
#
#
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('bootstrap.html', name=name)


if __name__ == '__main__':
    manager.run()