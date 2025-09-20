from main import app
from flask import render_template #usado para renderizar as templates de HTML

@app.route('/') 
def home(): 
    return render_template('formulario.html')

@app.route('/contato')
def contato():
    return 'Miguel, telefone 11 18929821'