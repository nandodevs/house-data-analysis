# Construção da API --> Flask
from flask import Flask, request
import joblib

# Instanciar o app
app = Flask(__name__)

#Carregar nosso modelo
Modelo = joblib.load('Modelo_Floresta_v100.pk1')

#Função para receber nossa API
@app.route('/api_preditivo/<area>;<rooms>;<bathroom>;<parking_spaces>;<floor>;<animal>;<furniture>;<hoa>;<property_tax>', methods = ['GET'])
def funcao_01(area, rooms, bathroom, parking_spaces, floor, animal, furniture, hoa, property_tax):
    
    # Recebendo os inputs da API
    Lista = [
        float(area), float(rooms), float(bathroom), float(parking_spaces), float(floor), float(animal), float(furniture), float(hoa), float(property_tax)
    ]
    
    #Tentar a previsão
    try:
        Previsao = Modelo.predict([Lista])
        return {"Valor_Aluguel" : str(Previsao)}
    
    except:
        return {"Aviso" : "Deu algum erro!"}
    

if __name__ == '__main__':
    app.run(debug=True)
    
    
