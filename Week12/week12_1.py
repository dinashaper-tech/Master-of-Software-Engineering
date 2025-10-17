from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <form action="/greet" method="post">
            <label>Enter your name:</label>
            <input type="text" name="username">
            <input type="submit" value="Your Name">
        </form>
    '''

@app.route('/bye')
def bye():
    return "Bye Flask!"

@app.route('/username/<name>')
def learn(name):
    return f"{name} is learning Flask"

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form['username']
    return f"{name} is good at Flask"

@app.route('/cal/<int:number>')
def show_square(number):
    return f"The square of {number} is {number**2}"

if __name__ == '__main__':
    app.run(debug=True)
