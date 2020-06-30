#!/usr/bin/python
from flask import Flask
from flask_restx import Api, Resource, fields
from sklearn.externals import joblib
from m10 import valores
from sklearn.ensemble import RandomForestRegressor


app = Flask(__name__)

api = Api(
    app, 
    version='1.0', 
    title='Modelo de estimación del precio de los autos API',
    description='Prediction del Precio  API')

ns = api.namespace('predict', 
     description='Prediccion del precio de los autos')
   
parser = api.parser()

parser.add_argument(
    'Year', 
    type=str, 
    required=True, 
    help='URL to be analyzed', 
    location='args')

parser.add_argument(
    'Mileage', 
    type=str, 
    required=True, 
    help='URL to be analyzed', 
    location='args')

parser.add_argument(
    'State', 
    type=str, 
    required=True, 
    help='URL to be analyzed', 
    location='args')

parser.add_argument(
    'Make', 
    type=str, 
    required=True, 
    help='URL to be analyzed', 
    location='args')

parser.add_argument(
    'Model', 
    type=str, 
    required=True, 
    help='URL to be analyzed', 
    location='args')


resource_fields = api.model('Resource', {
    'result': fields.String,
})

@ns.route('/')
class PhishingApi(Resource):

    @api.doc(parser=parser)
    @api.marshal_with(resource_fields)
    def get(self):
        args = parser.parse_args()
        
       
        return {
         "result": valores(args['Year'], args['Mileage'], args['State'], args['Make'], args['Model'])}, 200
    
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=5000)
 