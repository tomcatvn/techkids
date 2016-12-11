from flask import Flask,redirect,render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/school')
def school():
    return redirect('http://techkids.vn')

@app.route('/homework')
def homework():
    return render_template('homework.html')

@app.route('/bmi/<int:cannang>/<float:chieucao>')
def bmi(cannang,chieucao):
    bmi = cannang / chieucao / chieucao
    bmi = round(bmi,2)
    if bmi < 16:
        return 'còi xương hả mày ' +str(bmi)
    elif 16 <= bmi < 18.5:
        return 'thiếu cân hả mày ' +str(bmi)
    elif 18.5 <= bmi < 25:
        return 'bình thường nha mày ' +str(bmi)
    elif 25 <= bmi < 30:
        return 'hơi mập đó mày ' +str(bmi)
    else :
        return 'BÉO VẬY MÀY ' +str(bmi)


if __name__ == '__main__':
    app.run()
