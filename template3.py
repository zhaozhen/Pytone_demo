from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    name=[12,21,23,23,23,2,3]
    return render_template('users.html',name=name)

#启动
if __name__=="__main__":
    app.run(port=8000,debug=True)