import time
from multiprocessing import Process, Value, Array

class Processo(Process):
    def __init__(self, id_1, num_processos):
        super(Processo, self).__init__()
        self.id_1 = id_1
        self.num_processos = num_processos
        self.coordenador = Value('i', -1)
        self.status = Value('i', 1)
        self.respostas = Array('i', [-1] * num_processos)
    def run(self):
        while self.status.value == 1:
            if self.coordenador.value == -1:
                self.realizar_eleicao()
            else:
                time.sleep(3)
                if self.respostas[self.coordenador.value] == -1:
                    print("Processo {} detectou que o coordenador está inativo. Iniciando nova eleição.".format(self.id_1))
                    self.realizar_eleicao()

    def realizar_eleicao(self):
        for i in range(self.id_1 + 1, self.num_processos):
            if self.status.value == 0:
                return
            print("Processo {} enviou mensagem eleição para processo {}.".format(self.id_1, i))
            self.respostas[i] = self.id_1

        if max(self.respostas) == self.id_1:
            self.coordenador.value = self.id_1
            print("Processo {} se elegeu como coordenador.".format(self.id_1))
            for i in range(self.num_processos):
                if i != self.id_1:
                    print("Processo {} enviou mensagem coord para processo {}.".format(self.id_1, i))
                    self.respostas[i] = -1
    
    def encerrar(self):
        self.status.value = 0
        self.join()

if __name__ == "__main__":
    num_processos = 5
    processos = []
    
    for i in range(num_processos):
        p = Processo(i, num_processos)
        p.start()
        processos.append(p)

    time.sleep(15)

    for p in processos:
        p.encerrar()
