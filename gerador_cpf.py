import random

nove_digitos = ''

for i in range(9):
    nove_digitos += str(random.randint(0,9))


contagem_regressiva_num1 = 10
contagem_regressiva_num2 = 11
resultados_num1 = 0
resultados_num2 = 0

for j in nove_digitos:

    resultados_num1 += int(j) * contagem_regressiva_num1
    contagem_regressiva_num1 -= 1


decimo_digito = (resultados_num1 * 10) % 11

if decimo_digito <= 9:
    decimo_digito = decimo_digito
else:
    decimo_digito = 0

dez_digitos = nove_digitos + str(decimo_digito)

for num in dez_digitos:

    resultados_num2 += int(num) * contagem_regressiva_num2
    contagem_regressiva_num2 -= 1


ultimo_digito = (resultados_num2 * 10) % 11

if ultimo_digito <= 9:
    ultimo_digito = ultimo_digito
else:
    ultimo_digito = 0

cpf_gerado = dez_digitos + str(ultimo_digito)

print(cpf_gerado)
print(f'{len(cpf_gerado)} digitos')
