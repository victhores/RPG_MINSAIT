# int
idade = 21
ano_de_nascimento = 2001
dia_da_contratacao = 4

# float
saldo_bancario = 0.21
pi = 3.141521
constante_de_Euler = 1.6

#string (str)
nome_completo = "Víctor Eduardo da Silva"
marca_do_computador = "HP"
versao_do_codigo = "v0.0.1"
# print(f'Nome do colaborador: {nome_completo}')

# lista (list)
# tarefas diárias
tarefas_diarias = ['Arrumar a cama', 'Escovar os dentes']
tarefas_diarias.append('Tomar Café da manhã')
tarefas_diarias.extend(['Estudar programação', 'Jogar Bola'])
# print(tarefas_diarias)
tarefas_diarias.pop(4)
# print(tarefas_diarias)
tarefas_diarias.insert(2, "Mexer no mouse")
# print(tarefas_diarias)

# treinamento jovens profissionais
pessoas_no_treinamento_jovens_profissionais = ['Lucas', 'Lygia', 'Nívea', 'Madson']
funcionarios = ['Klismann', 'Rodolpho']
pessoas_no_treinamento_jovens_profissionais.extend(funcionarios)
# print(pessoas_no_treinamento_jovens_profissionais)
funcionario_performance_excepcional = funcionarios.index('Klismann')
# print(funcionario_performance_excepcional)

# mega sena
numeros_da_sorte_da_mega_sena = [60, 12, 43, 58, 4, 60, 60, 60]
quantas_vezes_o_60_se_repetiu = numeros_da_sorte_da_mega_sena.count(60)
# print(quantas_vezes_o_60_se_repetiu)
print(sorted(numeros_da_sorte_da_mega_sena))
print(numeros_da_sorte_da_mega_sena.reverse())

# lista x set
equipamentos = {232, 123, 456, 234, 112}
print(equipamentos)

# set_de_equipamentos = set(equipamentos)
# print(set_de_equipamentos)

equipamentos.update([123, 475, 987, 342])
# print(equipamentos)

equipamentos.pop()
# print(equipamentos)

equipamentos.clear()
# print(equipamentos)


parentes_diretos = {
    "pais" : ["Pai", "Mãe"],
    "irmão" : ["Keverton"]
}

modelo_tipo_de_cabo = {
    "Moto E7": ["Cabo3", "Cabo4"],
    "Iphone": ["Cabo1", "Cabo2"]
}


# print(parentes_diretos.get("pais")) # retorna os itens dentro da chave
# print(parentes_diretos.values()) # retorna todos os itens dentro do dicionario

print(parentes_diretos.items())

# funções

def soma_dois_inteiros(primeiro_numero, segundo_numero):
    return primeiro_numero + segundo_numero


# tuplas x listas
tupla_de_informacoes = ('Victor', 21, 'lindao')

tupla_de_informacoes[0] = 'eu'

print(tupla_de_informacoes)