from flask import Flask, render_template, redirect, request
from crear_db import CargarDatos

productos = CargarDatos()

# App
app = Flask(__name__)

# Ruta
@app.route('/')
def index():
    categoria = request.args.get('categoria')
    if categoria:
        productos_filtrados = [producto for producto in productos if producto.get('categoria') == categoria]
        return render_template('index.html', productos=productos_filtrados, categoria=categoria)
    else:
        return render_template('index.html', productos=productos, categoria=None)

@app.route('/producto/<int:pid>')
def producto(pid):
    for producto in productos:
        if pid == producto['id']:
            return render_template('producto.html', producto=producto)
    return redirect('/')

# Programa principal
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
