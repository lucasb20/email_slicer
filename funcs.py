import re

def verifica_nome(nome):
    padrao = r'^[a-zA-Z0-9]+$'
    correspondencia = re.match(padrao, nome)
    if correspondencia:
        return True
    else:
        return False

def verifica_dominio(texto):
    padrao = r'^[A-Za-z]+[.][A-Za-z]+$'
    correspondencia = re.match(padrao, texto)
    if correspondencia:
        return True
    else:
        return False

def valid_email(email):
    parts = email.split('@')
    if len(parts) != 2:
        return False
    
    if not(verifica_nome(parts[0])) or not(verifica_dominio(parts[1])):
        return False

    else:
        return parts
