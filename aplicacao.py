# Construção da API --> Flask
from flask import Flask, request
from datetime import datetime
import joblib
import sqlite3

# Instanciar o app
app = Flask(__name__)

#Carregar nosso modelo
Modelo = joblib.load('Modelo_Floresta_v100.pk1')


#Função para receber nossa API
@app.route('/api_preditivo/<area>;<rooms>;<bathroom>;<parking_spaces>;<floor>;<animal>;<furniture>;<hoa>;<property_tax>', methods = ['GET'])
def funcao_01(area, rooms, bathroom, parking_spaces, floor, animal, furniture, hoa, property_tax):
    
    # Data e Hora de Inicio
    Data_Inicio = datetime.now()
    
    # Recebendo os inputs da API
    Lista = [
        float(area), float(rooms), float(bathroom), float(parking_spaces), float(floor), float(animal), float(furniture), float(hoa), float(property_tax)
    ]
    
    #Tentar a previsão
    try:
        # Predict
        Previsao = Modelo.predict([Lista])
        
        # Inserir o valor da Previsão
        Lista.append(str(Previsao))
        
        # Transformando Lista em String
        Input = ''
        for Valor in Lista:
            Input = Input + ';' + str(Valor)
        
        # Capturando data e hora
        Data_Fim = datetime.now()
        Processamento = Data_Fim - Data_Inicio
        
        # Conexão com o banco de dados
        Conexao_Banco = sqlite3.connect('banco_api.db')
        Cursor = Conexao_Banco.cursor()
        
        # Query
        Query_Inserindo_Dados = f'''
        INSERT INTO Log_API (Inputs, Inicio, Fim, Processamento) 
        VALUES ( '{Input}', '{Data_Inicio}', '{Data_Fim}', '{Processamento}')
        '''
        # Executar a query
        Cursor.execute(Query_Inserindo_Dados)
        Conexao_Banco.commit()
        Cursor.close()
        
        return {"Valor_Aluguel" : str(Previsao)}
    
    except:
        return {"Aviso" : "Deu algum erro!"}
    

if __name__ == '__main__':
    app.run(debug=True)
    
    
