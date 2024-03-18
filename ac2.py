import math

def eq_seg_grau(a, b, c):
    delta = b**2 - 4*a*c
    
    
    if delta < 0:
        return None
    
    
    elif delta == 0:
        raiz = -b / (2*a)
        return raiz
    
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2*a)
        raiz2 = (-b - math.sqrt(delta)) / (2*a)
        return raiz1, raiz2

def bissexto(ano):
    
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False

# Testando as funções
print(eq_seg_grau(1, -3, 2))  # Saída esperada: (2.0, 1.0)
print(eq_seg_grau(1, 2, 1))    # Saída esperada: -1.0
print(eq_seg_grau(1, 1, 1))    # Saída esperada: None (sem raízes reais)

print(bissexto(2020))  # Saída esperada: True
print(bissexto(1900))  # Saída esperada: False
print(bissexto(2000))  # Saída esperada: True

#2
def calcular_salario(salario_por_hora, horas_trabalhadas):
    salario_total = salario_por_hora * horas_trabalhadas
    return salario_total

salario_por_hora = float(input("Digite o salário por hora: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

salario_final = calcular_salario(salario_por_hora, horas_trabalhadas)
print("O salário a ser recebido é:", salario_final)

