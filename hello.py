from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return render_template('student.html')

@app.route('/hello/<name>')
def hello_name(name):
    return render_template('home.html', user=name)

@app.route('/result',methods = ['POST'])
def result():
    #result_dict = {'math':60,'chemistry':49,'physics':55}
    result_dict = request.form
    return render_template('result.html', result = result_dict)

@app.route('/blog/<int:id>')
def show_blog(id):
    return 'show blog with id %d' % id

@app.route('/perc/<float:perc>')
def show_prec(perc):
    return 'Percentage is %f' % perc

@app.route('/success/<name>')
def success(name):
    return 'Welcome %s!' % name

@app.route('/login', methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success',name = user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success',name = user))

if __name__ == '__main__':
    app.run(debug = True)