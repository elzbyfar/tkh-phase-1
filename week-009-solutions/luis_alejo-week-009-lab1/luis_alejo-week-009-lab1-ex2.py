from flask import Flask, render_template, request

app = Flask(__name__)

app.config['SECRET_KEY'] = b'\xf6U\xb5\xfb\x0c\x17\xca\xd0\xb7|\xe6S\xe0\xa7\xfb\xce \xcd\xd9\xc7#K\xb0Y'

@app.route('/sqrt/<num>')
def sqrt(num):
    sqrt = pow(int(num), .5)
    return render_template('sqrt.html', sqrt=sqrt)

@app.route('/user/<username>')
def welcome(username):
    return render_template('user.html', username=username)
    
@app.route('/req_url')
def req_url():
    req_url = request.url
    return render_template('req_url.html', req_url=req_url)
    
if __name__ == '__main__':
    app.run(debug=True)