from faker import Faker
import random
import xlsxwriter
import shutil

#Variáveis básicas
Notas = []
ND = ['lista de números que podem ser utilizados']
Ano = 1
PE = ['Fundamental 1', "Médio"]
Período = 1
ac = 0
linhas = int(input())
fake = Faker()

#Aqui faz a criação do arquivo, podendo ser "qualquer coisa.xlsx"
workbook = xlsxwriter.Workbook('matematica.xlsx')
planilha = workbook.add_worksheet('notas')


for i in range(linhas):
    
    planilha.write(i, 0, fake.name())
    planilha.write(i, 1, ND[random.randint(0, len(ND)-1)])
    Notas.append([])
    Ano = random.randint(1,9)
    planilha.write(i, 2, Ano)
    if(Ano>5): Período ="Fundamental 2"
    elif(Ano > 3): Período = "Fundamental 1"
    else: Período = PE[random.randint(0,1)]
    planilha.write(i, 3, Período)
    for j in range(4):
        Notas[i].append(random.randint(0,10))
        ac += Notas[i][j]
        planilha.write(i, 4+j, Notas[i][j])
    planilha.write(i, 8, ac/4)
    if(ac/4<5): planilha.write(i, 9, 'REPROVADO')
    else: planilha.write(i, 9, 'APROVADO')
    ac = 0

#fecha o arquivo em excel e move o arquivo para a pasta atual
workbook.close()
shutil.move(r"C:\caminho\matematica.xlsx", r"C:\caminho\Analisador de planilha")