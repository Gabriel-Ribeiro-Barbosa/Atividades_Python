class Clientes():
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.lista_plano = ['basic','premium']
        if plano in self.lista_plano:
            self.plano = plano
        else:
            raise Exception('Plano Inválido')


    def Mudar_Plano(self,novo_plano):
        if novo_plano in self.lista_plano:
            self.plano = novo_plano
        else:
            print('Plano Inválido')


    def Ver_Filme(self, filme, plano_filme):
        if self.plano == plano_filme:
            print(f'Ver fileme {filme}')
        elif self.plano == 'premium':
            print(f'Ver fileme {filme}')
        elif self.plano ==  'basic' and plano_filme == 'premium':
            print('\033[1;31mAssine o plano premium para ver esse filme')
        else:
            print('Plano Inválido')



cliente = Clientes('gabriel', 'gribeirobarbosa386@gmail.com', 'basic')
print(cliente.plano)
cliente.Mudar_Plano('basicooo')
print(cliente.plano)
cliente.Ver_Filme('Mulan','basic')