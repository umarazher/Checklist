from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    print(request.method)
    if request.method == 'POST':
        email = request.form.get("email")
        passwd = request.form.get("password")
        print(email)
        print(passwd)
        return render_template("validation.html")
    return render_template('login.html')



@app.route('/home',methods =['GET'])
def home():
    return render_template('index.html')

@app.route('/widgets', methods=['GET'])
def widgets():
    return render_template('widgets.html')

@app.route('/validation', methods=['GET'])
def validation():
    return render_template('validation.html')

@app.route('/calendar', methods=['GET'])
def calendar():
    return render_template('pages/apps/calendar.html')

@app.route('/email', methods=['GET'])
def email():
    return render_template('pages/apps/email.html')

@app.route('/todo', methods=['GET'])
def todo():
    return render_template('pages/apps/todo.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('pages/samples/error-404.html')

@app.route('/profile', methods = ['GET'])
def profile():
    return render_template('profile.html')

@app.route('/feeds', methods = ['GET'])
def feeds():
    return render_template('pages/samples/timeline.html')

@app.route('/', methods = ['GET'])
def search():
    return render_template('pages/samples/blank-page.html')




if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')