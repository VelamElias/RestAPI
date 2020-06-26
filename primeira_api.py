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

@app.route('/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = devList[id]
        except IndexError:
            response = {'status' : 'erro', 'mensagem' : 'Dev com ID #''{} não existe'}
        except Exception:
            mensagem = 'Undefined error. Report to developer'
            response = {'status': 'erro', 'mensagem': mensagem}
        return jsonify(response)


    elif request.method == 'PUT':
        dados = json.loads(request.data)
        dev[id] = dados
        return jsonify(dados)
    
    elif request.method == 'DELETE':
        dev.pop(id)
        return jsonify({'status' : 'sucess', 'mensagem' : 'Registro deletado'})

if __name__ == '__main__':
    app.run(debug=True)