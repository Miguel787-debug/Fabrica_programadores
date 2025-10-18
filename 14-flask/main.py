from flask import Flask #Importa o módulo Flask
from routes import cliente
app = Flask(__name__) #app inicia nossa aplicação

app.register_blueprint(cliente)

if __name__ == '__main__':
    app.run(debug=True)
