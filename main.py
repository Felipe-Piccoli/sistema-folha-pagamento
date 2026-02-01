funcionarios = {
    "Ana Silva": 4500.00,
    "Bruno Souza": 7200.00,
    "Carla Dias": 3100.00,
    "Diego Lima": 5500.00,
    "Elena Ferri": 9800.00,
    "Felipe Rocha": 5000.00,
    "Giovanna Melo": 2900.00,
    "Henrique Vaz": 12000.00,
    "Isabela Cruz": 4800.00,
    "João Pedro": 3300.00,
    "Karina Lopes": 6100.00,
    "Leonardo Faz": 5000.00,
    "Marina Sol": 4200.00,
    "Nuno Gomes": 7000.00,
    "Olivia Reis": 3900.00,
    "Paulo Neto": 8500.00,
    "Quiteria Lu": 2700.00,
    "Rafael Ryu": 11000.00,
    "Sofia Mar": 4600.00,
    "Tiago Luz": 5300.00
}

funcionarios_negativo = {}
funcionarios_prontos = {}
funcionarios_outliers = {}

gasto_total = 0
total_funcionarios = 0
media_por_func = 0

def calcular_bonus(salario):
    bonus_curto = 0.05
    bonus_longo = 0.1
    if salario < 5000:
        return salario * bonus_longo + salario
    else:
        return salario * bonus_curto + salario
      
for nome, salario in funcionarios.items():
    if salario <= 0:
        funcionarios_negativo[nome] = salario
    else:
        funcionarios_prontos[nome] = calcular_bonus(salario)

for nome, salario in funcionarios_prontos.items():
    print(f"O salário do {nome} com bônus é de R$: {salario:.2f}")
    gasto_total += salario
    total_funcionarios += 1
    if salario >= 10000:
        funcionarios_outliers[nome] = salario
      
media_por_func = gasto_total / total_funcionarios

for nome, salario in funcionarios_negativo.items():
    print(f"O funcionário {nome} está com o salário negativo de R$: {salario}")

print("Os salários Outliers são:")
for nome, salario in funcionarios_outliers.items():
    print(f"{nome}, R$: {salario:.2f}")

print(f"O gasto total da Microsoft com salários é de R$: {gasto_total:.2f}, com um total de funcionários de {total_funcionarios}, dando uma média de R$: {media_por_func:.2f} por funcionário")
