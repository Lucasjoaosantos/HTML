import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/curriculo')
def curriculo():
    return render_template('curriculo.html')

@app.route('/lista')
def lista():
    df = pd.read_csv('C:/Users/joaol/Desktop/Nova pasta/curriclos/templates/tabela.csv')

    livros = df.to_dict(orient='records')

    return render_template('lista.html', livros=livros)

if __name__ == '__main__':
    app.run()


