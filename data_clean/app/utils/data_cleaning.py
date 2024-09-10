import re
from datetime import datetime

from app.utils.number_helper import apenas_numeros, extenso_para_numero
from app.utils.phone_helper import validar_telefone


def corrigir_idade_service(idade):
    if idade is None:
        return 0

    if isinstance(idade, str):
        try:
            idade = int(apenas_numeros(idade))
        except ValueError:
            idade = extenso_para_numero(idade)

    if isinstance(idade, (int, float)):
        idade = abs(int(idade))

        return idade
    return 0


def corrigir_data_service(data):
    if data is None or data.strip() == "":
        return None

    data_limpa = re.sub(r"[^\d\-]", "", data)

    if len(data_limpa) < 8:
        return None

    formatos_possiveis = ["%Y-%m-%d", "%d-%m-%Y", "%Y/%m/%d", "%d/%m/%Y"]

    for formato in formatos_possiveis:
        try:

            return datetime.strptime(data_limpa, formato).strftime("%Y-%m-%d")
        except ValueError:
            continue

    return None


def corrigir_ativo_service(ativo):
    return True if str(ativo).lower() in ["yes", "sim", "true", "y", "1"] else False


def corrigir_salario_service(salario):
    if salario is None:
        return 0

    if isinstance(salario, str):
        salario_str = salario.strip().replace(",", ".")

        try:
            salario = float(salario_str)
        except ValueError:

            try:
                salario = extenso_para_numero(salario_str)
            except ValueError:
                return None

    if isinstance(salario, (int, float)):
        salario = abs(float(salario))
        return salario if salario > 0 else 0
    return None


def corrigir_telefone_service(telefone):
    if telefone is None:
        return None
    return validar_telefone(apenas_numeros(telefone))


def limpar_dados_service(dados):
    # ultimo_id = 0
    for usuario in dados["usuarios"]:
        # usuario['id'] = corrigir_id_service(usuario['id'], ultimo_id)
        # decidi tirar o ID porque ele não tem influencia no meu serviço, logo, posso apenas usar o id criado pelo banco, mas pensei em botar o id tanto do json tanto o do banco, mas nao achei necessario
        # nao acho correto tratar o id, ja que ele representa em outro lugar algum valor
        # ultimo_id = usuario['id']
        usuario["idade"] = corrigir_idade_service(usuario["idade"])
        ## usuario['email'] = corrigir_email_service(usuario['email'])
        usuario["telefone"] = corrigir_telefone_service(usuario["telefone"])
        usuario["ativo"] = corrigir_ativo_service(usuario["ativo"])
        usuario["salario"] = corrigir_salario_service(usuario["salario"])
        usuario["data_cadastro"] = corrigir_data_service(usuario["data_cadastro"])
        usuario.pop("id", None)
    return dados
