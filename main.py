from flask import Flask, render_template, request, redirect, url_for
import config
import json
import requests
import ast

app = Flask(__name__, template_folder='templates')

#app.register_blueprint(controller, url_prefix='/controller/')

@app.route('/')
def index():
    return render_template('login/index.html')

@app.route('/github', methods=['GET','POST'])
def github():
    git_user = request.form['username']
    url = f'https://api.github.com/users/{git_user}'
    repos_url = f'https://api.github.com/users/{git_user}/repos'
    following_url = f'https://api.github.com/users/{git_user}/following'
    followers_url = f'https://api.github.com/users/{git_user}/followers'
    r_git = requests.get(url=url)
    r_repos = requests.get(url=repos_url)
    r_repos = r_repos.text.replace(':false', ':False').replace(':true', ':True').replace(':null',':None')
    repos = ast.literal_eval(r_repos)
    git = json.loads(r_git.text)

    try:
        git_exist = not (git['message'] == 'Not Found')
    except:
        git_exist = True
    if request.method == 'POST' and git_exist:
        return render_template('github.html', github=git, repos=repos)
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True,port=config.PORT)