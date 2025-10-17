from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <form action="/BMI" method="post">
            <label>Enter your weight:</label>
            <input type="float" name="weight">
            <label>Enter your height:</label>
            <input type="float" name="height">
            <input type="submit" value="Submit">
        </form>
    '''

@app.route('/BMI', methods=['POST'])
def bmi():
    weight = float(request.form['weight'])
    height = float(request.form['height'])
    return f"Your BMI is: {weight/height**2} "



if __name__ == '__main__':
    app.run(debug=True)
