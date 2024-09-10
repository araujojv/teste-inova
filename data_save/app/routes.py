from flask import Blueprint, request, jsonify
from datetime import datetime
from app.models import UserModel,db
cleaner_bp = Blueprint('database', __name__)

@cleaner_bp.route('/user-create-many', methods=['POST'])
def criar_usuario():
    dados = request.get_json()
    for usuario in dados['usuarios']:  
        novo_usuario = UserModel(
        nome=usuario['nome'],
        idade=usuario['idade'],
        email=usuario['email'],
        telefone=usuario['telefone'],
        endereco=usuario['endereco'],
        data_cadastro=usuario['data_cadastro'],
        ativo=usuario.get('ativo', True),
        salario=usuario['salario']
    )
    
        db.session.add(novo_usuario)
        db.session.commit()
    
    return jsonify({"message": "Usuário criado com sucesso!"}), 201


@cleaner_bp.route('/user-all', methods=['GET'])
def listar_usuarios():
    usuarios =  UserModel.query.all()

    usuarios_json = [{"id": u.id, "nome": u.nome, "idade": u.idade, "email": u.email , 'email_verificado': u.email_verificado,
                      'telefone': u.telefone, 'salario': u.salario, 'data_cadastro': u.data_cadastro, 'ativo': u.ativo, 'endereco': u.endereco} for u in usuarios]
    
    return jsonify(usuarios_json), 200

@cleaner_bp.route('/health', methods=['GET'])
def health():
    
    return jsonify(), 200