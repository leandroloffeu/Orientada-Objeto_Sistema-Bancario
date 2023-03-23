class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
    def exibir(self):
        print(f'O nome do cliente é: {self.nome} sobrenome: {self.sobrenome} CPF: {self.cpf}')


      