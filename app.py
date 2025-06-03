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
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

lista_de_compras = []

@app.route('/')
def index():
    return '<h1>Bem-vindo à Lista de Compras</h1><a href="/listar">Ver Lista</a> | <a href="/adicionar">Adicionar Item</a>'

@app.route('/listar')
def listar_compras():
    html = '<h1>Lista de Compras</h1><ul>'
    for i, item in enumerate(lista_de_compras):
        html += f'<li>{item} <a href="/editar/{i}">Editar</a></li>'
    html += '</ul><a href="/adicionar">Adicionar novo item</a>'
    return html

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
            <input type="text" name="item" required>
            <button type="submit">Adicionar</button>
        </form>
        <a href="/">Voltar</a>
    '''

@app.route('/editar/<int:index>', methods=['GET', 'POST'])
def editar_compra(index):
    if index < 0 or index >= len(lista_de_compras):
        return 'Item não encontrado', 404

    if request.method == 'POST':
        novo_valor = request.form.get('item')
        if novo_valor:
            lista_de_compras[index] = novo_valor
        return redirect(url_for('listar_compras'))

    item_atual = lista_de_compras[index]
    return f'''
        <h1>Editar Item</h1>
        <form method="post">
            <input type="text" name="item" value="{item_atual}" required>
            <button type="submit">Salvar</button>
        </form>
        <a href="/listar">Voltar</a>
    '''


if __name__ == '__main__':
    app.run(debug=True)
