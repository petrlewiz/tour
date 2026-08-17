import os
from flask import Flask, render_template, request
from flask_babel import Babel
from dotenv import load_dotenv

load_dotenv()

def get_locale():
    return request.accept_languages.best_match(['en', 'es'])

app = Flask(__name__)
app.config['SECRET_KEY']=os.environ.get('SECRET_KEY')
babel = Babel(app, locale_selector=get_locale)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()