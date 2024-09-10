import requests
from flask import Blueprint, request, jsonify
from .utils.data_cleaning import limpar_dados_service

cleaner_bp = Blueprint('cleaner', __name__)

@cleaner_bp.route('/clean', methods=['POST'])
def clean():
    """
    Rota para limpar os dados enviados.
    Recebe os dados via POST, limpa os dados e envia para outra API.
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    
    cleaned_data = limpar_dados_service(data)
    print(cleaned_data)
    
    external_api_url = "http://172.18.0.4:5002/database/user-create-many" 

    try:
       
        response = requests.post(external_api_url, json=cleaned_data)

       
        if response.status_code == 201:
            return jsonify({
                "message": "Dados limpos e enviados com sucesso para a API externa",
                "cleaned_data": cleaned_data,
                "external_api_response": response.json()
            }), 200
        else:
            return jsonify({
                "error": "Falha ao enviar dados para a API externa",
                "cleaned_data": cleaned_data,
                "external_api_response": response.text
            }), response.status_code

    except requests.exceptions.RequestException as e:
        return jsonify({
            "error": "Erro ao se comunicar com a API externa",
            "details": str(e),
            "cleaned_data": cleaned_data
        }), 500
@cleaner_bp.route('/health', methods=['GET'])
def health():
    
    return jsonify(), 200