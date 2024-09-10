#Ane Ludmila Monteiro Machado

# Trabalhando com try, except e finally
'''
try: 
    nota_1 = float(input('Digite a 1° nota:'))
    nota_2 = float(input('Digite a 2° nota:'))
    nota_3 = float(input('Digite a 3° nota:'))
    nota_4 = float(input('Digite a 4° nota:'))
    print()
    print(f'A soma das quatros notas são: {nota_1+nota_2+nota_3+nota_4}')
    print()
    print(f'A média das quatros notas são: {(nota_1+nota_2+nota_3+nota_4)/4}')
except ValueError:
    print('Digite apenas números: ')
finally:
    print('Bloco finalizado')
'''
# Trabalhando com try, except e finally
'''
try: 
    nota_1 = float(input('Digite a 1° nota:'))
    nota_2 = float(input('Digite a 2° nota:'))
    nota_3 = float(input('Digite a 3° nota:'))
    nota_4 = float(input('Digite a 4° nota:'))
    print()
    media = (nota_1+nota_2+nota_3+nota_4)/4
    print()

    print(f'A soma das quatro notas são: {nota_1+nota_2+nota_3+nota_4}')

    if media >= 60:
        print(f'Aprovado com média: {media}')
    elif media < 60 and media >= 40:
        print(f'Exame - média: {media}')
    elif media < 40 and media > 30:
        print(f'Só o conselho para ajudar - média: {media}')
    else:
        print(f'Retido na disciplina - média: {media}')

except ValueError:
    print('Digite apenas números: ')
finally:
    pass
'''
#Faça um script, onde o usuário digite seu nome completo em uma string e usando o for, imprima cada letra do nome.
'''
nome = ""
try:
    nome = input('Digite seu nome: ')

    if nome.isalpha and len(str(nome))>=1:
        for letra in nome:
            print(f'A letra do nome digitado foi/; {letra}')
except ValueError:
    print('Digite apenas números: ')
finally:
    pass
'''
# Faça um script, onde o usuário digite o nome completo da disciplina que estamos estudando e usando o comando for que imprima os índices e valores que forem ímpares.

try:
    disciplina = input('Digite o nome da disciplina: ')

    if not disciplina.isalpha():
        print('Digite apenas caractere')
    
    else:
        for indice, letra in enumerate(disciplina):
            if (indice % 2) !=0:
                print(f'{indice}: {letra}')

except Exception as e:
    print(f'Uma exceção ocorreu: {e}')

finally:
    pass
