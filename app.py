from flask import Flask, render_template, request,redirect,url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'Bem-vindo à Lista de Compras!'


lista_de_compras = []


@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar_compra():
    if request.method == 'POST':
        item = request.form.get('item')
        if item:
            lista_de_compras.append(item)
        return redirect(url_for('listar_compras'))
    return '''
        <h1>Adicionar Item</h1>
        <form method="post">
            <label for="item">Item:</label>
            <input type="text" name="item" id="item" required>
            <button type="submit">Adicionar</button>
        </form>
        <a href="/">Voltar</a>
    '''


@app.route('/listar')
def listar_compras():
    html = '<h1>Lista de Compras</h1><ul>'
    for item in lista_de_compras:
        html += f'<li>{item}</li>'
    html += '</ul><a href="/adicionar">Adicionar novo item</a>'
    return html


if __name__ == '__main__':
    app.run(debug=True)
