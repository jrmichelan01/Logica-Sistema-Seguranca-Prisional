import time


class SistemaPrisional:
    def __init__(self):
        self.portao_A = "FECHADO"
        self.portao_B = "FECHADO"
        self.alarme = False

    def abrir_portao_A(self):
        if self.portao_B == "FECHADO" and not self.alarme:
            self.portao_A = "ABERTO"
            print("Portão A aberto")
            self.timeout()
        else:
            print("Abertura bloqueada!")

    def fechar_portoes(self):
        self.portao_A = "FECHADO"
        self.portao_B = "FECHADO"
        print("Todos os portões fechados!")

    def timeout(self):
        print("Aguardando veículo (30s)...")
        tempo_limite = 5  # reduzido pra teste
        inicio = time.time()

        while True:
            entrada = input("Veículo entrou? (s/n): ")

            if entrada.lower() == "s":
                print("Acesso liberado!")
                self.portao_A = "FECHADO"
                self.portao_B = "ABERTO"
                break

            if time.time() - inicio > tempo_limite:
                print("Tempo excedido!")
                self.fechar_portoes()
                break

    def autenticar(self):
        placa = input("Digite a placa: ")
        re = input("Digite o RE: ")

        if placa == "ABC1234" and re == "999":
            print("Autenticado com sucesso!")
            self.abrir_portao_A()
        else:
            print("Acesso negado!")


# EXECUÇÃO
sistema = SistemaPrisional()
sistema.autenticar()
