# Matheus Carvalho

def ler_nome():
    """Retorna uma string com o nome do aluno."""
    return input("Informe o nome do aluno: ")

def ler_notas():

    try:
        ap1 = float(input("Informe a nota da AP1: "))
        ap2 = float(input("Informe a nota da AP2: "))
        asub = float(input("Informe a nota da AS: "))
        ac = float(input("Informe a nota da AC: "))
        return ap1, ap2, asub, ac
    except ValueError:
        print("Por favor, informe notas válidas.")
        return ler_notas()

def notas_sao_validas(ap1, ap2, asub, ac):

    if 0 <= ap1 <= 10 and 0 <= ap2 <= 10 and 0 <= asub <= 10 and 0 <= ac <= 10:
        return True
    else:
        return False

def selecionar_notas(ap1, ap2, asub):

    if asub >= ap1 and asub >= ap2:
        return asub, max(ap1, ap2)
    else:
        return ap1, ap2

def aluno_foi_aprovado(media):

    return media >= 7

def analisar_media(media):

    print("Média:", media)
    if aluno_foi_aprovado(media):
        print("Aluno foi aprovado.")
    else:
        print("Aluno foi reprovado.")

def main():
    nome = ler_nome()
    if nome:
        ap1, ap2, asub, ac = ler_notas()
        if notas_sao_validas(ap1, ap2, asub, ac):
            nota1, nota2 = selecionar_notas(ap1, ap2, asub)
            media = calcular_media(nota1, nota2, ac)
            analisar_media(media)

if __name__ == "__main__":
    main()

