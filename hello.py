from flask import Flask
from flask import request
from flask import make_response
from flask import  redirect
from flask import abort
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

# 没有激活上下文不能调用current_app
# @app.route("/")
# def index():
#     user_agent=request.headers.get("User-Agent")
#     req=request
#     return '<p>you browser is %s</p>'%user_agent

#设置返回的参数！创建一个cookie
# @app.route("/")
# def index():
#     response=make_response('<p>This document carries a cookie! </p>')
#     response.set_cookie("answer",'42')
#     return response

# #重定向，
# @app.route('/')
# def index():
#     return redirect("http://www.baidu.com")

#还有一种特殊的相应有abort函数生成，用于处理错误，abort不会把控制权交给调用它额函数，而是把异常抛出给web服务器
@app.route("/user/<id>")
def get_user(id):
    user=id
    if not user:
        abort(404)
    return '<h1>Hello ,%s<h1>'%user

@app.route("/user/<name>")
def user(name):
    return '<h1> Hello %s!</h1>'%name

if __name__=="__main__":
    app.run(port=8000,debug=True)
    # app.run(debug=True)