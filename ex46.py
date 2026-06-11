import re

def validar_cpf_mensagem(cpf: str) -> str:
    # Remove quaisquer caracteres que não sejam números
    cpf_limpo = re.sub(r'\D', '', cpf)
    
    # O CPF deve ter exatamente 11 dígitos
    if len(cpf_limpo) != 11:
        return f"CPF '{cpf}' inválido: Deve conter exatamente 11 números."
    
    # Rejeita CPFs com todos os dígitos iguais (ex: 111.111.111-11)
    if cpf_limpo == cpf_limpo[0] * 11:
        return f"CPF '{cpf}' inválido: Sequências repetidas não são permitidas."
    
    # ---- Validação do 1º Dígito Verificador ----
    soma = 0
    for i in range(9):
        soma += int(cpf_limpo[i]) * (10 - i)
    
    resto = soma % 11
    digito_1 = 0 if resto < 2 else 11 - resto
    
    if int(cpf_limpo[9]) != digito_1:
        return f"CPF '{cpf}' inválido."
    
    # ---- Validação do 2º Dígito Verificador ----
    soma = 0
    for i in range(10):
        soma += int(cpf_limpo[i]) * (11 - i)
        
    resto = soma % 11
    digito_2 = 0 if resto < 2 else 11 - resto
    
    if int(cpf_limpo[10]) != digito_2:
        return f"CPF '{cpf}' inválido."
        
    # Se passou por todas as validações
    return f"CPF '{cpf}' válido."
num = input("Digite o cpf =>")
x = validar_cpf_mensagem(num)
print(x)