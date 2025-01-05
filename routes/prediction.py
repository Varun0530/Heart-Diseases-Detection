"""Prediction route handlers."""

from flask import Blueprint, request, jsonify
from model.predictor import predict_heart_disease

prediction_bp = Blueprint('prediction', __name__)

@prediction_bp.route('/predict', methods=['POST'])
def predict():
    """Handle prediction requests."""
    try:
        features = request.json
        is_heart_disease, probability = predict_heart_disease(features)
        
        return jsonify({
            'prediction': 'Heart Disease Detected' if is_heart_disease else 'No Heart Disease Detected',
            'probability': round(probability * 100, 2)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400