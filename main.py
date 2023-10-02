print("="*40)
print('PROVA G2 POR EDUARDO JESUS')
print("="*40)
print('')

def readturmas():
    alunosp = {}
    turmasd = {}
    turmasp = {}
  
    with open('Turmas.txt', 'r') as arquivo:
        next(arquivo)

        for linha in arquivo:
            
            professor, disciplina, dia, turno, alunos = linha.strip().split(',')

            alunos = int(alunos)

            if professor in alunosp:
                alunosp[professor] += alunos
            else:
                alunosp[professor] = alunos

            if dia in turmasd:
                turmasd[dia] += 1
            else:
                turmasd[dia] = 1

            if professor in turmasp:
                turmasp[professor] += 1
            else:
                turmasp[professor] = 1

    return alunosp, turmasd, turmasp


def ordenar_professores(turmasp, reverse=False):

    lista_turmas_professores = list(turmasp.items())

    lista_turmas_professores.sort(key=lambda x: x[1], reverse=reverse)

    return lista_turmas_professores


def exibir_saidas(alunosp, turmasd, turmasp):
    print("="*40)
    print("= Quantos alunos cada professor tem? =")
    print("="*40)
    print('')
    print(alunosp)
    print('')
  
    print("="*40)
    print("= Quantas turmas em cada dia da semana? =")
    print("="*40)

    print('')
    print(turmasd)
    print('')
    print("="*40)
    print("= Quantas turmas cada professor tem? =")
    print("="*40)

    print('')
    print(turmasp)
    print('')
    print("="*50)
  
    print("= Professores e turmas em ordem decrescente =")
    print("="*50)
    print('')
    for professor, turmas in ordenar_professores(turmasp, reverse=True):
        print(professor, turmas)
    print('')
      
    print("="*50)
    print("= Professores e turmas em ordem crescente =")
    print("="*50)
    print('')
    for professor, turmas in ordenar_professores(turmasp):
        print(professor, turmas)

def programa():
    alunosp, turmasd, turmasp = readturmas()
    exibir_saidas(alunosp, turmasd, turmasp)


programa()
