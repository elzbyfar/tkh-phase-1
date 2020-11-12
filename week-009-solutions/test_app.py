

from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = b'\af234v\qvr4q4\234tg2v42\av4q43rvvq4\vq4qv4gq4v\avrq4\vaq424'

@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)