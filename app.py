from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Bem-vindo à Lista de Compras!'

if __name__ == '__main__':
    app.run(debug=True)
