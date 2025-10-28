#Validador de CPF
def validar_cpf(cpf):
    # Remover caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verificando se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False
    
    # Verificando se todos os dígitos são iguais
    if cpf == cpf[0] * 11:
        return False
    
    # Calculaddo primero dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = soma % 11
    if resto < 2:
        digito_verificador1 = 0
    else:
        digito_verificador1 = 11 - resto

    # Verificando o primeiro dígito verificador
    if int(cpf[9]) != digito_verificador1:
        return False
    
    # Calculando o segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = soma % 11
    if resto < 2:
        digito_verificador2 = 0
    else:
        digito_verificador2 = 11 - resto

    # Verificando o segundo dígito verificador
    if int(cpf[10]) != digito_verificador2:
        return False
    
    # CPF válido
    return True

# Exemplo de uso
cpf = input('Digite o CPF para validação: ')

if validar_cpf(cpf):
    print(f'O CPF [{cpf}] é váido.')
else:
    print(f'O CPF [{cpf}] é inválido.')