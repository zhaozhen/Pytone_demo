from flask import Flask
from flask import request
app=Flask(__name__)

# @app.route("/")
# def index():
#     return '<h1>Hello World 123</h1>'

#flask应用程序的上下文
# curren_app:当前激活程序的实力
# g：处理请求是用作临时变量对象，每次请求都会冲设这个值
#请求上下文
# request：请求对象，封装了http的请求内容
#seesion：用户会话，用于存储请求之间的需要记住的值的字典
@app.route("/")
def index():
    user_agent=request.headers.get("User-Agent")
    req=request
    return '<p>you browser is %s</p>'%user_agent

@app.route("/user/<name>")
def user(name):
    return '<h1> Hello %s!</h1>'%name

if __name__=="__main__":
    app.run(port=8000,debug=True)
    # app.run(debug=True)