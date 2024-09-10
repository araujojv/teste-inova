import phonenumbers
import re

def validar_telefone(telefone, codigo_pais="55"):
    try:
       
        telefone_limpo = re.sub(r"[^\d]", "", telefone)
        
        
        if telefone_limpo.startswith(codigo_pais):
            numero_telefone = phonenumbers.parse(f"+{telefone_limpo}", None)
        else:
           
            numero_telefone = phonenumbers.parse(f"+{codigo_pais}{telefone_limpo}", None)
        
       
        valido = phonenumbers.is_valid_number(numero_telefone)
        
        
        if valido:
            return phonenumbers.format_number(numero_telefone, phonenumbers.PhoneNumberFormat.E164)
        else:
            return None
        
    except phonenumbers.phonenumberutil.NumberParseException:
        return None
