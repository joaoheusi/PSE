from flask import Flask
from flask import render_template
from logic import write_json,read_json,get_latest_status
from datetime import datetime
from flask import request
app = Flask(__name__)


@app.route('/')
def home():
    return  render_template('index.html')

@app.route('/index')
def index():
    return  render_template('index.html')


@app.route('/aplicacao', methods=['GET','POST'])
def main_app():
    if request.method == 'POST':
        estado = get_latest_status()
        write_info = estado.get("write_info") 
        write_json(write_info)
        estado = get_latest_status()
        context = estado
        button_name = estado.get("button_name")
        button_class = estado.get("button_class")
        button_url = "main_app"

        return render_template('aplicacao.html', button_class = button_class, button_name = button_name, button_url =button_url)
     
    if request.method == 'GET':
        estado = get_latest_status()
        context = estado
        button_name = estado.get("button_name")
        button_class = estado.get("button_class")
        button_url = "main_app"

        return render_template('aplicacao.html', button_class = button_class, button_name = button_name, button_url =button_url)

@app.route('/historico')
def history():
    context = read_json()
    return  render_template('historico.html', context = context)

@app.route('/paginateste')
def teste():
    return  render_template('paginateste.html')


