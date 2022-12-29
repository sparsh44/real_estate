from flask import Flask, request, jsonify
import util
from flask_cors import CORS,cross_origin

app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/get_location_names' ,methods = ['GET'])
def get_location_names():
    response = jsonify({
        'locations' : util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_home_price', methods = ['GET', 'POST'])
@cross_origin()
def predict_home_price():
    print(request.json)

    total_sqft = float(request.json['total_sqft'])
    location = request.json['location']
    bath = int(request.json['bath'])
    bhk = int(request.json['bhk'])
    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bath, bhk)
    })
    print(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
    
    

if __name__ == '__main__':
    print('Server started!!..............')
    app.run(debug=True)