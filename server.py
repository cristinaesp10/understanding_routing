from flask import Flask
# from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<string:name>')
def hi_name(name):
    return f"Hi {name.capitalize()}!"

@app.route('/repeat/<int:num>/<string:whatever>')
def repeat(num, whatever):
    return f"Hello {num * whatever}"

# @app.errorhandler(404)
# def not_found(e):
#     return render_template('404.html'), 404

if __name__ =="__main__":
    app.run(debug=True)