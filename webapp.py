from flask import Flask
from flask import render_template
from logic import write_json,read_json,get_latest_status
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def home():
    return  render_template('index.html')

@app.route('/index')
def index():
    return  render_template('index.html')


@app.route('/aplicacao')
def main_app():
    estado = get_latest_status()
    context = estado
    button_name = estado.get("button_name")
    button_class = estado.get("button_class")
    button_url = "/aplicacao"
    write_info = estado.get("write_info")
    print(write_info)
    if write_info is None:
        pass
    else:
        write_json(write_info)
    return  render_template('aplicacao.html', button_class = button_class, button_name = button_name, button_url =button_url)

@app.route('/historico')
def history():
    context = read_json()
    return  render_template('historico.html', context = context)

@app.route('/paginateste')
def teste():
    return  render_template('paginateste.html')


