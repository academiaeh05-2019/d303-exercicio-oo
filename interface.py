from classes import Cliente, Conta


class CaixaEletronico():
  def __init__(self):
    nome = input('Digite seu nome: ')
    cpf = input('Digite seu CPF: ')

    cliente = Cliente(nome, cpf)
    self._conta = Conta(cliente)

    print(f'Olá, {self._conta.titular.nome}, sua conta é {self._conta.numero}')

  def exibir_menu(self):
    print(f'1- Consultar saldo\n2- Depositar\n3- Sacar')
    escolha = input('Escolha uma opção: ')

    if escolha == '1':
      self.exibir_saldo()
    elif escolha == '2':
      self.depositar()
    elif escolha == '3':
      self.sacar()
    else:
      print('Opção inválida.')

  def exibir_saldo(self):
    valor = str(self._conta.consultar_saldo())
    print(f'Seu saldo é R$ {valor}.')

  def depositar(self):
    valor = float(input('Digite o valor: '))
    self._conta.depositar(valor)
    print('Depósito efetuado.')
    self.exibir_saldo()

  def sacar(self):
    valor = float(input('Digite o valor: '))
    
    if self._conta.sacar(valor):
      print('Saque efetuado.')
      self.exibir_saldo()
    else:
      print('Saldo insuficiente.')