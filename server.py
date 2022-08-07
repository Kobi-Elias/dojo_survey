from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "Kusrabak arse"

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/user', methods=['POST'])
# def create_user():
#     return redirect('/')

@app.route('/submit_info', methods=['POST'])
def results():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language']= request.form['language']
    session['comment'] = request.form['comment']
    return redirect("/result")

@app.route('/result')
def result():
    return render_template ("result.html")

if __name__ == "__main__":
    app.run(debug=True)