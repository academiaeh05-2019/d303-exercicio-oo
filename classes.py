from random import randint


class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class Conta:
    def __init__(self, cliente):
        self.titular = cliente
        self.numero = self._gerar()
        self._saldo = 0

    def extrato(self):
        print(f'Numero: {self.numero}\nSaldo: {self._saldo}')

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        if(self._saldo < valor):
            return False
        else:
            self._saldo -= valor
            return True

    def consultar_saldo(self):
        return self._saldo

    def _gerar(self):
        self.random_num = f'{randint(1000, 9999)}-{randint(1, 9)}'
        return self.random_num


