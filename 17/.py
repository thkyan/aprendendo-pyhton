'''
class ControleRemoto:
    def __init__(self, cor, altura, profundidade, largura):
        self.cor = cor
        self.altura = altura
        self.prfundidade = profundidade
        self.largura = largura

    def passar_canal(self, botao):
      if botao == "+":
         print("Aumentar o canal.")
      elif botao == "-":
         print("Dimunir o canal.")
      
    

Controle_Remoto = ControleRemoto("preto", "10cm", "2cm", "2cm")
print(Controle_Remoto.cor)
Controle_Remoto.passar_canal("+")

Controle_Remoto2 = ControleRemoto("cinza", "10cm", "2cm", "2cm")
print(Controle_Remoto2.cor)
Controle_Remoto.passar_canal("-")
'''

class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.lista_planos = ['basic', 'premium']
        if plano in self.lista_planos:
            self.plano = plano
        else:
            #raise Excepition ou 
            print("plano invalido.")

    def mudar_plano(self, novo_plano):  
        if novo_plano in self.lista_planos: 
            self.plano = novo_plano
        else:
            print("plano invalido.")     

cliente = Cliente("Thayná", "thaynamatos956@gmail.com", "basic")
print(cliente.plano)
# no botão de upgrade
cliente.mudar_plano("premium")
print(cliente.plano)
    