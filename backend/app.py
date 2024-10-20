from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from model import TrafficPredictor
import os

app = Flask(__name__)
CORS(app)

predictor = TrafficPredictor()

@app.route('/')
def index():
    return send_from_directory('../frontend', 'index.html')

@app.route('/<path:path>')
def serve_frontend(path):
    return send_from_directory('../frontend', path)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        lat = float(data['lat'])
        lng = float(data['lng'])
        coded_day = int(data['CodedDay'])
        weather = int(data['Weather'])
        is_holiday = int(data['IsHoliday'])
        
        prediction = predictor.predict(coded_day, weather, is_holiday)
        return jsonify({'prediction': prediction, 'lat': lat, 'lng': lng})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)