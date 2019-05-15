from flask import Flask, render_template, url_for, request, redirect
from search import word_search
from functions import load_recommend, ver

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('home.html')


@app.route('/user/<username>', methods=['POST', 'GET'])
def user(username):
    movies = load_recommend(username)
    return render_template('user.html', username=username, movies=movies)


@app.route('/result/<search>/<selection>', methods=['POST', 'GET'])
def result(search, selection):
    if selection == 'Story':
        selection = 'keyWords'
    result = word_search(search, selection.lower())
    return render_template('result.html', search=search, result=result)


@app.route('/user/login')
def login():
    return render_template('login.html')


@app.route('/user/redirect', methods=['POST'])
def redirect_to_new_url():
    username = request.form['username']
    password = request.form['password']
    print(username)
    print(password)
    if ver(username, password):
        return redirect(url_for('user', username=username))
    else:
        return 'wrong'


@app.route('/home/redirect', methods=['POST'])
def search_result():
    search = request.form['search']
    selection = request.values.get('opt')
    print('sel', selection)
    print(search)
    return redirect(url_for('result', search=search, selection=selection))


if __name__ == '__main__':
    app.run(debug=True)
