from faker import Faker
import random
import xlsxwriter
import shutil
Notas = []
ND = ['13 988241058',
      '13 988298845', 
      '13 981334385', 
      '13 988826964', 
      '13 988676061', 
      '13 982270867', 
      '11 951468966', 
      '13 991090654']
Ano = 1
PE = ['Fundamental 1', "Médio"]
Período = 1
ac = 0
linhas = int(input())
fake = Faker()
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
workbook.close()
shutil.move(r"C:\Users\Nicolas\Documents\Nicolas LINDÃO\Cursos\Informática\Projetos Impressionadores\matematica.xlsx", r"C:\Users\Nicolas\Documents\Nicolas LINDÃO\Cursos\Informática\Projetos Impressionadores\Analisador de planilha")