from flask import Flask #Importa o módulo Flask

app = Flask(__name__) #app inicia nossa aplicação

from routes import *

if __name__ == '__main__':
    app.run(debug=True)
