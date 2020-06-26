from flask import Flask, jsonify

app = Flask(__name__)


devList = [
    {'nome': 'Dev Severino', 
    'habilidade' : ['Python','Java']
    },
    {'nome': 'Dev Isac', 
    'habilidade' : ['C','Cpp']
    }
]

@app.route('/<int:id>/')
def desenvolvedor(id):
    dev = devList[id]
    return jsonify(dev)

if __name__ == '__main__':
    app.run(debug=True)