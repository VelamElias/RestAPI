from flask import Flask, jsonify, request
import json

app = Flask(__name__)


devList = [
    {'nome': 'Dev Severino', 
    'habilidade' : ['Python','Java']
    },
    {'nome': 'Dev Isac', 
    'habilidade' : ['C','Cpp']
    }
]

@app.route('/<int:id>/', methods=['GET', 'PUT'])
def desenvolvedor(id):
    if request.method == 'GET':
        dev = devList[id]
        return jsonify(dev)
        
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        dev[id] = dados
        return jsonify(dados)

if __name__ == '__main__':
    app.run(debug=True)