from flask import Flask, request, jsonify
import json
import random

app = Flask(__name__)

@app.route('/GET/<int:Factor>',methods=['GET'])
def getPrice(Factor):
    Price = random.randint(0, Factor+1)
    Face = random.randint(Factor, 2*Factor)
    dict = {}
    dict['Price'] = Price
    dict['Face'] = Face
    return json.dumps(dict)

@app.route('/POST',methods=['POST'])
def getResult():
    j_data = request.json
    app.logger.info(j_data)
    price = j_data['Price']
    face = j_data['Face']
    dict={}
    dict['Price'] = price
    dict['Face'] = face
    dict['Result'] = price*face
    return json.dumps(dict)

if __name__ == '__main__':
    app.run(debug=True)
