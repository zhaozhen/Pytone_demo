from flask import Flask
app=Flask(__name__)

@app.route("/")
def index():
    return '<h1>Hello World 123</h1>'

if __name__=="__main__":
    app.run(port=8000,debug=True)
    # app.run(debug=True)