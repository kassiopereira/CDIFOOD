import datetime

class SysBank:
    
    def __init__(self):
        self.opcoes = {"1": self.opdeposito,
                       "2": self.opsaque,
                       "3": self.opextrato,
                     }
        self.extrato = []
        self.saldo = 0.0
        self.limsaque = 3
        self.vallimit = 500

    def exibir_menu(self):
      print("Bem vindo Ao SysBank!")
      print("1: Para Deposito")
      print("2: Para Saque")
      print("3: Para Extrato")
      print("4: Para Sair")

    def selecionar_menu(self):
        escolha = input("Digite a operação desejada: ")
        if escolha == "4":
            print("Você escolheu a opção Sair, até a próxima!!")
            return False
        elif escolha in self.opcoes:
            self.opcoes[escolha]()
            return True
        else:
            print("Opção inválida.")
            return True
    
    def opdeposito(self):
        print("Você escolheu a opção Deposito.")
        valordep = float(input("Digite o valor do deposito: "))
        if valordep > 0:    
           print(f"Foi depositado o valor de R${valordep:.2f} ")
           self.saldo += valordep
           data = datetime.datetime.now()
           registro = {"data": data, "valor": valordep}
           self.extrato.append(registro) 
           print(f"Seu novo saldo é o valor de R$ {self.saldo:.2f} ")
         
        else:
              print("Valor não aceito.")
        return
    
    def opsaque(self):
        print("Você escolheu a opção Saque.")
        valorsaq= float(input("Digite o valor de saque: "))
        if self.limsaque == 0:    
           print("Limite Diario de Saques Execido.")
           return
        elif valorsaq > self.saldo :
           print(f"Valor solicitado é maior que o saldo atual. Saldo restante é de: R$ {self.saldo:.2f}")
           return
        elif valorsaq > self.vallimit :
           print(f"Valor permitido por saque foi ultrapassado, tente outro valor menor que: R$ {self.vallimit:.2f}.")
           return
        else:
           print(f"Foi sacado o valor de R$ {valorsaq:.2f}")
           self.limsaque -= 1
           self.saldo -= valorsaq
           data = datetime.datetime.now()
           registro = {"data": data, "valor": -valorsaq}
           self.extrato.append(registro)
           print(f"Seu novo saldo é o valor de R$ {self.saldo:.2f}")     
        return
    
    def opextrato(self):
            print("\n=============== Você escolheu a opção Extrato ===============\n")

            for registro in self.extrato:
                data = registro["data"]
                valor = registro["valor"]
                print(f"Data: {data.strftime('%d/%m/%Y')} - Valor: {valor:.2f}")
            print(f"Seu saldo é o valor de: R$ ",self.saldo) 
            print("\n=============================================================")
            return   


extrato = []
saldo = float()
menu = SysBank()
continuar = True

while continuar:
    menu.exibir_menu()
    continuar = menu.selecionar_menu()

