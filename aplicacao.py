# Construção da API --> Flask
from flask import Flask, request

# Instanciar o app
app = Flask(__name__)

@app.route('/api_preditivo')
def funcao_01():
    return {'Retorno' : 'Deu certo'}

if __name__ == '__main__':
    app.run(debug=True)
    
    
